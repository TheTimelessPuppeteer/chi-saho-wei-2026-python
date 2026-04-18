from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pygame

from robot_core import RobotState, RobotWorld


# 地圖大小（可依需求調整）。
GRID_W = 5
GRID_H = 3

CELL = 90
MARGIN = 40
PANEL_GAP = 18
PANEL_W = 260

WINDOW_SCALE = 1.2
BASE_BOARD_W = MARGIN * 2 + (GRID_W + 1) * CELL
BASE_BOARD_H = MARGIN * 2 + (GRID_H + 1) * CELL
BASE_SCREEN_W = BASE_BOARD_W + PANEL_GAP + PANEL_W + MARGIN
BASE_SCREEN_H = BASE_BOARD_H
SCREEN_W = int(BASE_SCREEN_W * WINDOW_SCALE)
SCREEN_H = int(BASE_SCREEN_H * WINDOW_SCALE)

BG_COLOR = (7, 18, 14)
BOARD_FILL_COLOR = (10, 28, 22)
GRID_COLOR = (42, 122, 90)
GRID_BOLD_COLOR = (71, 170, 129)
AXIS_COLOR = (161, 245, 201)
MATRIX_RAIN_COLOR = (50, 140, 96)
ROBOT_BODY_COLOR = (78, 145, 255)
ROBOT_HEAD_COLOR = (133, 181, 255)
ROBOT_EYE_COLOR = (235, 245, 255)
ROBOT_ACCENT_COLOR = (37, 84, 180)
SCENT_COLOR = (255, 168, 0)
TEXT_COLOR = (200, 250, 223)
LOST_COLOR = (255, 107, 107)
PANEL_BG_COLOR = (12, 36, 28)
PANEL_BORDER_COLOR = (66, 171, 126)
COORD_TEXT_SCALE = 0.9


@dataclass
class Snapshot:
    """單步快照，用於回放。"""

    x: int
    y: int
    direction: str
    lost: bool
    scents: set[tuple[int, int, str]]
    action: str


def to_screen_pos(x: int, y: int) -> tuple[int, int]:
    """把格子座標轉成螢幕座標（y 軸向上）。"""
    sx = MARGIN + x * CELL
    sy = MARGIN + (GRID_H - y) * CELL
    return sx, sy


def draw_matrix_backdrop(screen: pygame.Surface, tiny_font: pygame.font.Font) -> None:
    """畫出數學矩陣風格的背景字元。"""
    board_left = MARGIN
    board_top = MARGIN
    board_right = MARGIN + (GRID_W + 1) * CELL
    board_bottom = MARGIN + (GRID_H + 1) * CELL

    for x in range(board_left + 6, board_right - 8, 24):
        for y in range(board_top + 6, board_bottom - 8, 22):
            bit = "1" if ((x // 24 + y // 22) % 3) else "0"
            glyph = tiny_font.render(bit, True, MATRIX_RAIN_COLOR)
            glyph.set_alpha(40)
            screen.blit(glyph, (x, y))


def draw_grid(screen: pygame.Surface, small_font: pygame.font.Font) -> None:
    """畫矩陣化格線，並在每格右下角顯示座標。"""
    board_left = MARGIN
    board_top = MARGIN
    board_right = MARGIN + (GRID_W + 1) * CELL
    board_bottom = MARGIN + (GRID_H + 1) * CELL

    board_rect = pygame.Rect(
        board_left, board_top, board_right - board_left, board_bottom - board_top
    )
    pygame.draw.rect(screen, BOARD_FILL_COLOR, board_rect)
    pygame.draw.rect(screen, GRID_BOLD_COLOR, board_rect, 2)

    for x in range(GRID_W + 2):
        x0 = board_left + x * CELL
        width = 2 if x in (0, GRID_W + 1) else 1
        color = GRID_BOLD_COLOR if width == 2 else GRID_COLOR
        pygame.draw.line(screen, color, (x0, board_top), (x0, board_bottom), width)

    for y in range(GRID_H + 2):
        y0 = board_top + y * CELL
        width = 2 if y in (0, GRID_H + 1) else 1
        color = GRID_BOLD_COLOR if width == 2 else GRID_COLOR
        pygame.draw.line(screen, color, (board_left, y0), (board_right, y0), width)

    # 在每個格子右下角顯示座標 (x,y)。
    for x in range(GRID_W + 1):
        for y in range(GRID_H + 1):
            sx, sy = to_screen_pos(x, y)
            label = f"({x},{y})"
            txt = small_font.render(label, True, AXIS_COLOR)
            scaled_w = max(1, int(txt.get_width() * COORD_TEXT_SCALE))
            scaled_h = max(1, int(txt.get_height() * COORD_TEXT_SCALE))
            txt = pygame.transform.smoothscale(txt, (scaled_w, scaled_h))
            tx = sx + CELL - txt.get_width() - 5
            ty = sy + CELL - txt.get_height() - 4
            screen.blit(txt, (tx, ty))


def draw_scents(screen: pygame.Surface, scents: set[tuple[int, int, str]]) -> None:
    """畫 scent（僅畫位置，不分方向圖示）。"""
    pos_set = {(x, y) for x, y, _ in scents}
    for x, y in pos_set:
        sx, sy = to_screen_pos(x, y)
        center = (sx + CELL // 2, sy + CELL // 2)
        pygame.draw.circle(screen, SCENT_COLOR, center, 8)


def draw_robot(screen: pygame.Surface, robot: RobotState) -> None:
    """畫藍色小機器人，並讓整體隨方向旋轉。"""
    sx, sy = to_screen_pos(robot.x, robot.y)
    cx = sx + CELL // 2
    cy = sy + CELL // 2

    # 在透明畫布上先畫「朝北」機器人，再整體旋轉。
    sprite_size = 56
    sprite = pygame.Surface((sprite_size, sprite_size), pygame.SRCALPHA)
    scx = sprite_size // 2
    scy = sprite_size // 2

    # 造型維持縮小 30% 的版本。
    body = pygame.Rect(scx - 14, scy - 10, 28, 21)
    head = pygame.Rect(scx - 11, scy - 21, 21, 10)
    pygame.draw.rect(sprite, ROBOT_BODY_COLOR, body, border_radius=8)
    pygame.draw.rect(sprite, ROBOT_HEAD_COLOR, head, border_radius=6)

    # 眼睛與腳輪。
    pygame.draw.circle(sprite, ROBOT_EYE_COLOR, (scx - 4, scy - 16), 2)
    pygame.draw.circle(sprite, ROBOT_EYE_COLOR, (scx + 4, scy - 16), 2)
    pygame.draw.circle(sprite, ROBOT_ACCENT_COLOR, (scx - 7, scy + 13), 3)
    pygame.draw.circle(sprite, ROBOT_ACCENT_COLOR, (scx + 7, scy + 13), 3)

    # 朝向箭頭先畫在正上方，旋轉後會和整體一起轉。
    arrow = [(scx, scy - 25), (scx - 4, scy - 18), (scx + 4, scy - 18)]
    pygame.draw.polygon(sprite, ROBOT_ACCENT_COLOR, arrow)

    # LOST 時畫紅色叉叉提示（也會跟著整體旋轉）。
    if robot.lost:
        pygame.draw.line(
            sprite, LOST_COLOR, (scx - 13, scy - 13), (scx + 13, scy + 13), 3
        )
        pygame.draw.line(
            sprite, LOST_COLOR, (scx + 13, scy - 13), (scx - 13, scy + 13), 3
        )

    angle_map = {
        "N": 0,
        "E": -90,
        "S": 180,
        "W": 90,
    }
    rotated = pygame.transform.rotate(sprite, angle_map[robot.direction])
    rect = rotated.get_rect(center=(cx, cy))
    screen.blit(rotated, rect)


def draw_hud(
    screen: pygame.Surface,
    font: pygame.font.Font,
    small_font: pygame.font.Font,
    robot: RobotState,
    scents: set[tuple[int, int, str]],
    replay_mode: bool,
) -> None:
    """在側邊面板畫文字資訊，每個資訊項目分行。"""
    panel_left = MARGIN + (GRID_W + 1) * CELL + PANEL_GAP
    panel_top = MARGIN
    panel_right = SCREEN_W - MARGIN
    panel_bottom = MARGIN + (GRID_H + 1) * CELL

    panel_rect = pygame.Rect(
        panel_left,
        panel_top,
        panel_right - panel_left,
        panel_bottom - panel_top,
    )
    pygame.draw.rect(screen, PANEL_BG_COLOR, panel_rect, border_radius=10)
    pygame.draw.rect(screen, PANEL_BORDER_COLOR, panel_rect, 2, border_radius=10)

    status = "LOST" if robot.lost else "ALIVE"
    mode = "REPLAY" if replay_mode else "LIVE"

    title = font.render("MATRIX HUD", True, TEXT_COLOR)
    screen.blit(title, (panel_left + 16, panel_top + 14))

    info_lines = [
        f"x = {robot.x}",
        f"y = {robot.y}",
        f"direction = {robot.direction}",
        f"status = {status}",
        f"mode = {mode}",
        f"scents = {len(scents)}",
        f"grid = [0..{GRID_W}] x [0..{GRID_H}]",
    ]

    y = panel_top + 54
    for line in info_lines:
        img = small_font.render(line, True, TEXT_COLOR)
        screen.blit(img, (panel_left + 16, y))
        y += 28

    controls_title = small_font.render("Controls", True, PANEL_BORDER_COLOR)
    screen.blit(controls_title, (panel_left + 16, y + 4))
    y += 34

    control_lines = [
        "L/R/F : turn & step",
        "N/C : new robot / clear scent",
        "P/S/ESC : replay / shot / quit",
    ]
    for line in control_lines:
        img = small_font.render(line, True, TEXT_COLOR)
        screen.blit(img, (panel_left + 16, y))
        y += 24


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Robot Lost - Week 03")
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 20)
    small_font = pygame.font.SysFont("consolas", 16)

    world = RobotWorld(GRID_W, GRID_H)
    robot = RobotState(0, 0, "N")

    history: list[Snapshot] = []

    def save_snapshot(action: str) -> None:
        history.append(
            Snapshot(
                x=robot.x,
                y=robot.y,
                direction=robot.direction,
                lost=robot.lost,
                scents=set(world.scents),
                action=action,
            )
        )

    save_snapshot("INIT")

    replay_mode = False
    replay_idx = 0
    replay_tick = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if replay_mode:
                    continue

                if event.key == pygame.K_l:
                    world.step(robot, "L")
                    save_snapshot("L")
                elif event.key == pygame.K_r:
                    world.step(robot, "R")
                    save_snapshot("R")
                elif event.key == pygame.K_f:
                    world.step(robot, "F")
                    save_snapshot("F")
                elif event.key == pygame.K_n:
                    # 產生新機器人，但保留 scent。
                    robot = RobotState(0, 0, "N")
                    save_snapshot("NEW")
                elif event.key == pygame.K_c:
                    world.clear_scents()
                    save_snapshot("CLEAR_SCENT")
                elif event.key == pygame.K_p and history:
                    replay_mode = True
                    replay_idx = 0
                    replay_tick = 0
                elif event.key == pygame.K_s:
                    out_path = Path(__file__).with_name("assets") / "gameplay.png"
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    pygame.image.save(screen, str(out_path))

        if replay_mode:
            replay_tick += 1
            if replay_tick >= 20:  # 約每 0.33 秒前進一格
                replay_tick = 0
                replay_idx += 1
                if replay_idx >= len(history):
                    replay_mode = False
                    replay_idx = 0

            snap = history[min(replay_idx, len(history) - 1)]
            show_robot = RobotState(snap.x, snap.y, snap.direction, snap.lost)
            show_scents = snap.scents
        else:
            show_robot = robot
            show_scents = world.scents

        screen.fill(BG_COLOR)
        draw_matrix_backdrop(screen, small_font)
        draw_grid(screen, small_font)
        draw_scents(screen, show_scents)
        draw_robot(screen, show_robot)
        draw_hud(screen, font, small_font, show_robot, show_scents, replay_mode)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

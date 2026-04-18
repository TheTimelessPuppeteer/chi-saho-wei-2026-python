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
HUD_H = 140

SCREEN_W = MARGIN * 2 + (GRID_W + 1) * CELL
SCREEN_H = MARGIN * 2 + (GRID_H + 1) * CELL + HUD_H

BG_COLOR = (24, 26, 34)
GRID_COLOR = (90, 96, 120)
ROBOT_BODY_COLOR = (78, 145, 255)
ROBOT_HEAD_COLOR = (133, 181, 255)
ROBOT_EYE_COLOR = (235, 245, 255)
ROBOT_ACCENT_COLOR = (37, 84, 180)
SCENT_COLOR = (255, 168, 0)
TEXT_COLOR = (230, 232, 244)
LOST_COLOR = (255, 107, 107)


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


def draw_grid(screen: pygame.Surface) -> None:
    """畫地圖格線。"""
    for x in range(GRID_W + 2):
        x0 = MARGIN + x * CELL
        y0 = MARGIN
        y1 = MARGIN + (GRID_H + 1) * CELL
        pygame.draw.line(screen, GRID_COLOR, (x0, y0), (x0, y1), 1)

    for y in range(GRID_H + 2):
        y0 = MARGIN + y * CELL
        x0 = MARGIN
        x1 = MARGIN + (GRID_W + 1) * CELL
        pygame.draw.line(screen, GRID_COLOR, (x0, y0), (x1, y0), 1)


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
    robot: RobotState,
    scents: set[tuple[int, int, str]],
    replay_mode: bool,
) -> None:
    """畫文字資訊。"""
    hud_top = MARGIN + (GRID_H + 1) * CELL + 18

    status = "LOST" if robot.lost else "ALIVE"
    mode = "REPLAY" if replay_mode else "LIVE"
    line1 = (
        f"Robot=({robot.x},{robot.y},{robot.direction})  Status={status}  Mode={mode}"
    )
    line2 = f"Scents={len(scents)} | Keys: L/R/F step, N new robot, C clear scent, P replay, S screenshot, ESC quit"

    img1 = font.render(line1, True, TEXT_COLOR)
    img2 = font.render(line2, True, TEXT_COLOR)
    screen.blit(img1, (MARGIN, hud_top))
    screen.blit(img2, (MARGIN, hud_top + 34))


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Robot Lost - Week 03")
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 20)

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
        draw_grid(screen)
        draw_scents(screen, show_scents)
        draw_robot(screen, show_robot)
        draw_hud(screen, font, show_robot, show_scents, replay_mode)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

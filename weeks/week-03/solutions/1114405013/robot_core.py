from dataclasses import dataclass


# 方向旋轉規則（順時針與逆時針）。
LEFT_TURN = {
    "N": "W",
    "W": "S",
    "S": "E",
    "E": "N",
}

RIGHT_TURN = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N",
}

# 前進位移表。
MOVE_DELTA = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass
class RobotState:
    """機器人狀態。"""

    x: int
    y: int
    direction: str
    lost: bool = False


class RobotWorld:
    """Robot Lost 的規則世界。"""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        # scent 記錄格式：(x, y, direction)
        self.scents: set[tuple[int, int, str]] = set()

    def in_bounds(self, x: int, y: int) -> bool:
        """判斷座標是否在地圖範圍內（含邊界）。"""
        return 0 <= x <= self.width and 0 <= y <= self.height

    def clear_scents(self) -> None:
        """清除所有 scent。"""
        self.scents.clear()

    def step(self, robot: RobotState, command: str) -> None:
        """執行一步指令。"""
        if robot.lost:
            # LOST 後不再執行任何指令。
            return

        if command == "L":
            robot.direction = LEFT_TURN[robot.direction]
            return

        if command == "R":
            robot.direction = RIGHT_TURN[robot.direction]
            return

        if command == "F":
            dx, dy = MOVE_DELTA[robot.direction]
            nx, ny = robot.x + dx, robot.y + dy

            if self.in_bounds(nx, ny):
                robot.x, robot.y = nx, ny
                return

            # 若會越界，先檢查同位置同方向是否已有 scent。
            scent_key = (robot.x, robot.y, robot.direction)
            if scent_key in self.scents:
                # 有 scent 就忽略這次危險前進。
                return

            # 沒有 scent：本台機器人 LOST，並留下 scent。
            self.scents.add(scent_key)
            robot.lost = True
            return

        # 非法指令策略：拋出例外讓上層明確處理。
        raise ValueError(f"Unsupported command: {command}")

    def run(self, robot: RobotState, commands: str) -> RobotState:
        """依序執行多步指令，回傳最終狀態。"""
        for ch in commands:
            self.step(robot, ch)
            if robot.lost:
                break
        return robot

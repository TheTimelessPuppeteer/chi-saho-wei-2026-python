import sys
import unittest
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parents[1]))

from robot_core import RobotState, RobotWorld  # noqa: E402


class TestRobotCore(unittest.TestCase):
    """robot_core 基本規則測試。"""

    def setUp(self) -> None:
        self.world = RobotWorld(5, 3)

    def test_turn_left_from_north(self) -> None:
        # 最低清單：N + L = W
        robot = RobotState(1, 1, "N")
        self.world.step(robot, "L")
        self.assertEqual(robot.direction, "W")

    def test_turn_right_from_north(self) -> None:
        # 最低清單：N + R = E
        robot = RobotState(1, 1, "N")
        self.world.step(robot, "R")
        self.assertEqual(robot.direction, "E")

    def test_four_right_turns_back_to_origin_direction(self) -> None:
        # 最低清單：連續四次右轉回原方向
        robot = RobotState(1, 1, "N")
        self.world.run(robot, "RRRR")
        self.assertEqual(robot.direction, "N")

    def test_forward_inside_boundary_not_lost(self) -> None:
        # 最低清單：邊界內移動不會 LOST
        robot = RobotState(1, 1, "N")
        self.world.step(robot, "F")
        self.assertEqual((robot.x, robot.y), (1, 2))
        self.assertFalse(robot.lost)

    def test_forward_out_of_boundary_becomes_lost(self) -> None:
        # 最低清單：邊界往外 F 會 LOST
        robot = RobotState(0, 3, "N")
        self.world.step(robot, "F")
        self.assertTrue(robot.lost)

    def test_invalid_command_raises_value_error(self) -> None:
        # 最低清單：非法指令需有明確策略（本實作採拋出例外）
        robot = RobotState(1, 1, "N")
        with self.assertRaises(ValueError):
            self.world.step(robot, "X")


if __name__ == "__main__":
    unittest.main()

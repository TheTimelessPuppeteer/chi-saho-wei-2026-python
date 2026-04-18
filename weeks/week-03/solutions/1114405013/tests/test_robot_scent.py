import sys
import unittest
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parents[1]))

from robot_core import RobotState, RobotWorld  # noqa: E402


class TestRobotScent(unittest.TestCase):
    """robot_core 的 scent 與 LOST 規則測試。"""

    def setUp(self) -> None:
        self.world = RobotWorld(5, 3)

    def test_first_robot_lost_and_leave_scent(self) -> None:
        # 最低清單：第一台越界後要留下 scent
        robot = RobotState(0, 3, "N")
        self.world.step(robot, "F")

        self.assertTrue(robot.lost)
        self.assertIn((0, 3, "N"), self.world.scents)

    def test_second_robot_ignores_dangerous_forward_with_same_state(self) -> None:
        # 最低清單：第二台在相同 (x,y,dir) 會忽略危險 F
        self.world.step(RobotState(0, 3, "N"), "F")

        robot2 = RobotState(0, 3, "N")
        self.world.step(robot2, "F")

        self.assertFalse(robot2.lost)
        self.assertEqual((robot2.x, robot2.y, robot2.direction), (0, 3, "N"))

    def test_same_cell_different_direction_not_share_scent(self) -> None:
        # 最低清單：同格不同方向不共用 scent
        self.world.step(RobotState(0, 3, "N"), "F")

        # 這裡方向改成 W，同樣在 (0,3) 往前會越界，但 scent 只記 N 方向
        # 所以不會被保護，仍然應該 LOST。
        robot2 = RobotState(0, 3, "W")
        self.world.step(robot2, "F")
        self.assertTrue(robot2.lost)

    def test_lost_robot_stops_processing_remaining_commands(self) -> None:
        # 最低清單：LOST 後不再執行後續指令
        robot = RobotState(0, 3, "N")
        self.world.run(robot, "FRRF")

        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y, robot.direction), (0, 3, "N"))

    def test_clear_scent(self) -> None:
        # 清除 scent 後，相同危險位置會再次 LOST
        self.world.step(RobotState(0, 3, "N"), "F")
        self.world.clear_scents()

        robot2 = RobotState(0, 3, "N")
        self.world.step(robot2, "F")
        self.assertTrue(robot2.lost)


if __name__ == "__main__":
    unittest.main()

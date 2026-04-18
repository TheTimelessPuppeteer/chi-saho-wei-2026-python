# TEST_LOG

## Run 1 - Red (預期失敗)

- 指令：

```bash
python -m unittest discover -s weeks/week-03/solutions/1114405013/tests -p "test_*.py" -v
```

- 結果摘要：
  - 測試總數：2（測試模組載入）
  - 通過：0
  - 失敗：0
  - 錯誤：2
  - 主要錯誤：`ModuleNotFoundError: No module named 'robot_core'`

- 從失敗到修正：
  - 新增 `robot_core.py`（`RobotState`、`RobotWorld`、`scent` 規則）。
  - 補齊 `step/run/clear_scents` 等核心行為。

---

## Run 2 - Green (全通過)

- 指令：

```bash
python -m unittest discover -s weeks/week-03/solutions/1114405013/tests -p "test_*.py" -v
```

- 結果摘要：
  - 測試總數：11
  - 通過：11
  - 失敗：0
  - 錯誤：0

- 重構說明：
  - 把「同格不同方向不共用 scent」測試案例改得更直接（使用 `(0,3,W)+F`）。
  - 保持所有測試持續綠燈。

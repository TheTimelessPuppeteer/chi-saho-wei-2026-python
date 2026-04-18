# Week 03 - Robot Lost (pygame)

## 1) 功能清單

- 規則核心獨立在 `robot_core.py`，可單獨測試（不依賴 pygame）
- `robot_game.py` 提供互動視覺化：
  - 顯示格子地圖
  - 顯示機器人位置與朝向
  - 顯示 scent
  - 逐步輸入 `L/R/F`
  - `N` 建立新機器人（保留 scent）
  - `C` 清除 scent
  - `P` 回放歷史步驟
  - `S` 匯出螢幕截圖到 `assets/gameplay.png`

## 2) 執行方式

- Python 版本：建議 `3.11+`
- 安裝 pygame：

```bash
python -m pip install pygame
```

- 啟動遊戲：

```bash
python weeks/week-03/solutions/1114405013/robot_game.py
```

## 3) 測試方式

- 指令：

```bash
python -m unittest discover -s weeks/week-03/solutions/1114405013/tests -p "test_*.py" -v
```

- 目前結果：`11 tests, 11 passed`

## 4) 資料結構選擇理由

1. `RobotState` 用 `dataclass`：欄位明確，狀態更新可讀性高。
2. `scent` 用 `set[(x, y, dir)]`：查詢/插入 O(1)，且天然去重。
3. 方向用字典（`LEFT_TURN`/`RIGHT_TURN`/`MOVE_DELTA`）：規則集中、易維護。

## 5) 一個踩到的 bug 與修正

- 問題：一開始把 scent 只記 `(x, y)`，導致同格不同方向被錯誤保護。
- 修正：改成 `(x, y, dir)`，並補上測試 `test_same_cell_different_direction_not_share_scent`。

## 6) 遊玩截圖

> 可在遊戲執行中按 `S` 產生 `assets/gameplay.png`。

![gameplay](assets/gameplay.png)

## 7) 重播方式

- 在遊戲中按 `P` 進入回放模式，按步驟重播歷史操作。
- 本版本提供「內建回放機制」；若要 GIF，可再加上額外錄製流程。

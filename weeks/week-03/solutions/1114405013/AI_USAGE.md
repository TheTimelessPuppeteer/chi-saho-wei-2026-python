# AI_USAGE

## 1) 問 AI 的問題（3~5 題）

1. `Robot Lost` 的 scent 應該記錄哪些欄位？
2. 如何把可測試的規則邏輯與 pygame 畫面分離？
3. `unittest` 最低 10 個測試要如何分組（core/scent）？
4. LOST 後繼續收到指令時，核心函式應該怎麼處理？

## 2) 採用的建議與原因

- 採用 `scent = set[(x, y, dir)]`：查詢快且符合題意（方向不可省略）。
- 採用 `robot_core.py` + `robot_game.py` 模組分離：便於 TDD 與維護。
- 採用 `dataclass RobotState`：狀態欄位清楚、測試可讀性高。

## 3) 拒絕的建議與原因

- 拒絕把規則寫在 pygame 事件迴圈裡：會讓測試困難、耦合過高。
- 拒絕用全域 mutable 變數散落多處：追蹤狀態會變複雜。

## 4) AI 建議不完整、我自行修正的案例

- 不完整建議：只用 `(x, y)` 當 scent key。
- 問題：會錯誤地讓「同格不同方向」也被保護。
- 修正：改成 `(x, y, dir)`，並新增對應測試驗證。

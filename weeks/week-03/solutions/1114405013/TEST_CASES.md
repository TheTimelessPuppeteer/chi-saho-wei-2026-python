# TEST_CASES

以下測資對應 `tests/test_robot_core.py` 與 `tests/test_robot_scent.py`。

| # | 輸入（初始 + 指令） | 預期結果 | 實際結果 | PASS/FAIL | 對應測試函式 |
|---|---|---|---|---|---|
| 1 | `(1,1,N) + L` | 方向變 `W` | `W` | PASS | `test_turn_left_from_north` |
| 2 | `(1,1,N) + R` | 方向變 `E` | `E` | PASS | `test_turn_right_from_north` |
| 3 | `(1,1,N) + RRRR` | 回到 `N` | `N` | PASS | `test_four_right_turns_back_to_origin_direction` |
| 4 | `(0,3,N) + F`（地圖 5x3） | 越界並 `LOST` | `LOST=True` | PASS | `test_forward_out_of_boundary_becomes_lost` |
| 5 | `(1,1,N) + F`（地圖 5x3） | 移到 `(1,2)` 且非 LOST | `(1,2), LOST=False` | PASS | `test_forward_inside_boundary_not_lost` |
| 6 | 第一台 `(0,3,N)+F`，第二台 `(0,3,N)+F` | 第二台忽略危險 F、不 LOST | 停在 `(0,3,N), LOST=False` | PASS | `test_second_robot_ignores_dangerous_forward_with_same_state` |
| 7 | 第一台在 `(0,3,N)` 留 scent，第二台 `(0,3,W)+F` | 同格不同向不共用 scent，第二台 LOST | `LOST=True` | PASS | `test_same_cell_different_direction_not_share_scent` |
| 8 | `(0,3,N)+FRRF` | 第一步 LOST 後不再執行後續指令 | 位置方向維持 `(0,3,N)` | PASS | `test_lost_robot_stops_processing_remaining_commands` |
| 9 | 先留 scent 再 `clear_scents()`，第二台同位置方向 `F` | scent 清除後再次 LOST | `LOST=True` | PASS | `test_clear_scent` |
| 10 | `(1,1,N) + X` | 非法指令明確處理（拋 `ValueError`） | 拋出 `ValueError` | PASS | `test_invalid_command_raises_value_error` |

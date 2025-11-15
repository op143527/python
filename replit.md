# Python 學習專案

## 專案概述
這是一個 Python 基礎學習專案，包含多個課程的練習檔案。專案採用中文註解和教學，適合 Python 初學者。

## 專案結構
```
├── class1/          # 第一課：基礎概念
│   └── prj01.py    # 註解、資料型態、變數、運算子
├── class2/          # 第二課：函式與輸入
│   └── prj02.py    # 字串格式化、內建函式、使用者輸入
├── class3/          # 第三課：錯誤處理與條件判斷
│   ├── prj03.py    # Try-Except、比較運算子、If-Elif-Else
│   └── homework.py # 華氏轉攝氏溫度計算
├── class4/          # 第四課：實作練習
│   ├── prj04.py    # 成績等級判斷
│   └── prj04-1.py  # 奇偶數判斷
└── main.py          # 主選單介面
```

## 課程內容

### 第一課 - 基礎概念 (class1/prj01.py)
- 單行與多行註解
- 基本資料型態：int, float, str, bool
- 變數宣告與命名規則
- 算術運算子：+, -, *, /, %, **, //
- 運算子優先順序
- 字串運算

### 第二課 - 函式與輸入 (class2/prj02.py)
- f-string 字串格式化
- 內建函式：max(), len(), type()
- 型態轉換：str(), int(), float(), bool()
- input() 函式與使用者輸入
- 實作練習：圓形面積計算

### 第三課 - 錯誤處理與條件判斷 (class3/prj03.py)
- try-except 錯誤處理
- 指定錯誤類型：ValueError, ZeroDivisionError
- else 和 finally 子句
- 比較運算子：==, !=, >, <, >=, <=
- 邏輯運算子：and, or, not
- if-elif-else 條件判斷

### 第三課 - 作業 (class3/homework.py)
- 華氏轉攝氏溫度計算器
- 結合 try-except 和使用者輸入

### 第四課 - 實作練習
- **prj04.py**: 成績等級判斷（A-E 等級）
- **prj04-1.py**: 奇偶數判斷

## 如何使用
執行 `main.py` 啟動主選單，可以選擇執行任何一個課程練習：
```bash
python main.py
```

## 環境需求
- Python 3.11+
- 無額外套件依賴（使用標準函式庫）

## 最近更新
- 修復 class4/prj04.py 中的 typo (int1 → int)
- 新增主選單介面 (main.py) 方便執行各個練習
- 新增 .gitignore 和專案文件

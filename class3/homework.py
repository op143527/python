try:  # 嘗試轉換成浮點數
    f = float(input("請輸入華氏溫度"))
    c = (f - 32) * 5 / 9
    print(f"華氏溫度{f}F等於攝氏{c}:C")
except:
    print("輸入錯誤!")

# 猜數字遊戲
import random

x = random.randint(1, 100)  # 產生1到1000之間的隨機整數
v = 0  # 猜測次數
print("歡迎來到猜數字遊戲?請在1到10之間猜一個數字。")
while True:
    y = input("請輸入你的猜測（或輸入 'exit' 離開遊戲）：")
    if y.lower() == "exit":
        print("遊戲結束，感謝你的參與！")
        break
    try:
        t = int(y)
        v += 1
        if t < 1 or t > 100:
            print("請輸入1到100之間的數字。")
            continue
        if t < x:
            print("太小了！再試一次。")
        elif t > x:
            print("太大了！再試一次。")
        else:
            print(f"恭喜你！猜對了，答案是 {x}。你總共猜了 {v} 次。")
            break
    except ValueError:
        print("請輸入有效的數字。")

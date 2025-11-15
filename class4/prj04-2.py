
 import turtle as x

# 匯入模組turtle並命名為x
x.forward(100)
x.right(90)
x.forward(100)
x.right(90)
x.left(90)
x.forward(100)
x.right(90)
x.forward(100)
x.right(90)
x.left(90)
x.forward(100)
x.right(90)
x.forward(100)
x.right(90)
x.left(90)
x.forward(100)
x.right(90)
x.forward(100)
x.left(90)
x.done()

# 使用turtle模組繪製一個由多個正方形組成的圖案
# 每個正方形的邊長為100單位，並且每個正方形之間有90度的轉向
# 最後使用x.done()來結束繪圖並保持視窗開啟

# for example
# for的組成有三個部分：初始值、條件、遞增值
# for i in range(5):  # 初始值為0，條件為i小於5，遞增值為1
#     print(i)  # 印出0到4的數字
# range(5)會產生一個從0到4的數列
# range(2, 6)會產生一個從2到5的數列
# range(1, 10, 2)會產生一個從1到9的奇數數列
# for 迴圈變數只能活在for迴圈裡面
# 迴圈變數每回合都會從範圍中取出一個值
import turtle as x

for i in range(10000000):  # 外層迴圈控制正方形的數量
    for i in range(4):  # 內層迴圈控制每個正方形的邊
        x.forward(100)  # 向前移動100單位
        x.right(90)  # 右轉90度
    x.right(90)  # 每畫完一個正方形後右轉90度，準備畫下一個正方形
x.done()  # 結束繪圖並保持f視窗開啟


# 使用巢狀迴圈繪製多個正方形組成的圖案
# 外層迴圈控制正方形的數量，內層迴圈控制每個正方形的邊
# 每個正方形的邊長為100單位，並且每個正方形之間有90度的轉向
# 最後使用x.done()來結束繪圖並保持視窗開啟

# 蓋章示範
import turtle as x

x.penup()  # 提起畫筆，移動時不會畫線
x.goto(-100, 0)  # 移動到座標(-100, 0)
x.pendown()  # 放下畫筆，開始畫線
x.circle(50)  # 畫一個半徑為50的圓


import turtle as x

x.penup()  # 提起畫筆，移動時不會畫線
x.color("red")  # 將畫筆顏色改為某種顏色
x.shape("turtle")  # 將畫筆形狀改為烏龜形狀
for i in range(100006):  # 畫?個蓋章
    x.stamp()  # 蓋章
    x.right(10)  # 右轉10度
x.done()  # 結束繪圖並保持視窗開啟

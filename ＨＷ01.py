import turtle

t = turtle.Turtle()
t.speed(0)   # 讓烏龜畫最快

# 畫一個小箭頭的函式
def draw_arrow():
	t.forward(20)       # 往前畫出箭身
	t.left(150)         # 開始畫箭頭
	t.forward(10)
	t.back(10)
	t.right(300)        # 畫另一邊箭頭
	t.forward(10)
	t.back(10)
	t.left(150)         # 將方向調回原方向

# 開始畫 8 個箭頭
for i in range(8):
	t.penup()
	t.home()            # 回到位置 (0,0)
	t.setheading(i * 45) # 每次轉 45 度（360/8）
	t.forward(40)        # 往外移動到適合位置
	t.pendown()          # 畫箭頭
	draw_arrow()         # 畫箭頭

turtle.done() # 讓視窗不會自動關閉

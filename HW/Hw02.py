import turtle as t
# 匯入 turtle 模組
import time as s

t.speed(0)

t.pensize(5)
t.shape("turtle")
t.color("red")
t.pendown()
for i in range(10000):
	t.forward(100)
	# 往前畫出箭身
	t.back(100)
	s.sleep(1)
	t.clear()
	t.right(6)  # 畫箭頭sss
t.done()
# 讓視窗不會自動關閉
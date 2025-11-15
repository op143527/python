import turtle as x

x.tracer(False)
x.penup()
x.shape("circle")
for i in  range(100):
	x.forward(10)
	x.stamp()
	x.right(10)
x.update()
x.done()
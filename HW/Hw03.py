n=int(input("請輸入要印出的箭頭大小: "))
for i in range(1,n+1):
	print(" "*(n-i)+"*"*(2*i-1))
for i in range(n):
	print(" "*(n-1)+"*")
n = int(input("請輸入正整數: "))

for i in range(1, n + 1): # 從 1 到 n，每次加 1
	if i % 3 == 0 or i % 7 == 0:	# 如果 i 可以被 3 或 7 整除
		print(i）  # 印出 i.                  
	
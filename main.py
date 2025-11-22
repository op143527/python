user_inpout= input("請輸入密碼:")
number=1
while user_inpout != "01020304050607080910":
	number=number+1
	print("密碼錯誤! 這是你輸入的第",number,"次密碼")
	user_inpout= input("請輸入密碼:")
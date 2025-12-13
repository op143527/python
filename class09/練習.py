weather = ["晴天", "多雲", "雨天", "晴天", " 多雲", "雷陣雨", "晴天"]
x = weather
z = "本產品可能會罵髒話，請小心使用"
print(x)
print(z)
while True:
    try:
        day = int(input("請輸入要修改得星期數字(1~7):"))
    except:
        print("print("87喔!",TM的不要亂搞喔!""輸入1-7之間的數字","不要當智障,謝謝尼!,SB")")
        
        continue
    if day < 1 or day > 7:
        print("請輸入1到7之間的數字喔!")
        continue
    new_weather = input("請輸入要修改的天氣狀況:")
    x[day - 1] = new_weather
    print("修改後的天氣狀況為:", x)
    break

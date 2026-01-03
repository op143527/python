# 字串格式化 f-string
name = "Alice"
age = 30
print(f"我叫{name}，我今年{age}歲。")
# 只要在字串的前面加上 f 或 F，就可以在字串中直接使用大括號 {}
# 把想要帶入的變數或運算任何資料都放進去
# 就可以形成一個新的字串
# 這種方式稱為 f-string


# 函式是由名稱和參數組成（提供的材料）組成 每一個參數都要用逗號隔開
# max()函式 會回傳提供的參數（數字）中最大的值
print(max(10, 20, 30, 40, 50))

# len()函式,會回傳提供的參數（字串）的長度
print(len("Hello, World!"))

# type()函式 會回傳提供的參數（資料）的資料型態
print(type(123))
print(type("Hello"))
print(type(3.14))
print(type(True))

# str()函式 會把提供的參數（資料）轉換成字串型態
print(str(123))
print(str(3.14))
print(str(True))
print(str("100"))

# int()函式 會把提供的參數（資料）轉換成整數型態
print(int("123"))
print(int(3.99))
print(int(True))
print(int(False))

# float()函式 會把提供的參數（資料）轉換成浮點數型態
print(float("3.14"))
print(float(100))
print(float(True))
print(float(False))

# bool()函式 會把提供的參數（資料）轉換成布林值型態
print(bool(1))
print(bool(0))
print(bool("Hello"))
print(bool(""))

# input()函式 會讓程式暫停並等待使用者輸入資料???
# 使用者輸入的資料會以字串型態回傳
name = input("請輸入你的名字：")  # 提示的文字會顯示在螢幕上不會被儲存
print(f"你好，{name}！")
age = input("請輸入你的年齡：")

# 注意：input()函式回傳的資料型態是字串
# 如果需要其他型態的資料，必須自行轉換
age = int(age)  # 將字串轉換成整數型態
print(f"你100000000年後{age+10000000}歲了！")

# 圓形面積
半徑 = float(input("請輸入圓形的半徑："))
面積 = 3.14 * 半徑 * 半徑
print(f"圓形的面積是：{面積}")

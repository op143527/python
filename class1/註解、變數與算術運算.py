# 這是單行註解
print("Hello, World!")  # 這是單行註解
# print("Hello, World!")  #這行程式碼不會被執行
# print("Hello, World!")  #ctrl + ? 會變成註解
"""
這是多行註解
這是多行註解
這是多行註解            
這是多行註解
這是多行註解    
"""
# 🐔本型態
print(123)  # 整數Integer, int
print(3.14)  # 浮點數Float, float
print("Hello, World!")  # 字串String, str
print(True)  # 布林值Boolean, bool
print(False)  # 布林值Boolean, bool

# 變數
# 變數是存放資料的空間每個變數都有自己的名稱
# 變數名稱只能包含英文字母、數字、底線，且不能以數字開頭
# 要存啥都行，但不能用Python的關鍵字當變數名稱
# 變數名稱建議使用有意義的名稱，且使用小寫字母和底線來分隔單字
# = 的功能是將右邊的資料存到給左邊的變數
a = 765628465694321
b = 674578573957436
h = 475737838383820
c = a + b + h
print(c)

# 算術運算子
print(3 + 5)  # 加法
print(10 - 2)  # 減法
print(4 * 6)  # 乘法
print(8 / 2)  # 除法
print(7 % 3)  # 取餘數
print(2**3)  # 次方
print(10 // 3)  # 取整數商
print(10 / 4)  # 小🌲除法

# 運算子優先順序
# 1. 括號()
# 2. 次方**
# 3. +-正負號
# 4. 乘法* 除法/ 取餘數% 取整數商//
# 5. 加減+-
print(3 + 5 * 2)  # 先乘除後加減

# 字串運算
print("Hello" + "World")  # 字串串接
print("Hello" * 3)  # 字串重複
# print("Hello" - "o")  # 字串無法相減
# print("Hello" / 2)  # 字串無法相除
# print("Hello" % 2)  # 字串無法取餘數
# print("Hello" ** 2)  # 字串無法次方
# print("Hello" // 2)  # 字串無法取整數商
# 除了加法和乘法，其他運算子都不能用在字串上
# 字串跟字串之間只能用加法
# 字串跟數字之間只能用乘法
# 字串不能用在其他運算子上
# 字串可以用在加法和乘法上

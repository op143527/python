# try except 錯誤處理
# 使用 try except 可以在執行過程中發生錯誤時 ,繼續執行下去
# 可以用冒號(:)縮排來區分 try 和 except
try:
    n = int(input("請輸入一個數字:"))  # 這是裝在 try 裡面的程式碼
    print(f"輸入的數字是 {n}  再加一是 {n+1}")
except:
    print("輸入的不是數字喔!")  # 這是裝在 except 裡面的程式碼
print("程式繼續執行...")

# 當使用者輸入的不是數字時 ,程式不會當掉 ,而是會執行 except 裡面的程式碼
# 然後繼續執行後面的程式碼
# except也可以指定錯誤類型 ,例如 ValueError代表數值錯誤
# 這樣只有在發生數值錯誤時 ,才會執行 except 裡面的程式碼
# 所以except可以有多個 ,分別處理不同的錯誤類型

try:
    n = int(input("請輸入一個數字:"))
    print(f"輸入的數字是 {n}  再加一是 {n+1}")
    result = 10 / n
except ValueError:
    print("輸入的不是數字喔!")
except ZeroDivisionError:
    print("你輸入不數字不能是0!")
except:  # 最少要有一個 except 來來代表其他錯誤
    print("發生其他錯誤!")
else:  # (可選) 如果沒有發生錯誤 ,就會執行 else 裡面的程式碼
    print("你入的數字沒有錯誤喔!")
# 如果try裡面的程式碼不管有沒有發生錯誤 ,都會執行 elsa 裡面的程式碼
finally:  # (可選) 不管有沒有發生錯誤 ,都會執行 finally 裡面的程式碼
    print("不管有沒有錯誤 ,都會被執行都會被執行!")
# finally   裡面的程式碼不管有沒有錯都會執行

# 比較運算子
print(5 == 5)  # True, 5等於5
print(5 != 3)  # True, 5不等於3
print(5 > 3)  # True, 5大於3
print(3 < 5)  # True, 3小於5
print(5 >= 5)  # True, 5大於等於5
print(3 <= 5)  # True, 3小於等於5

# 邏輯運算子
# and 代表全部條件都要成立才會回傳True
print(True and False)  # False, True和False
print(True and True)  # True, True和True

# or 代表只要有一個條件成立就會回傳True
print(False or True)  # True, False或True
print(False or False)  # False, False或False

# not 代表將原本的布林值相反
print(not True)  # False, 非True
print(not False)  # True, 非False

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. + - 正負號
# 4. * / // % 乘 除 取商 取餘數
# 5. + - 加 減
# 6. == != > < >= <= 比較運算子
# 7. not 非
# 8. and 且
# 9. or 或

# if 條件判斷
# if 後面接條件，條件成立就會執行縮排內的程式碼
# 可以有多個elif，代表其他條件，也可以沒有
# 最後可以有一個else，代表前面的條件都不成立時執行, else也是可以沒有的
pwd = input("請輸入密碼: ")
if pwd == "apple":
    print("歡迎apple回來!")
elif pwd == "sea food":
    print("歡迎sea food回來!")
elif pwd == "student" or pwd == "Student":
    print("歡迎student回來!")
else:
    print("what's your name?")

# if-elif-else使用的時機
# 在有多個有關聯的條件需要判斷時使用，最後只會執行一個區塊
# 多個if使用的時機在每個條件是獨立運作的時候使用，可能會執行多個區塊

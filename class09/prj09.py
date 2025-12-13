# List=更新資料
# 用起來跟一般的變數很像
# 要注意的是記得指定index(編號)位置
L = ["apple", "banana", "cherry"]
L[1] = "orange"  # 將索引1的位置改成orange

# call by value
# 在一般情況下，存資料到變數當中是採用 call by value 的方式
a = 1
b = a  # 複製 a 的值給 b
b = 2
print(a, b)


# call by reference
a = [1, 2, 3]
b = a  # 把 a 跟 b 指向同一個記憶體位置，所以改變 b 的值，a 也會跟著改變
b[0] = 2
print(a, b)


a = [1, 2, 3]
b = a.copy()  # 複製 a 的值給 b，但是 b 跟 a 指向不同的記憶體位置
b[0] = 2
print(a, b)

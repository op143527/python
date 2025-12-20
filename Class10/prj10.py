# append 可以再以存在的List當中加入新的資料
# 可以在程式執行過程當中可以將資料加入到以存在的List當中
# insert在程式執行的過成當中可以將資料加入到列表的"指定位置"
# 記得List的index是從0開始
# 如果新增的位置超過List的長度,會自動加入到最後面
# 如果新增的位置是負數,會從List的最後面開始算起,例如-1是最後一個位置
L = [
    "hello",
    "world",
]
L.insert(1, "python")
print(L)
L.insert(-1, "Java")  # 在倒數第一個位置加入 Java
print(L)  # ['Hello', 'Python', 'Java', 'World']
L.insert(-100, "C++")  # 索引超過範圍會加到最前面
print(L)  # ['C++', 'Hello', 'Python', 'Java', 'World']


# remove：移除 List 中指定的元素
# 電腦會從左到右尋找第一個符合的元素並移除，只移除一次
L = ["Hello", "World", "Python"]
L.remove("World")  # 移除 "World"
print(L)  # ['Hello', 'Python']
# pop：移除並回傳 List 中的元素
L = ["Hello", "World", "Python"]
# 不給索引時，pop() 會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)  # ['Hello', 'World']
s = L.pop(1)  # 如果用變數去存，可以取得被移除的元素
print(s)  # World
print(L)  # ['Hello'
# 如果輸入的 index 超過範圍，會產生錯誤訊息
# 負數索引也可以使用
L = ["Hello", "World", "Python"]
L.pop(-2)  # 移除倒數第二個元素
print(L)  # ['Hello', 'Python']
# 負數索引超過範圍也會產生錯誤訊息

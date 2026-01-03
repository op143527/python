# index:尋找指定元素在List中第一次出現的位置
# 如果元素不存在會產生錯誤,建議先檢查元素是否存在於List中
L = ["Hello", "World", "Python", "World"]
index1 = L.index("World")  # 找到第一個 World 的位置
print(index1)  # 1


# count:計算指定元素在List中出現的次數
L = ["Hello", "World", "Python", "World"]
print(L.count("World"))  # "world" 出現的次數是 2

# sort:將List中的元素依照指定的順序排列 預設是由小到大排序
L = [5, 2, 9, 1, 5, 6]
L.sort()  # 由小到大排序
print(L)  # [1, 2, 5, 5, 6, 9]


# sort(reverse=True):將List中的元素由大到小排序(降續排列)
# 由大到小排序可以用reverse參數改成由大到小排序
L.sort(reverse=True)
print(L)  # [9, 6, 5, 5, 2, 1]

# 這不是排序！只是把第一個變最後一個，最後一個變第一個
L = [1, 3, 2, 4, 5]
L.reverse()
print(L)

# List 和字串有很多相似的操作方式
# 我們可以像操作字串一樣來處理 List

# 合併兩個 List：使用 + 運算子將兩個 List 連接在一起
# 會產生一個全新的 List，原本的 List 不會被改變
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2  # 把 L1 和 L2 合併成一個新的 List
print(L3)

# 複製 List 中的內容：使用 * 運算子將 List 內容重複多次
# 這在需要建立重複資料時很有用
L = [1, 2, 3]
L = L * 3  # 將 List 的內容重複 3 次
print(L)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 不同型態之間的轉換技巧
print(range(10))  # range 物件本身看不到具體內容,只是一個範圍描述
print(list(range(10)))  # 用 list() 轉換成 List 後就可以看到內容
print(list("Hello"))  # 把字串轉換成 List,每個字元變成 List 的一個元素

# split:將一個完整的字串按指定照指定的分割符號切割成多個部分
# 這是處理文資料時非常常用的方法
s = "Hello World"
L = s.split(" ")  # 用空格分割字串
print(L)  # ['Hello', 'World']
calendar = "2024/06/15"
L = calendar.split("/")  # 用斜線分割字串
print(L)  # ['2024', '06', '15']

# join:將List中的多個字串元素合併成一個完整的字串
# 可以指定要用什麼符號來連接這些元素
L = ["Hello", "World"]
s = " ".join(L)  # 用空格把 List 元素合併成一個字串
print(s)  # "Hello World"


# 字典(dictionary):用來儲存[key:value]配對資料的資料結構
# 字典很適合用來表示有對應關係的資料,像商品和價格對應

# 建立一個字典,用大誇號{},key和value用冒號:分隔
f = {"apple": 25, "banana": 30, "orange": 20}
print(f)  # {'apple': 25, 'banana': 30, 'orange': 20}

# 從字典中取得特定key對應的value
# 如果key不存在會產生錯誤keyError錯誤
d = {"apple": 25, "banana": 30, "orange": 20}
print(d["ban"])
# print(d["ban"])#  # KeyError: 'ban' 錯誤

# 遍歷字典:有多種有種方式可以遍歷字典中的資料
d = {"apple": 25, "banana": 30, "orange": 20}
# 方法1:遍歷所有的key
for key in d:
    print(key)  # 印出key名稱
    print(d[key])  # 印出key對應的value

# 方法2:明確使用d.keys()取得所有key
for k in d.keys():
    print(k)  # 印出key名稱
    print(d[k])  # 印出key對應的value

# 方法3:用values()取得所有value
for v in d.values():
    print(v)  # 印出value ,but無法取得key
# 方法4:用items()同時取得key和value
for k, v in d.items():
    print(f"{k}:{v}")  # 同時印出key和value

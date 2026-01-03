import random  # 這是引入隨機模組

# random.randrange 設定範圍的方式跟 range 一樣
# random.randrange 的功能是隨機取得ㄧ個數字
print(random.randrange(10))  # 取得0~9的隨機整數
print(random.randrange(1, 10))  # 取得1~9的隨機整數
print(random.randrange(1, 10, 2))  # 從[1,3,5,7,9]中取得隨機整數

# random.randint 設定範圍的方式必須有開始跟結束，且含最後ㄧ個數字
# 不能跳數字抽籤
print(random.randint(1, 10))  # 取得1~10的隨機整數

# List 清單（List)
# List 可以存入很多資料,每筆料用`,`區隔
# List 可以存入不同型態的資料
# List最外層用`[]`包住
a = [1, 2, 3, 4, 5]  # 數字
print(a)
# 不同型態混合
l = [1, 2, 3, 4, 5, "hello", ["World", 6]]
print(l)

# List 取值
# List 取值方式跟字串一樣,用`[]`取值
# List 也可以用負數取值,負數是從最後面開始算起
# list 取值方式跟字串一樣，也可以用`[:]`取值
# List當中資料的編號（index）是從0開始算起
# 設定範圍的方式跟range很像,不含最後一個數字
print(a[0])  # 取得第一個資料
print(a[4])  # 取得第五個資料
print(a[-1])  # 取得最後一個資料
print(a[-2])  # 取得倒數第二個資料
print(a[1:4])  # 取得第2個到第4個資料
print(a[:3])  # 取得第1個到第3個資料
print(a[2:])  # 取得第3個到最後一個資料
print(a[:])  # 取得所有資料
print(l[5])  # 取得第6個資料
print(l[6])  # 取得第7個資料
print(l[6][0])  # 取得第7個資料當中的第一個
print(l[6][1])  # 取得第7個資料當中的第二個
print(l[6][0][2])  # 取得第7個資料當中的第一個的第三個字元
print(l[6][0][:2])  # 取得第7個資料當中的第一個的前兩個字元
print(l[6][0][2:])  # 取得第7個資料當中的第一個的第三個字元之後的所有字元
print(l[6][0][1:4])  # 取得第7個資料當中的第一個的第二個到第四個字元
print(l[6][0][-1])  # 取得第7個資料當中的第一個的最後一個字元
print(l[6][0][-3:])  # 取得第7個資料當中的第一個的最後三個字元取直的
print(l[6][0][:-2])  # 取得第7個資料當中的第一個的除了最後兩個字元之外的所有字元


# list len 列表長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得 List 長度，也就是 List 當中有幾筆資料

# 務必不要跟 index 混淆，index 是資料的編號，len 是資料的數量

# len 可以搭配 for 迴圈使用來取的 List 當中的所有資料
for i in range(len(L)):  # 這邊的 i 是 index
    print(L[i])

for i in L:  # 這邊的 i 是資料
    print(i)

# 要使用哪一種方式讀取 List 當中的資料，要看使用的情境當中會不會需要 index
# 可愛版
# 🍭 List 的長度（有幾個小朋友？）
L = [1, 2, 3, 4, 5]
print(len(L))  # 😲 哇～List 裡有幾筆資料呢？

# ❗小提醒：
# index（索引）＝ 第幾號
# len（長度）＝ 有幾個
# 兩個不一樣，請不要搞混唷！(๑•̀ㅂ•́)و✧

# 🐥 用 len 配合 for 迴圈，一個一個把資料抓出來
# 這個 for 取出來的 i 是「索引編號」
for i in range(len(L)):
    print("第", i, "號的小朋友是：", L[i], "🌟")

# 🐰 這個寫法就更簡單了！
# i 直接是資料，不是索引～
for i in L:
    print("我找到一個資料：", i, "💖")

# 🌈 什麼時候要用哪一種？
# ➤ 如果你需要知道「第幾個」→ 用 range(len(L))
# ➤ 如果只是要跑過所有資料 → for i in L 超方便！

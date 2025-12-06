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
# 更可愛版

import time

# 顏色設定 🎨
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


# 小動畫函式 ✨
def cute_print(text, delay=0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


# 🐰 小兔子出來介紹
cute_print(MAGENTA + "🐰：嗨嗨～今天我要教你什麼是 List 的長度唷！💖" + RESET)

# 🍬 List 的長度
L = [1, 2, 3, 4, 5]
cute_print(CYAN + "🌟 小兔子偷偷數一數… List 裡有 " + str(len(L)) + " 個孩子！" + RESET)

time.sleep(0.5)

# ❗ index vs len 小提醒
cute_print(
    YELLOW + "🐥：注意唷！index 是位置編號～ len 是資料數量！完全不一樣！" + RESET
)

time.sleep(0.5)

# 🐱 用 range(len) 方式取資料
cute_print(GREEN + "🐱：現在讓我一個一個找出每個孩子吧！(用 index～)" + RESET)

for i in range(len(L)):
    cute_print(f"   ➤ 第 {i} 號的小朋友是：{L[i]} 🍪")

time.sleep(0.5)

# 🐻 直接讀資料
cute_print(RED + "🐻：換我！我直接把每個資料抱出來～不看編號～" + RESET)

for i in L:
    cute_print(f"   🧸 抱到一個資料：{i} 💛")

time.sleep(0.5)

cute_print(MAGENTA + "🌈：什麼時候用哪一種？" + RESET)
cute_print("   💡 想知道第幾個 → 用 range(len(L))")
cute_print("   💡 只要資料本身 → for i in L 最省力！✨")
# 可愛版結束

import time

# 顏色 🎨
R = "\033[91m"  # 紅
G = "\033[92m"  # 綠
Y = "\033[93m"  # 黃
B = "\033[94m"  # 藍
M = "\033[95m"  # 紫
C = "\033[96m"  # 青
RESET = "\033[0m"


# 小動畫函式 ✨
def cute(text, delay=0.02):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


# 🐰🐥🐉🦖 角色登場！
cute(M + "🐰 兔兔：哈囉！今天我們一起來玩 List～" + RESET)
cute(Y + "🐥 小雞：我會幫忙數數！" + RESET)
cute(C + "🐉 小龍：我負責噴彩虹火～🌈🔥" + RESET)
cute(G + "🦖 小恐龍：我…我只負責可愛！(˶ᵔ ᵕ ᵔ˶)" + RESET)

L = [1, 2, 3, 4, 5]

cute(B + f"\n🌟 兔兔：我們的清單裡總共有 {len(L)} 個寶物！✨" + RESET)

# index 教學
cute(Y + "\n🐥 小雞：記得！index＝第幾個，len＝有幾個！不要搞混唷！" + RESET)

# 用 index 方式讀
cute(C + "\n🐉 小龍：我用編號一個個找出來～ (range(len))" + RESET)
for i in range(len(L)):
    cute(f"   ➤ 第 {i} 號寶物：{L[i]} 🎁")

# 直接讀資料
cute(G + "\n🦖 小恐龍：我直接把寶物抱出來～不看編號～" + RESET)
for item in L:
    cute(f"   🦖 抱到：{item} 💚")

cute(
    M
    + "\n💡 什麼時候用哪一種？\n"
    + "   🐥 要知道第幾項 → range(len())\n"
    + "   🐰 只要跑內容 → for i in L"
    + RESET
)

import time
import random
import os

chars = ["🐰", "🐥", "🐉", "🦖"]
L = [1, 2, 3, 4, 5]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def show_items():
    clear()
    for item in L:
        c = random.choice(chars)
        print(f"{c} 找到寶物：{item} ✨")
        time.sleep(0.3)
    input("\n按 Enter 回主選單")


def show_index():
    clear()
    for i in range(len(L)):
        c = random.choice(chars)
        print(f"{c} 第 {i} 號寶物：{L[i]} 🎁")
        time.sleep(0.3)
    input("\n按 Enter 回主選單")

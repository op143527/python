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

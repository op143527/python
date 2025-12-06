
# 主程式
while True:
    clear()
    print("🎮 可愛 List 冒險遊戲 🐰🐥🐉🦖")
    print("1️⃣ 直接讀資料")
    print("2️⃣ 用 index 讀")
    print("0️⃣ 離開遊戲")
    cmd = input("請選擇：")

    if cmd == "1":
        show_items()
    elif cmd == "2":
        show_index()
    elif cmd == "0":
        print("👋 小動物們跟你說再見～")
        break
    else:
        print("❓ 這個選項不存在唷！")
        time.sleep(1)
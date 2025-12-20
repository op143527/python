# 🛒 我的超市購物清單
shopping = []

while True:
    print("\n📋 目前清單：", shopping)
    print("1️⃣ 新增東西")
    print("2️⃣ 修改東西")
    print("3️⃣ 刪除東西")
    print("4️⃣ 離開")

    choice = input("請選 1~4：")

    # 1️⃣ 新增東西
    if choice == "1":
        item = input("要買什麼呢？🧺 ")
        shopping.append(item)

    # 2️⃣ 修改東西（有註解）
    elif choice == "2":
        # 輸入要修改的「位置編號」
        index = int(input("要改第幾個？👀 "))

        # 如果編號在清單範圍內
        if 0 <= index < len(shopping):
            # 輸入新的東西名稱
            new_item = input("改成什麼呢？✨ ")
            # 用新內容換掉舊的
            shopping[index] = new_item
        else:
            print("❌ 這個編號不存在喔")

    # 3️⃣ 刪除東西
    elif choice == "3":
        index = int(input("要刪第幾個？🗑️ "))
        if 0 <= index < len(shopping):
            shopping.pop(index)
        else:
            print("❌ 這個編號不存在喔")

    # 4️⃣ 離開
    elif choice == "4":
        print("👋 掰掰～回家囉！")
        break

    else:
        print("❌ 請輸入 1~4")

# 🛒🐰 我的超市購物清單小管家
# 幫媽媽記住要買什麼～不會忘記 ✨

shopping_list = []


def show_list():
    print("\n📋✨ 目前的購物清單：")
    if not shopping_list:
        print("（清單空空的，快加點東西吧～）")
    else:
        for i, item in enumerate(shopping_list):
            print(f"🍎 {i}. {item}")
    print("💛" * 20)


while True:
    show_list()

    print("請選擇你要做的事 🌈")
    print("1️⃣ 新增東西")
    print("2️⃣ 修改東西")
    print("3️⃣ 刪除東西")
    print("4️⃣ 回家休息 🏠")

    choice = input("👉 輸入 1～4：")

    # 🌟 1. 新增東西
    if choice == "1":
        print("\n➕ 要怎麼加呢？")
        print("1. 加在最後 🍭")
        print("2. 插在指定位置 🍰")
        add_choice = input("請選 1 或 2：")

        if add_choice == "1":
            item = input("請輸入要買的東西：")
            shopping_list.append(item)

        elif add_choice == "2":
            item = input("請輸入要買的東西：")
            index = int(input("請輸入要放的位置："))
            shopping_list.insert(index, item)

    # 🌟 2. 修改東西（📌 重點註解版）
    elif choice == "2":
        # 請使用者輸入「要修改的編號」
        index = int(input("✏️ 請輸入要修改的編號："))

        # 檢查編號有沒有在清單範圍內
        if 0 <= index < len(shopping_list):
            # 如果編號正確，就輸入新的物品名稱
            new_item = input("✨ 請輸入新的內容：")

            # 用新內容取代原本清單中的項目
            shopping_list[index] = new_item
            print("🎉 修改完成囉！")
        else:
            # 如果輸入錯誤的編號
            print("❌ 這個編號不存在喔～")

    # 🌟 3. 刪除東西
    elif choice == "3":
        print("\n🗑️ 要怎麼刪呢？")
        print("1. 用名稱刪除 ❌")
        print("2. 用位置刪除 📍")
        del_choice = input("請選 1 或 2：")

        if del_choice == "1":
            item = input("請輸入要刪除的東西名稱：")
            if item in shopping_list:
                shopping_list.remove(item)
                print("👋 已刪除～")
            else:
                print("❌ 清單裡沒有這個東西")

        elif del_choice == "2":
            index = int(input("請輸入要刪除的位置："))
            if 0 <= index < len(shopping_list):
                shopping_list.pop(index)
                print("🧹 刪掉囉！")
            else:
                print("❌ 編號錯誤")

    # 🌟 4. 離開程式
    elif choice == "4":
        print("🏠 不想逛了～回家吧！掰掰 👋")
        break

    else:
        print("❌ 請輸入正確的選項喔～")

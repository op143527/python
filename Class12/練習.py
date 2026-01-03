# 水果店價格查詢系統
# 使用 dictionary 來儲存水果名稱與價格

# 一開始先準備一個空的字典
fruits = {}

while True:
    print(" 水果店價格查詢系統 ")
    print("1. 新增水果價格")
    print("2. 修改水果價格")
    print("3. 刪除水果")
    print("4. 離開系統")
# 目前水果價格
fruits = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print("目前水果價格：", fruits)
# 讓使用者輸入選項
choice = input("請輸入選項 (1~4)")

# ---------- 功能 1：新增水果 ----------
if choice == "1":
    name = input("請輸入水果名稱：")
    price = int(input("請輸入水果價格："))

    # 檢查水果是否已存在
    if name in fruits:
        print("⚠️ 這個水果已經存在，請使用修改功能")
    else:
        fruits[name] = price
        print(f"✅ 已新增 {name}，價格是 {price} 元")

# ---------- 功能 2：修改水果 ----------
elif choice == "2":
    name = input("請輸入要修改的水果名稱：")

    if name in fruits:
        price = int(input("請輸入新的價格："))
        fruits[name] = price
        print(f"✏️ {name} 的價格已修改為 {price} 元")
    else:
        print("❌ 找不到這個水果")

# ---------- 功能 3：刪除水果 ----------
elif choice == "3":
    name = input("請輸入要刪除的水果名稱：")

    if name in fruits:
        fruits.pop(name)
        print(f"🗑️ 已刪除 {name}")
    else:
        print("❌ 找不到這個水果")

# ---------- 功能 4：離開系統 ----------
elif choice == "4":
    print("👋 謝謝使用，再見！")


else:
    print("⚠️ 請輸入正確的選項")

try:
    m = int1(input("請輸入成績:"))
    A = 90
    B = 80
    C = 70
    D = 60
    E = 59
    if m >= A:
        print("你的成績等級為A")
    elif m >= B:
        print("你的成績等級為B")
    elif m >= C:
        print("你的成績等級為C")
    elif m >= D:
        print("你的成績等級為D")
    elif m <= E:
        print("你的成績等級為E")
except:
    print("輸入錯誤!")

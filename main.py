import subprocess
import sys

def clear_screen():
    print("\n" * 50)

def run_script(script_path):
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError:
        print(f"\n執行 {script_path} 時發生錯誤")
    except KeyboardInterrupt:
        print("\n\n程式被中斷")
    input("\n按 Enter 鍵返回主選單...")

def main():
    while True:
        clear_screen()
        print("=" * 50)
        print("Python 學習專案 - 練習選單")
        print("=" * 50)
        print("\n第一課 - 基礎概念:")
        print("  1. 註解、資料型態、變數、運算子")
        print("\n第二課 - 函式與輸入:")
        print("  2. 字串格式化、內建函式、使用者輸入")
        print("\n第三課 - 錯誤處理與條件判斷:")
        print("  3. Try-Except、比較運算子、If-Elif-Else")
        print("  4. 作業 - 華氏轉攝氏溫度")
        print("\n第四課 - 實作練習:")
        print("  5. 成績等級判斷")
        print("  6. 奇偶數判斷")
        print("\n0. 離開")
        print("=" * 50)
        
        choice = input("\n請選擇要執行的練習 (0-6): ").strip()
        
        if choice == "0":
            print("\n感謝使用！再見！")
            break
        elif choice == "1":
            run_script("class1/prj01.py")
        elif choice == "2":
            run_script("class2/prj02.py")
        elif choice == "3":
            run_script("class3/prj03.py")
        elif choice == "4":
            run_script("class3/homework.py")
        elif choice == "5":
            run_script("class4/prj04.py")
        elif choice == "6":
            run_script("class4/prj04-1.py")
        else:
            print("\n無效的選擇，請輸入 0-6")
            input("\n按 Enter 鍵繼續...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程式結束")
        sys.exit(0)

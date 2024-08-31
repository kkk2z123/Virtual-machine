import tkinter as tk

def main():
    root = tk.Tk()
    root.title("電卓")

    # 簡単な電卓GUI
    label = tk.Label(root, text="電卓アプリ")
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

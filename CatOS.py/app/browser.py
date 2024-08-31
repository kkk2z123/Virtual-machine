import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("ブラウザ")

    messagebox.showinfo("ブラウザ", "ブラウザアプリを起動中...")

    root.mainloop()

if __name__ == "__main__":
    main()

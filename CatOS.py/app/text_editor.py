import tkinter as tk
from tkinter import scrolledtext

def main():
    root = tk.Tk()
    root.title("テキストエディタ")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    text_area.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

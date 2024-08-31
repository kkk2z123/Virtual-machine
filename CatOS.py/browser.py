import tkinter as tk
from tkinterweb import HtmlFrame

def open_browser():
    browser_window = tk.Toplevel()
    browser_window.title("ブラウザ")
    browser_window.geometry("800x600")

    frame = HtmlFrame(browser_window)
    frame.pack(expand=True, fill='both')

    # 初期URLを設定
    frame.load_website("https://www.google.com")


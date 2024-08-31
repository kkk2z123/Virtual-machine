import tkinter as tk
from tkinter import filedialog

def open_text_editor():
    editor_window = tk.Toplevel()
    editor_window.title("テキストエディタ")
    editor_window.geometry("600x400")

    text_area = tk.Text(editor_window)
    text_area.pack(expand=True, fill='both')

    save_button = tk.Button(editor_window, text="保存", command=lambda: save_file(text_area))
    save_button.pack(side='left')

    load_button = tk.Button(editor_window, text="読み込み", command=lambda: load_file(text_area))
    load_button.pack(side='left')

    exit_button = tk.Button(editor_window, text="終了", command=editor_window.destroy)
    exit_button.pack(side='right')

def save_file(text_area):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_area.get("1.0", tk.END))

def load_file(text_area):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"),
                                                     ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", file.read())

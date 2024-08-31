import tkinter as tk
from tkinter import PhotoImage
from text_editor import open_text_editor
from file_operations import create_folder, list_files
from calculator import run_calculator
from shell import run_shell
from browser import open_browser

class VirtualMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("仮想マシン")
        self.master.geometry("800x600")

        self.label = tk.Label(master, text="仮想デスクトップ", font=("Helvetica", 24))
        self.label.pack(pady=20)

        # アイコンを配置するフレーム
        self.icon_frame = tk.Frame(master)
        self.icon_frame.pack(pady=20)

        # 各アプリのアイコンとラベルを追加
        self.add_app_icon("テキストエディタ", "icons/text_editor_icon.png", open_text_editor)
        self.add_app_icon("ファイル操作", "icons/file_operations_icon.png", self.file_operations)
        self.add_app_icon("電卓", "icons/calculator_icon.png", run_calculator)
        self.add_app_icon("シェル", "icons/shell_icon.png", run_shell)
        self.add_app_icon("ブラウザ", "icons/browser_icon.png", open_browser)

        self.exit_button = tk.Button(master, text="終了", command=master.quit)
        self.exit_button.pack(pady=10)

    def add_app_icon(self, app_name, icon_path, command):
        try:
            icon = PhotoImage(file=icon_path)
            button = tk.Button(self.icon_frame, image=icon, command=command)
            button.image = icon  # 画像を保持しないと表示されない
            button.pack(side='left', padx=10)
            
            label = tk.Label(self.icon_frame, text=app_name)
            label.pack(side='left', padx=10)
        except Exception as e:
            print(f"アイコン '{app_name}' の読み込みエラー: {e}")

    def file_operations(self):
        # ファイル操作の例: 新しいフォルダを作成し、ファイル一覧を表示
        create_folder("NewFolder")
        list_files()

if __name__ == "__main__":
    root = tk.Tk()
    vm = VirtualMachine(root)
    root.mainloop()

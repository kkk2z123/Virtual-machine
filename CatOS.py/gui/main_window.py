import tkinter as tk
from gui.app_icon import AppIcon

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("仮想デスクトップOS")
        self.root.geometry("800x600")

        # アプリのアイコンを設定
        icons = [
            {"icon": "icon/file_manager_icon.png", "command": self.launch_file_manager},
            {"icon": "icon/calculator_icon.png", "command": self.launch_calculator},
            {"icon": "icon/text_editor_icon.png", "command": self.launch_text_editor},
            {"icon": "icon/browser_icon.png", "command": self.launch_browser},
            {"icon": "icon/image_viewer_icon.png", "command": self.launch_image_viewer},
            {"icon": "icon/basic_interpreter_icon.png", "command": self.launch_basic_interpreter},
            {"icon": "icon/shell_icon.png", "command": self.launch_shell},
        ]

        for i, app in enumerate(icons):
            app_icon = AppIcon(self.root, app["icon"], app["command"])
            app_icon.button.grid(row=i//4, column=i%4, padx=10, pady=10)

    def run(self):
        self.root.mainloop()

    # 各アプリの起動メソッド
    def launch_file_manager(self):
        exec(open("app/file_manager.py").read())

    def launch_calculator(self):
        exec(open("app/calculator.py").read())

    def launch_text_editor(self):
        exec(open("app/text_editor.py").read())

    def launch_browser(self):
        exec(open("app/browser.py").read())

    def launch_image_viewer(self):
        exec(open("app/image_viewer.py").read())

    def launch_basic_interpreter(self):
        exec(open("app/basic_interpreter.py").read())

    def launch_shell(self):
        exec(open("app/shell.py").read())

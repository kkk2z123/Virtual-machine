import tkinter as tk
from PIL import Image, ImageTk

class AppIcon:
    def __init__(self, root, icon_path, command):
        self.icon_image = Image.open(icon_path)
        self.icon_image = self.icon_image.resize((64, 64))  # アイコンのサイズを調整
        self.icon_photo = ImageTk.PhotoImage(self.icon_image)

        self.button = tk.Button(root, image=self.icon_photo, command=command)
        self.button.image = self.icon_photo  # 画像参照を保持

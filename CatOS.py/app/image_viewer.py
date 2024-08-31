import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.title("画像ビューア")

    def open_image():
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((400, 400))  # 画像サイズを変更
            img_tk = ImageTk.PhotoImage(img)
            label.config(image=img_tk)
            label.image = img_tk

    label = tk.Label(root)
    label.pack()

    btn_open = tk.Button(root, text="画像を開く", command=open_image)
    btn_open.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk

def run_calculator():
    calculator_window = tk.Toplevel()
    calculator_window.title("電卓")
    calculator_window.geometry("300x400")

    # 電卓のGUIを構築するコードはここに追加
    display = tk.Entry(calculator_window, font=("Arial", 24), borderwidth=2, relief="solid")
    display.grid(row=0, column=0, columnspan=4)

    # ここに電卓のボタンと機能を追加します

    def click_button(value):
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current_text + value)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row = 1
    col = 0
    for button in buttons:
        tk.Button(calculator_window, text=button, width=5, height=2,
                  command=lambda b=button: click_button(b)).grid(row=row, column=col)
        col += 1
        if col > 3:
            col = 0
            row += 1

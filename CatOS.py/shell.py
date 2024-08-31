import os

def run_shell():
    shell_window = tk.Toplevel()
    shell_window.title("シェル")
    shell_window.geometry("600x400")

    # シェルのコマンド入力と出力を表示するコードはここに追加

    def execute_command():
        command = entry.get()
        # コマンドを実行する処理を追加します
        print(f"実行コマンド: {command}")

    entry = tk.Entry(shell_window, font=("Arial", 14))
    entry.pack(pady=10)

    execute_button = tk.Button(shell_window, text="実行", command=execute_command)
    execute_button.pack(pady=10)

import os

def create_folder(folder_name):
    """指定された名前で新しいフォルダを作成します。"""
    try:
        os.mkdir(folder_name)
        print(f"フォルダ '{folder_name}' を作成しました。")
    except FileExistsError:
        print(f"フォルダ '{folder_name}' はすでに存在します。")
    except Exception as e:
        print(f"フォルダ作成中にエラーが発生しました: {e}")

def list_files():
    """現在のディレクトリ内のファイルとフォルダを表示します。"""
    try:
        files = os.listdir()
        print("ディレクトリ内のファイルとフォルダ:")
        for file in files:
            print(file)
    except FileNotFoundError:
        print("ディレクトリが見つかりません。")
    except Exception as e:
        print(f"ファイル一覧表示中にエラーが発生しました: {e}")

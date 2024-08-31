from quart import Quart, render_template, request, send_from_directory
import os

app = Quart(__name__)

# ホームページ
@app.route('/')
async def home():
    return await render_template('index.html')

# テキストエディタページ
@app.route('/editor')
async def editor():
    return await render_template('editor.html')

# ファイルの保存
@app.route('/save_file', methods=['POST'])
async def save_file():
    file_content = await request.form['content']
    file_name = 'saved_file.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(file_content)
    return 'File saved successfully!'

# ファイルの読み込み
@app.route('/load_file')
async def load_file():
    file_name = 'saved_file.txt'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    return 'File not found!'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!doctype html>
    <title>Simple Web App</title>
    <h1>Welcome to the Web App</h1>
    <p>This is a simple Flask application running in Codespaces.</p>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

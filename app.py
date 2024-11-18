import subprocess

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        # Ejecuta el script de Python con el texto como argumento
        subprocess.run(['python', 'script.py', text])
        return render_template('index.html', text=text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
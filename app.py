from flask import Flask

import script

app = Flask(__name__)

@app.route('/')
def hello():
    return script.get_hello_world()  # Call a function from your script

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
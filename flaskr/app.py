from flask import Flask

app = Flask(__name__)

@app.route('/personal',  methods=['GET'])
def get_personal():
    return 'Hello, World!'

@app.route('/experience',  methods=['GET'])
def get_experience():
    return 'Hello, World!'

@app.route('/education',  methods=['GET'])
def get_education():
    return 'Hello, World!'

@app.cli.command('print')
def print_command():
    print('Hello world')
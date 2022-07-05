from flask import Flask
from flaskr import data
from flaskr.utils import dict_print
app = Flask(__name__)

@app.route('/personal',  methods=['GET'])
def get_personal():
    return data.fetch_personal()

@app.route('/experience',  methods=['GET'])
def get_experience():
    return data.fetch_experience()

@app.route('/education',  methods=['GET'])
def get_education():
    return data.fetch_education()

@app.cli.command('print')
def print_command():
    print("My personal data:")
    dict_print(data.fetch_personal())

    print("My education:")
    dict_print(data.fetch_education())

    print("My experience:")
    dict_print(data.fetch_experience())
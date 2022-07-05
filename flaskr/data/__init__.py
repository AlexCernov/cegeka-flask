import json

def fetch_experience():
    with open('./flaskr/data/cv.json', 'r') as file:
         return json.load(file).get('experience', None)


def fetch_personal():
    with open('./flaskr/data/cv.json', 'r') as file:
         return json.load(file).get('personal', None)


def fetch_education():
    with open('./flaskr/data/cv.json', 'r') as file:
         return json.load(file).get('education', None)
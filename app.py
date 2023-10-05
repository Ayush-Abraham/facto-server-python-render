from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def find_facts():
    request_data = request.get_json()
    date = request_data['date']
    month = request_data['month']

    # response = requests.get('https://today.zenquotes.io/api/'+month+'/'+date)

    # return jsonify(response.json())

    return month+'/'+date

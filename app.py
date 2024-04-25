import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! Blessed by bald Jesus <3'


@app.route('/postendpoint', methods=['POST'])
def handle_post():
    request_text = request.json.get('requestText', 'Kein Text gesendet')
    community_id = 1

    offers = requests.get(f'https://neighbourly.lanzeray.ch/api/sample-offers/{community_id}')

    response_data = {
        'offers': offers,
        'requested_service': request_text
    }

    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Spezifiziert den Port explizit

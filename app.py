import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Blessed by bald Jesus <3'

@app.route('/postendpoint', methods=['POST'])
def handle_post():
    # Nehmen Sie den Wert von "requestText" aus der POST-Anfrage
    request_text = request.json.get('requestText', 'Kein Text gesendet')

    # Bereiten Sie die Daten für die Weiterleitung vor
    data_to_send = {
        "requestText": request_text
    }

    # Senden Sie eine POST-Anfrage an die externe URL
    response_from_external_api = requests.post('https://neighbourly.lanzeray.ch/api/testRequest/1', json=data_to_send)

    # Hier können Sie den Statuscode und die Antwort von der externen API überprüfen
    # Zum Beispiel: response_from_external_api.json() oder response_from_external_api.status_code

    # Stellen Sie die Antwort zusammen
    response_data = {
        "originalRequest": request_text,
        "foundOffer": "Dies ist ein Beispielangebot, basierend auf Ihrem Request.",
        # Optional: Fügen Sie Informationen aus der Antwort der externen API hinzu
        "externalApiResponse": response_from_external_api.json()
    }

    # Senden Sie das Datenobjekt als JSON-Antwort zurück
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Spezifiziert den Port explizit


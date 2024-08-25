from flask import Flask, request, jsonify
from astroapi.services.natal_service import generate_natal_chart

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    natal_chart = generate_natal_chart(data)
    return jsonify(natal_chart), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
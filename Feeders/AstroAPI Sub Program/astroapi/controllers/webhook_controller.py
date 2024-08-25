from flask import Flask, request, jsonify, render_template
from astroapi.services.natal_service import generate_natal_chart
from astroapi.services.transit_service import pull_transit_data

app = Flask(__name__)

@app.route('/generate-natal', methods=['POST'])
def generate_natal():
    # Extract birth data from the form submission
    birth_data = {
        "date": request.form['date'],
        "time": request.form['time'],
        "location": request.form['location']
    }
    # Generate the natal chart based on the provided data
    natal_chart = generate_natal_chart(birth_data)
    # Return the natal chart as a JSON response
    return jsonify(natal_chart), 200

@app.route('/pull-transit', methods=['POST'])
def pull_transit():
    # Extract birth data from the form submission
    birth_data = {
        "date": request.form['date'],
        "time": request.form['time'],
        "location": request.form['location']
    }
    # Pull the transit data based on the provided birth data
    transit_data = pull_transit_data(birth_data)
    # Return the transit data as a JSON response
    return jsonify(transit_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
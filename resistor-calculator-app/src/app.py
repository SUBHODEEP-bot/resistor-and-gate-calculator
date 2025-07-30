
from flask import Flask, render_template, request, jsonify
from utils.resistor_calculator import calculate_resistor_value
from utils.gate_calculator import calculate_logic_gate




app = Flask(__name__)

COLOR_CODES = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
}
MULTIPLIERS = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
    "green": 100000, "blue": 1000000, "violet": 10000000, "gray": 100000000, "white": 1000000000
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gates', methods=['POST'])
def gates():
    data=request.get_json()
    input1=data['input1']
    input2=data['input2']
    gate_type=data['gate_type']
    result = calculate_logic_gate(gate_type, input1, input2)
    return render_template('gates.html', result=result)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    band1 = data['color1']
    band2 = data['color2']
    multiplier = data['multiplier']
    tolerance = data.get('tolerance', 'brown')
    # Use the utility function for calculation and formatting
    result = calculate_resistor_value(band1, band2, multiplier, tolerance)
    # Extract resistance value for display (for SVG and JS)
    if result.startswith('Resistance:'):
        value = result.split(',')[0].replace('Resistance:','').strip().replace(' Ohms','')
    else:
        value = result
    return jsonify({'value': value})

if __name__ == '__main__':

    app.run(debug=True, port=5050)
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/duasDimensoes')
def gerar_duas():
    return render_template('2d.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  
    value = int(data['value'])  
    calculated_values = [value * i for i in range(1, 6)]
    return jsonify({'calculated_values': calculated_values})

if __name__ == '__main__':
    app.run(debug=True)

from flask import *
from plotter import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

chance = 0

@app.route('/simulate/<int:copies>/<int:pulls>', methods=['GET'])
def simulate(copies, pulls) -> Response:
    try:
        global chance
        chance = createPlot(copies, pulls)
        return send_file('plot.png', mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/simulate/getchance', methods=['GET'])
def getchance() -> Response:
    print(chance)
    return jsonify({"chance": chance})

if __name__ == '__main__':
    app.run(debug=True)

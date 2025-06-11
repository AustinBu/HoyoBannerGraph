from flask import *
from plotter import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/simulate/<int:copies>/<int:pulls>', methods=['GET'])
def simulate(copies, pulls) -> Response:
    try:
        chance = createPlot(copies, pulls)
        return send_file('plot.png', mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

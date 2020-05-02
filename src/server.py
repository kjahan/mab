from argparse import ArgumentParser

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import jsonify

from src.models.epsilon_greedy import EpsilonGreedy

import logging
logging.getLogger('flask_cors').level = logging.DEBUG
logging.getLogger('fbprophet').setLevel(logging.ERROR)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1/start')
def start():
    model.initialize(int(request.args.get('armsnumber')))
    return jsonify({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/api/v1/predict")
def predict():
    arm_index = model.predict()
    data = {'index': arm_index}
    return jsonify(data)

@app.route('/api/v1/update')
def update():
    arm_index = int(request.args.get('index'))
    payout = int(request.args.get('payout'))
    model.update(arm_index, payout)
    return jsonify({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-o", "--output", dest="MODEL_FOLDER",
        help="specify directory for uploading experiments", required=True)
    model = EpsilonGreedy()   
    args = parser.parse_args()
    app.config['MODEL_FOLDER'] = args.MODEL_FOLDER
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)	#set debug flag to False
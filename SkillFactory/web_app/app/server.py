from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

with open('./models/model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json)
    features = features.reshape(1, 4) 
    num = model.predict(features)

    return jsonify({
        'prediction': num[0]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
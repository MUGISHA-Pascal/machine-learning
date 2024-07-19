from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.DEBUG)

model_path = './irisdataset/model/iris.joblib'

try:
    model = joblib.load(model_path)
except EOFError:
    app.logger.error(f"EOFError: Model file {model_path} may be corrupted or incomplete.")
    model = None
except FileNotFoundError:
    app.logger.error(f"FileNotFoundError: Model file {model_path} not found.")
    model = None
except Exception as e:
    app.logger.error(f"Unexpected error loading model: {e}")
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded correctly'}), 500

    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        data = request.json.get('data')
        if data is None:
            return jsonify({'error': 'Missing "data" key in request'}), 400

        app.logger.debug(f"Received data: {data}")

        input_data = np.array([float(i) for i in data.split(',')]).reshape(1, -1)
        prediction = model.predict(input_data)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)

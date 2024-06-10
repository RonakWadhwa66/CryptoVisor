from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load the trained LSTM model
model = load_model('bitcoin_price_prediction_model.keras')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    data = request.json
    
    # Preprocess the input data as needed (e.g., scaling, formatting)
    # Perform any necessary data transformation
    
    # Make predictions using the loaded model
    # For demonstration purposes, let's assume the input is a single feature vector
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    
    # Serialize the prediction as JSON and return it
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)

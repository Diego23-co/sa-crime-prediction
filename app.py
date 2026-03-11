from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json

app = Flask(__name__)

# Load model and columns
model = pickle.load(open('crime_model.pkl', 'rb'))
with open('model_columns.json', 'r') as f:
    model_columns = json.load(f)

@app.route('/')
def home():
    return "SA Crime Prediction API is running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])
        df = df.reindex(columns=model_columns, fill_value=0)
        prediction = model.predict(df)
        return jsonify({
            'predicted_crime_count': round(prediction[0])
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

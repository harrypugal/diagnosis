from flask import Flask, render_template,request,url_for
import pickle

app = Flask(__name__)

# Load the model

with open('ke.pugal', 'rb') as model_file:
    model = pickle.load(model_file)


@app.route('/')
def home():
    return render_template('model.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if not model:
        return render_template('model.html', prediction_text="Model file not found. Please ensure 'ke.pugal' exists.")
    
    try:
        # Retrieve input features from the form
        features = [float(request.form[key]) for key in ['radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness', 'concavity', 'concave', 'symmetry', 'fractal']]
        
        # Make prediction
        result = model.predict([features])[0]
        prediction_text = f'The prediction is: {result}'
    except ValueError:
        prediction_text = "Invalid input. Please enter numeric values for all fields."
    
    # Return the prediction result
    return render_template('model.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
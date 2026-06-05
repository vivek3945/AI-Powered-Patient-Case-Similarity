import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from joblib import dump, load
import os
from openai import OpenAI

# Initialize OpenAI API
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

app = Flask(__name__)
CORS(app)

# Initialize encoders and model
symptom_encoder = LabelEncoder()
disease_encoder = LabelEncoder()
model = None

def prepare_data():
    """Prepare data from the large dataset"""
    # Read the CSV file
    data = pd.read_csv('patient_case_similarity_dataset_v3.csv')
    
    # Encode symptoms
    all_symptoms = pd.concat([data['Symptom 1'], data['Symptom 2'], 
                              data['Symptom 3'], data['Symptom 4']]).unique()
    symptom_encoder.fit(all_symptoms)
    
    # Encode diseases
    disease_encoder.fit(data['Disease'])
    
    # Prepare features
    X = pd.DataFrame({
        'Symptom_1': symptom_encoder.transform(data['Symptom 1']),
        'Symptom_2': symptom_encoder.transform(data['Symptom 2']),
        'Symptom_3': symptom_encoder.transform(data['Symptom 3']),
        'Symptom_4': symptom_encoder.transform(data['Symptom 4']),
        'Age': data['Age']
    })
    
    y = disease_encoder.transform(data['Disease'])
    
    # Save treatment data
    data[['Disease', 'Medication', 'Cure_Methods', 'Outcome', 'Nearby_Hospital']].to_csv('treatments.csv', index=False)
    
    print(f"Dataset loaded successfully with {len(data)} records")
    print(f"Number of unique diseases: {len(data['Disease'].unique())}")
    print(f"Number of unique symptoms: {len(all_symptoms)}")
    
    return X, y

def initialize_model():
    """Initialize and train the Random Forest model"""
    global model
    
    print("Loading and preparing data...")
    X, y = prepare_data()
    
    print("Splitting dataset into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1  # Use all CPU cores for faster training
    )
    model.fit(X_train, y_train)
    
    # Calculate and print accuracy
    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)
    print(f"Training Accuracy: {train_accuracy:.2f}")
    print(f"Testing Accuracy: {test_accuracy:.2f}")
    
    # Save the model
    dump(model, 'disease_model.joblib')
    print("Model trained and saved successfully")

def get_treatment_info(disease):
    """Get treatment information for a predicted disease"""
    treatments_data = pd.read_csv('treatments.csv')
    treatment = treatments_data[treatments_data['Disease'] == disease].iloc[0]
    return {
        'medication': treatment['Medication'],
        'cureMethods': treatment['Cure_Methods'],
        'outcome': treatment['Outcome'],
        'nearbyHospital': treatment['Nearby_Hospital']
    }

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint for disease prediction"""
    try:
        data = request.json
        symptoms = [
            data['symptom1'].lower(),
            data['symptom2'].lower(),
            data['symptom3'].lower(),
            data['symptom4'].lower()
        ]
        age = int(data['age'])
        
        # Transform symptoms to numerical values
        symptoms_encoded = symptom_encoder.transform(symptoms)
        
        # Create input DataFrame with feature names
        input_data = pd.DataFrame([{
            'Symptom_1': symptoms_encoded[0],
            'Symptom_2': symptoms_encoded[1],
            'Symptom_3': symptoms_encoded[2],
            'Symptom_4': symptoms_encoded[3],
            'Age': age
        }])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        predicted_disease = disease_encoder.inverse_transform([prediction])[0]
        
        # Get treatment information
        treatment_info = get_treatment_info(predicted_disease)
        
        # Get prediction probability
        probabilities = model.predict_proba(input_data)[0]
        max_probability = float(max(probabilities) * 100)
        
        return jsonify({
            'success': True,
            'disease': predicted_disease,
            'confidence': f"{max_probability:.1f}%",
            'treatment': treatment_info
        })
        
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/symptoms', methods=['GET'])
def get_symptoms():
    """Endpoint to get list of all symptoms"""
    try:
        return jsonify({
            'success': True,
            'symptoms': sorted(symptom_encoder.classes_.tolist())
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/chat', methods=['POST'])
def chatbot():
    """Endpoint to interact with OpenAI's chatbot"""
    try:
        # Get the user message from the request
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'No message provided'
            }), 400
        
        # Modify the user message to include a prompt asking for food, fruits, and vegetables
        prompt = f"Based on the user's disease and symptoms: {user_message}, recommend suitable fruits in one line then have a line break ,then vegetables then have a line break, and have a line break and recommend food items. Provide only the names in separate lines, grouped by category, with a line gap compulsory between each category. No explanations are needed."

        # Make OpenAI request with the new library method
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful health assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_tokens=150
        )
        
        # Extract the chatbot's response (note the different response parsing)
        chatbot_response = response.choices[0].message.content
        
        return jsonify({
            'success': True,
            'response': chatbot_response
        })
        
    except Exception as e:
        print(f"Error during chatbot interaction: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    print("Initializing Disease Prediction System...")
    initialize_model()
    print("System ready! Starting server...")
    app.run(debug=True)
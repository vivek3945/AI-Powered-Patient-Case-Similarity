import pandas as pd
import numpy as np
from datetime import datetime

# Set random seed for reproducibility
np.random.seed(42)

# Define common diseases and their associated symptoms
disease_symptoms = {
    'Common Cold': [
        ('runny nose', 'sore throat', 'cough', 'fever'),
        ('congestion', 'sneezing', 'fatigue', 'headache'),
        ('sore throat', 'sneezing', 'congestion', 'body ache')
    ],
    'Type 2 Diabetes': [
        ('frequent urination', 'excessive thirst', 'increased hunger', 'fatigue'),
        ('blurred vision', 'slow healing', 'excessive thirst', 'weight loss'),
        ('fatigue', 'increased hunger', 'dry mouth', 'blurred vision')
    ],
    'Hypertension': [
        ('headache', 'shortness of breath', 'dizziness', 'chest pain'),
        ('irregular heartbeat', 'vision problems', 'fatigue', 'headache'),
        ('nosebleed', 'dizziness', 'chest pain', 'anxiety')
    ],
    'Asthma': [
        ('wheezing', 'chest tightness', 'shortness of breath', 'cough'),
        ('difficulty breathing', 'chest pain', 'fatigue', 'wheezing'),
        ('nighttime cough', 'shortness of breath', 'chest tightness', 'anxiety')
    ],
    'Migraine': [
        ('severe headache', 'nausea', 'sensitivity to light', 'vision changes'),
        ('throbbing pain', 'vomiting', 'dizziness', 'sensitivity to sound'),
        ('aura', 'severe headache', 'nausea', 'fatigue')
    ],
    'Gastritis': [
        ('abdominal pain', 'nausea', 'bloating', 'indigestion'),
        ('loss of appetite', 'vomiting', 'abdominal pain', 'heartburn'),
        ('upper stomach pain', 'nausea', 'bloating', 'early satiety')
    ],
    'Arthritis': [
        ('joint pain', 'stiffness', 'swelling', 'reduced mobility'),
        ('morning stiffness', 'joint tenderness', 'fatigue', 'joint pain'),
        ('decreased range of motion', 'joint swelling', 'stiffness', 'weakness')
    ],
    'Bronchitis': [
        ('persistent cough', 'chest congestion', 'fatigue', 'shortness of breath'),
        ('wheezing', 'chest discomfort', 'mucus production', 'fever'),
        ('dry cough', 'chest pain', 'fatigue', 'sore throat')
    ],
    'COVID-19': [
        ('fever', 'dry cough', 'fatigue', 'loss of taste'),
        ('shortness of breath', 'body aches', 'loss of smell', 'headache'),
        ('sore throat', 'fever', 'chills', 'difficulty breathing')
    ],
    'Dengue Fever': [
        ('high fever', 'severe headache', 'joint pain', 'rash'),
        ('muscle pain', 'fatigue', 'nausea', 'bleeding gums'),
        ('eye pain', 'severe joint pain', 'fever', 'vomiting')
    ],
    'Malaria': [
        ('high fever', 'chills', 'sweating', 'headache'),
        ('fatigue', 'nausea', 'muscle pain', 'vomiting'),
        ('chest pain', 'cough', 'rapid breathing', 'fever')
    ],
    'Typhoid': [
        ('persistent fever', 'headache', 'abdominal pain', 'weakness'),
        ('loss of appetite', 'diarrhea', 'fever', 'fatigue'),
        ('cough', 'muscle pain', 'constipation', 'rash')
    ],
    'Common Cold': [
        ('runny nose', 'sore throat', 'cough', 'mild fever'),
        ('congestion', 'sneezing', 'fatigue', 'headache'),
        ('sore throat', 'sneezing', 'congestion', 'body ache')
    ],
    'Influenza': [
        ('high fever', 'severe body aches', 'fatigue', 'headache'),
        ('dry cough', 'chills', 'nasal congestion', 'sore throat'),
        ('muscle pain', 'fever', 'weakness', 'loss of appetite')
    ],
    'Tuberculosis': [
        ('persistent cough', 'chest pain', 'weight loss', 'night sweats'),
        ('fatigue', 'fever', 'loss of appetite', 'coughing blood'),
        ('weakness', 'chest pain', 'difficulty breathing', 'fever')
    ],
    'Chickenpox': [
        ('fever', 'itchy rash', 'fatigue', 'loss of appetite'),
        ('headache', 'muscle pain', 'blistering rash', 'fever'),
        ('tired feeling', 'rash', 'fever', 'body aches')
    ],
    'Measles': [
        ('high fever', 'cough', 'runny nose', 'red eyes'),
        ('rash', 'tiny white spots', 'fever', 'sore throat'),
        ('fatigue', 'light sensitivity', 'fever', 'muscle pain')
    ],
    'Viral Hepatitis': [
        ('fatigue', 'nausea', 'abdominal pain', 'jaundice'),
        ('loss of appetite', 'fever', 'dark urine', 'joint pain'),
        ('yellowing eyes', 'fever', 'weakness', 'vomiting')
    ],
    'Zika Virus': [
        ('fever', 'rash', 'joint pain', 'red eyes'),
        ('muscle pain', 'headache', 'fatigue', 'conjunctivitis'),
        ('mild fever', 'skin rash', 'fatigue', 'eye pain')
    ],
    'Cholera': [
        ('severe diarrhea', 'vomiting', 'dehydration', 'leg cramps'),
        ('thirst', 'rapid heart rate', 'low blood pressure', 'fatigue'),
        ('watery diarrhea', 'muscle cramps', 'weakness', 'vomiting')
    ],
    'Pneumonia': [
        ('chest pain', 'cough with phlegm', 'fever', 'difficulty breathing'),
        ('fast breathing', 'shortness of breath', 'fatigue', 'fever'),
        ('rapid breathing', 'chest pain', 'confusion', 'fever')
    ],
    'Meningitis': [
        ('severe headache', 'stiff neck', 'fever', 'confusion'),
        ('sensitivity to light', 'nausea', 'fever', 'vomiting'),
        ('drowsiness', 'fever', 'rash', 'seizures')
    ],
    'Food Poisoning': [
        ('nausea', 'vomiting', 'diarrhea', 'abdominal pain'),
        ('fever', 'weakness', 'headache', 'dehydration'),
        ('stomach cramps', 'loss of appetite', 'fatigue', 'diarrhea')
    ]
}

# Define treatment information for each disease
treatments = {
    

    'Common Cold': {
        'medication': 'Acetaminophen, Decongestants, Cough suppressants',
        'cure_methods': 'Rest, Hydration, Steam inhalation, Saltwater gargle',
        'outcome': 'Generally resolves within 7-10 days with proper care',
        'nearby_hospital': 'General Practice Clinic'
    },
    'Type 2 Diabetes': {
        'medication': 'Metformin, Sulfonylureas, Insulin as needed',
        'cure_methods': 'Diet control, Regular exercise, Blood sugar monitoring',
        'outcome': 'Manageable with proper medication and lifestyle changes',
        'nearby_hospital': 'Diabetes Care Center'
    },
    'Hypertension': {
        'medication': 'ACE inhibitors, Beta blockers, Diuretics',
        'cure_methods': 'Low-sodium diet, Regular exercise, Stress management',
        'outcome': 'Controllable with medication and lifestyle modifications',
        'nearby_hospital': 'Cardiovascular Center'
    },
    'Asthma': {
        'medication': 'Albuterol inhaler, Corticosteroids, Long-acting beta agonists',
        'cure_methods': 'Avoid triggers, Use air purifiers, Regular check-ups',
        'outcome': 'Manageable with proper medication and trigger avoidance',
        'nearby_hospital': 'Pulmonary Care Center'
    },
    'Migraine': {
        'medication': 'Triptans, NSAIDs, Anti-nausea medication',
        'cure_methods': 'Rest in dark room, Stress management, Trigger avoidance',
        'outcome': 'Manageable with proper medication and lifestyle adjustments',
        'nearby_hospital': 'Neurology Center'
    },
    'Gastritis': {
        'medication': 'Antacids, H2 blockers, Proton pump inhibitors',
        'cure_methods': 'Diet modification, Stress reduction, Small frequent meals',
        'outcome': 'Treatable with medication and dietary changes',
        'nearby_hospital': 'Gastroenterology Center'
    },
    'Arthritis': {
        'medication': 'NSAIDs, Disease-modifying antirheumatic drugs, Corticosteroids',
        'cure_methods': 'Physical therapy, Exercise, Joint protection',
        'outcome': 'Manageable with medication and physical therapy',
        'nearby_hospital': 'Rheumatology Center'
    },
    'Bronchitis': {
        'medication': 'Antibiotics (if bacterial), Cough suppressants, Bronchodilators',
        'cure_methods': 'Rest, Hydration, Humidifier use, Avoid irritants',
        'outcome': 'Usually resolves within 2-3 weeks with proper treatment',
        'nearby_hospital': 'Respiratory Care Center'
    },
    'COVID-19': {
        'medication': 'Antiviral medications, Pain relievers, Fever reducers',
        'cure_methods': 'Rest, Isolation, Hydration, Monitoring oxygen levels',
        'outcome': 'Recovery typically within 2-6 weeks depending on severity',
        'nearby_hospital': 'COVID Care Center'
    },
    'Dengue Fever': {
        'medication': 'Pain relievers, Fever reducers (avoid aspirin)',
        'cure_methods': 'Rest, Hydration, Platelet monitoring',
        'outcome': 'Recovery usually within 2-7 days with proper care',
        'nearby_hospital': 'Tropical Disease Center'
    },
    'Malaria': {
        'medication': 'Antimalarial drugs, Fever reducers',
        'cure_methods': 'Rest, Hydration, Regular monitoring',
        'outcome': 'Curable with appropriate antimalarial treatment',
        'nearby_hospital': 'Infectious Disease Center'
    },
    'Typhoid': {
        'medication': 'Antibiotics, Fever reducers',
        'cure_methods': 'Rest, Hydration, Soft diet',
        'outcome': 'Complete recovery with antibiotic treatment',
        'nearby_hospital': 'Infectious Disease Hospital'
    },
    'Common Cold': {
        'medication': 'Decongestants, Cough suppressants',
        'cure_methods': 'Rest, Hydration, Steam inhalation',
        'outcome': 'Recovery within 7-10 days',
        'nearby_hospital': 'General Clinic'
    },
    'Influenza': {
        'medication': 'Antiviral medications, Pain relievers',
        'cure_methods': 'Rest, Hydration, Isolation',
        'outcome': 'Recovery typically within 1-2 weeks',
        'nearby_hospital': 'General Hospital'
    },
    'Tuberculosis': {
        'medication': 'Antibiotics (multiple drugs)',
        'cure_methods': 'Long-term treatment, Regular monitoring',
        'outcome': 'Curable with complete treatment course',
        'nearby_hospital': 'TB Treatment Center'
    },
    'Chickenpox': {
        'medication': 'Antihistamines, Calamine lotion',
        'cure_methods': 'Rest, Cool baths, Prevent scratching',
        'outcome': 'Recovery within 1-2 weeks',
        'nearby_hospital': 'Pediatric Center'
    },
    'Measles': {
        'medication': 'Vitamin A, Fever reducers',
        'cure_methods': 'Rest, Hydration, Isolation',
        'outcome': 'Recovery within 7-10 days',
        'nearby_hospital': 'Infectious Disease Hospital'
    },
    'Viral Hepatitis': {
        'medication': 'Antiviral medications, Supportive care',
        'cure_methods': 'Rest, Proper nutrition, Avoid alcohol',
        'outcome': 'Recovery varies by type and severity',
        'nearby_hospital': 'Liver Specialist Center'
    },
    'Zika Virus': {
        'medication': 'Pain relievers, Fever reducers',
        'cure_methods': 'Rest, Hydration, Prevent mosquito bites',
        'outcome': 'Symptoms resolve within a week',
        'nearby_hospital': 'Tropical Disease Center'
    },
    'Cholera': {
        'medication': 'Oral rehydration solution, Antibiotics',
        'cure_methods': 'Immediate rehydration, Electrolyte replacement',
        'outcome': 'Recovery within a few days with treatment',
        'nearby_hospital': 'Emergency Care Center'
    },
    'Pneumonia': {
        'medication': 'Antibiotics, Cough medicine',
        'cure_methods': 'Rest, Hydration, Deep breathing exercises',
        'outcome': 'Recovery within 1-3 weeks with treatment',
        'nearby_hospital': 'Pulmonary Care Center'
    },
    'Meningitis': {
        'medication': 'Antibiotics, Anti-inflammatory drugs',
        'cure_methods': 'Hospitalization, Close monitoring',
        'outcome': 'Recovery varies; early treatment crucial',
        'nearby_hospital': 'Neurological Center'
    },
    'Food Poisoning': {
        'medication': 'Anti-diarrheal medication, Probiotics',
        'cure_methods': 'Rest, Hydration, Bland diet',
        'outcome': 'Recovery usually within 1-3 days',
        'nearby_hospital': 'Emergency Care Center'
    }
}

# Generate dataset
num_samples = 5000
data = []

for _ in range(num_samples):
    # Randomly select a disease
    disease = np.random.choice(list(disease_symptoms.keys()))
    
    # Randomly select one symptom combination for this disease
    symptom_idx = np.random.randint(0, len(disease_symptoms[disease]))
    symptoms = disease_symptoms[disease][symptom_idx]
    
    # Generate a random age appropriate for the disease
    if disease in ['Common Cold', 'Asthma']:
        age = np.random.randint(5, 80)
    else:
        age = np.random.randint(30, 85)
    
    # Get treatment information
    treatment = treatments[disease]
    
    data.append({
        'Disease': disease,
        'Symptom 1': symptoms[0],
        'Symptom 2': symptoms[1],
        'Symptom 3': symptoms[2],
        'Symptom 4': symptoms[3],
        'Age': age,
        'Medication': treatment['medication'],
        'Cure_Methods': treatment['cure_methods'],
        'Outcome': treatment['outcome'],
        'Nearby_Hospital': treatment['nearby_hospital']
    })

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('patient_case_similarity_dataset_v3.csv', index=False)

# Print dataset statistics
print("\nDataset Statistics:")
print(f"Total number of records: {len(df)}")
print(f"Number of unique diseases: {len(df['Disease'].unique())}")
print("\nDisease distribution:")
print(df['Disease'].value_counts())
print("\nAge statistics:")
print(df['Age'].describe())

# Print sample records
print("\nSample records:")
print(df.head())

# Print unique symptoms
print("\nUnique symptoms:")
all_symptoms = set()
for col in ['Symptom 1', 'Symptom 2', 'Symptom 3', 'Symptom 4']:
    all_symptoms.update(df[col].unique())
print(f"Total unique symptoms: {len(all_symptoms)}")
print(sorted(all_symptoms))
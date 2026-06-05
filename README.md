# 🏥 AI-Powered Patient Case Similarity System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![React](https://img.shields.io/badge/React-18.3-61DAFB.svg)](https://reactjs.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000.svg)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E.svg)](https://scikit-learn.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991.svg)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent full-stack healthcare application that predicts diseases from patient symptoms using a **Random Forest ML model** and provides personalized dietary recommendations via an **OpenAI-powered chatbot**.

---

## 📋 Table of Contents

- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Dataset](#-dataset)
- [ML Model Details](#-ml-model-details)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Disease Prediction** | Predicts disease from up to 4 symptoms + patient age using a trained Random Forest classifier |
| 💊 **Treatment Recommendations** | Provides medication, cure methods, outcome info, and nearby hospitals |
| 🤖 **AI Dietary Chat** | OpenAI GPT-3.5-powered chatbot recommends fruits, vegetables, and foods for the diagnosed condition |
| 📊 **Confidence Score** | Shows prediction probability for the identified disease |
| ⚡ **Real-time Inference** | Fast prediction via REST API with minimal latency |
| 🎨 **Clean UI** | Intuitive React-based frontend with modular component design |

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend (React)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────────┐ │
│  │  Symptom     │  │  Prediction  │  │    AI Diet Chatbot     │ │
│  │  Input Form  │  │  Results     │  │    (OpenAI GPT-3.5)    │ │
│  └──────┬───────┘  └──────────────┘  └────────────────────────┘ │
└─────────┼───────────────────────────────────────────────────────┘
          │  HTTP (REST API)
┌─────────▼───────────────────────────────────────────────────────┐
│                        Backend (Flask)                           │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────────┐ │
│  │  /predict    │  │  /symptoms   │  │       /chat            │ │
│  │  endpoint    │  │  endpoint    │  │       endpoint         │ │
│  └──────┬───────┘  └──────────────┘  └──────────┬─────────────┘ │
│         │                                         │               │
│  ┌──────▼───────────────────┐         ┌──────────▼─────────────┐ │
│  │  Random Forest Classifier│         │    OpenAI API Client   │ │
│  │  (scikit-learn)          │         │    (GPT-3.5-turbo)     │ │
│  └──────────────────────────┘         └────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
          │
┌─────────▼───────────────────────────────────────────────────────┐
│                         Data Layer                               │
│   patient_case_similarity_dataset_v3.csv  |  treatments.csv      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠 Tech Stack

**Backend**
- Python 3.8+
- Flask + Flask-CORS
- scikit-learn (Random Forest Classifier)
- pandas & numpy
- joblib (model serialization)
- OpenAI Python SDK

**Frontend**
- React 18.3
- react-icons
- @radix-ui/react-label, @radix-ui/react-slot
- class-variance-authority
- Custom CSS component library

---

## 📂 Project Structure

```
patient-case-similarity/
├── backend/                        # Flask API server
│   ├── app.py                      # Main application entry point & API routes
│   └── dataset_prepare.py          # Data preprocessing utilities
│
├── frontend/                       # React application
│   ├── public/                     # Static assets
│   └── src/
│       ├── App.js                  # Root application component
│       ├── App.css                 # Global application styles
│       ├── index.js                # React DOM entry point
│       └── components/             # Reusable UI components
│           ├── button.js / button.css
│           ├── card.js / card.css
│           ├── inout.js            # Input component
│           ├── input.css
│           ├── label.js / label.css
│           └── utils.js            # Shared utility functions
│
├── data/                           # Dataset files
│   ├── patient_case_similarity_dataset_v3.csv   # Main training dataset
│   └── treatments.csv              # Disease-to-treatment mappings
│
├── docs/                           # Additional documentation
│   └── API.md                      # API endpoint documentation
│
├── scripts/                        # Helper scripts
│   └── setup.sh                    # Automated environment setup
│
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 📦 Prerequisites

- **Python** 3.8 or higher
- **Node.js** 16 or higher & npm
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/patient-case-similarity.git
cd patient-case-similarity
```

### 2. Backend Setup

```bash
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
# OR
venv\Scripts\activate           # Windows

# Install Python dependencies
pip install -r ../requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY="your_openai_api_key_here"   # macOS/Linux
# OR
set OPENAI_API_KEY=your_openai_api_key_here         # Windows

# Start the Flask server (this will also train the ML model on first run)
python app.py
```

The backend will be available at `http://localhost:5000`.

> **Note:** The first startup trains the Random Forest model on the full dataset — this may take 1–2 minutes. The trained model is cached as `disease_model.joblib` for subsequent runs.

### 3. Frontend Setup

Open a new terminal:

```bash
cd frontend

# Install Node dependencies
npm install

# Start the React development server
npm start
```

The frontend will open at `http://localhost:3000`.

---

## 🖥 Usage

1. **Enter Patient Symptoms** — Fill in up to 4 symptoms (e.g., fever, cough, headache, fatigue) and the patient's age.
2. **Check Disease** — Click **Check Disease** to get the predicted condition with confidence score.
3. **View Treatment** — See recommended medications, cure methods, outcome, and nearby hospitals.
4. **AI Diet Advice** — Click the chat icon to ask the AI assistant for food, fruit, and vegetable recommendations tailored to the diagnosis.

---

## 📡 API Reference

See [`docs/API.md`](docs/API.md) for full endpoint documentation.

### Quick Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/predict` | Predict disease from symptoms + age |
| `GET` | `/symptoms` | Retrieve all known symptoms |
| `POST` | `/chat` | Get AI dietary recommendations |

**Example — Predict Disease:**

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "symptom1": "fever",
    "symptom2": "cough",
    "symptom3": "headache",
    "symptom4": "fatigue",
    "age": 35
  }'
```

**Response:**
```json
{
  "success": true,
  "disease": "Influenza",
  "confidence": "87.3%",
  "treatment": {
    "medication": "Oseltamivir",
    "cureMethods": "Rest, hydration, antiviral therapy",
    "outcome": "Full recovery expected in 7-10 days",
    "nearbyHospital": "City General Hospital"
  }
}
```

---

## 📊 Dataset

The training dataset (`data/patient_case_similarity_dataset_v3.csv`) contains anonymized patient case records with:

| Column | Description |
|--------|-------------|
| `Symptom 1–4` | Patient-reported symptoms |
| `Age` | Patient age |
| `Disease` | Diagnosed condition (target label) |
| `Medication` | Prescribed medication |
| `Cure_Methods` | Recommended treatments |
| `Outcome` | Expected recovery outcome |
| `Nearby_Hospital` | Suggested healthcare facility |

---

## 🤖 ML Model Details

| Parameter | Value |
|-----------|-------|
| Algorithm | Random Forest Classifier |
| Estimators | 100 trees |
| Max Depth | 10 |
| Min Samples Split | 5 |
| Min Samples Leaf | 2 |
| Test Split | 20% |
| Feature Encoding | Label Encoding (symptoms + disease) |
| Serialization | joblib |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate comments.

---

## ⚠️ Disclaimer

This application is intended for **educational and research purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical decisions.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

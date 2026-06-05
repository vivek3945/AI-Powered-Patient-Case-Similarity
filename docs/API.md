# API Reference

Base URL: `http://localhost:5000`

---

## POST `/predict`

Predicts a disease based on patient symptoms and age.

### Request Body

```json
{
  "symptom1": "string",
  "symptom2": "string",
  "symptom3": "string",
  "symptom4": "string",
  "age": "integer"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `symptom1` | string | Yes | First symptom (case-insensitive) |
| `symptom2` | string | Yes | Second symptom |
| `symptom3` | string | Yes | Third symptom |
| `symptom4` | string | Yes | Fourth symptom |
| `age` | integer | Yes | Patient age in years |

### Success Response (200)

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

### Error Response (400)

```json
{
  "success": false,
  "error": "Error description"
}
```

---

## GET `/symptoms`

Returns a sorted list of all recognized symptoms the model was trained on.

### Success Response (200)

```json
{
  "success": true,
  "symptoms": [
    "abdominal pain",
    "back pain",
    "chest pain",
    "cough",
    "fatigue",
    "fever",
    "..."
  ]
}
```

---

## POST `/chat`

Sends a message to the OpenAI GPT-3.5-turbo chatbot, which returns dietary recommendations (fruits, vegetables, and foods) suited to the patient's diagnosed condition.

### Request Body

```json
{
  "message": "string"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `message` | string | Yes | Disease/symptom description to get dietary advice for |

### Success Response (200)

```json
{
  "success": true,
  "response": "Fruits:\nApple\nBanana\nOrange\n\nVegetables:\nSpinach\nCarrot\nBroccoli\n\nFoods:\nOatmeal\nChicken Soup\nYogurt"
}
```

### Error Response (400)

```json
{
  "success": false,
  "error": "Error description"
}
```

---

## Error Handling

All endpoints return a consistent error format:

```json
{
  "success": false,
  "error": "Human-readable error message"
}
```

Common HTTP status codes:
- `200` — Success
- `400` — Bad request (invalid or missing parameters)
- `500` — Internal server error

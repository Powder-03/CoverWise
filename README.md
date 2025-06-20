# Premium Predictor API

A FastAPI-based machine learning service that predicts insurance premium categories based on user demographics, health metrics, and lifestyle factors. The application uses a pre-trained model to provide quick and accurate premium category predictions.

## 🌐 **Live Demo**

**🚀 The API is now live on AWS EC2!**

- **Base URL**: `http://3.94.195.184:8000`
- **API Documentation**: [http://3.94.195.184:8000/docs](http://3.94.195.184:8000/docs)
- **Health Check**: [http://3.94.195.184:8000/health](http://3.94.195.184:8000/health)

### Quick Test:
```bash
# Health check
curl http://3.94.195.184:8000/health

# Make a prediction
curl -X POST "http://3.94.195.184:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "age": 30,
       "weight": 70.0,
       "height": 1.75,
       "income_lpa": 10.0,
       "smoker": false,
       "city": "Mumbai",
       "occupation": "private_job"
     }'
```

**Expected Response:**
```json
{
  "predicted_category": "medium",
  "confidence": 0.7652,
  "class_probabilities": {
    "high": 0.1543,
    "low": 0.0805,
    "medium": 0.7652
  }
}
```

## 🚀 Features

- **Smart Predictions**: ML-powered insurance premium category predictions
- **Fast API**: Built with FastAPI for high-performance async operations
- **Health Monitoring**: Built-in health check endpoints
- **Docker Ready**: Containerized deployment support
- **API Documentation**: Auto-generated OpenAPI documentation
- **Type Safety**: Full type hints with Pydantic models

## 📁 Project Structure

```
premium_predictor/
├── app.py                    # FastAPI application main file
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container configuration
├── config/
│   └── city_tier.py         # City classification config
├── model/
│   ├── insurance.csv        # Training dataset
│   ├── model_training.ipynb # Model development notebook
│   ├── model.pkl           # Trained ML model
│   └── predict.py          # Prediction logic
└── schema/
    ├── prediction_response.py # Response data models
    └── user_input.py        # Request data models
```

## 🛠️ Installation

### Local Development

1. Clone the repository and create a virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Start the development server:
```powershell
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

### 🐳 Docker Deployment

#### Option 1: Pull from Docker Hub
```powershell
docker pull powder04/coverwise:latest
docker run -d -p 8000:8000 powder04/coverwise:latest
```

#### Option 2: Build from Source
1. Build the Docker image:
```powershell
docker build -t powder04/coverwise .
```

2. Run the container:
```powershell
docker run -d -p 8000:8000 powder04/coverwise
```

## 📚 API Documentation

### Endpoints

#### 1. GET /
Welcome endpoint with API information.

#### 2. GET /health
Health check endpoint returning:
- API operational status
- Model version information
- Model loading status

#### 3. POST /predict

Predicts insurance premium category based on user data.

**Request Body**:
```json
{
    "age": 30,
    "weight": 70.0,
    "height": 1.75,
    "income_lpa": 10.0,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
}
```

**Response**:
```json
{
    "predicted_category": "medium",
    "confidence": 0.8542,
    "class_probabilities": {
        "high": 0.1234,
        "low": 0.0224,
        "medium": 0.8542
    }
}
```

### Interactive Documentation
- Swagger UI (Local): `http://localhost:8000/docs`
- Swagger UI (Live): `http://3.94.195.184:8000/docs`
- ReDoc (Local): `http://localhost:8000/redoc`
- ReDoc (Live): `http://3.94.195.184:8000/redoc`

## 🧮 Model Information

The prediction model:
- **Algorithm**: Gradient boosting for classification
- **Input Features**:
  - Age group (young, adult, middle_aged, senior)
  - BMI calculation (weight/height²)
  - Income bracket (LPA - Lakhs Per Annum)
  - Lifestyle risk factors (based on smoking + BMI)
  - City tier (1, 2, or 3 based on city classification)
  - Occupation category (7 different types)
- **Output Categories**: low, medium, high premium
- **Model Confidence**: Provides probability scores for all categories
- **Response Format**: 
  - `predicted_category`: Most likely premium category
  - `confidence`: Probability of the predicted category (0-1)
  - `class_probabilities`: Detailed breakdown of all category probabilities

## 🛡️ Error Handling

The API implements proper error handling for:
- Invalid input data
- Missing required fields
- Model prediction errors
- Server-side exceptions

## 🔒 Dependencies

Major dependencies include:
- FastAPI
- Uvicorn
- Pydantic
- Scikit-learn
- Python-jose
- Passlib

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🔍 Swagger Documentation

Access the full API documentation at:
- **Local**: `http://localhost:8000/docs`
- **Live (AWS EC2)**: `http://3.94.195.184:8000/docs`

## 🌐 Live API Usage Examples

### Using curl:
```bash
# Test the live API
curl -X POST "http://3.94.195.184:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "age": 25,
       "weight": 65.0,
       "height": 1.70,
       "income_lpa": 8.0,
       "smoker": false,
       "city": "Delhi",
       "occupation": "government_job"
     }'
```

**Expected Response:**
```json
{
  "predicted_category": "low", 
  "confidence": 0.7834,
  "class_probabilities": {
    "high": 0.0876,
    "low": 0.7834,
    "medium": 0.1290
  }
}
```

### Using Python:
```python
import requests

response = requests.post(
    "http://3.94.195.184:8000/predict",
    json={
        "age": 35,
        "weight": 75.0,
        "height": 1.80,
        "income_lpa": 12.0,
        "smoker": True,
        "city": "Bangalore",
        "occupation": "private_job"
    }
)

result = response.json()
print(f"Predicted Category: {result['predicted_category']}")
print(f"Confidence: {result['confidence']:.2%}")
print(f"All Probabilities: {result['class_probabilities']}")
```

**Expected Output:**
```
Predicted Category: high
Confidence: 89.45%
All Probabilities: {'high': 0.8945, 'low': 0.0234, 'medium': 0.0821}
```

## ☁️ AWS EC2 Deployment

The application is deployed on AWS EC2:
- **Instance IP**: `3.94.195.184`
- **Port**: `8000`
- **Deployment**: Docker containerized
- **Access**: Public HTTP endpoint
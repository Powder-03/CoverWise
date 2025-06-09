# CoverWise

A FastAPI-based machine learning service that predicts insurance premium categories based on user demographics, health metrics, and lifestyle factors. The application uses a pre-trained model to provide quick and accurate premium category predictions.

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

1. Build the Docker image:
```powershell
docker build -t powder04/premium_predictor_api .
```

2. Run the container:
```powershell
docker run -d -p 8000:8000 premium-predictor
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
    "prediction_category": "medium"
}
```

### Interactive Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🧮 Model Information

The prediction model:
- Uses gradient boosting for classification
- Takes into account:
  - Age group
  - BMI calculation
  - Income bracket
  - Lifestyle risk factors
  - City tier
  - Occupation category
- Outputs premium categories: low, medium, high

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
```
http://localhost:8000/docs
```

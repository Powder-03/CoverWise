from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output , model , MODEL_VERSION
from schema.prediction_response import PredictionResponse



app = FastAPI()



# Human readable description of the API
@app.get("/")
def home():
    return {'message': "Insurance premium prediction API."}


# Health check endpoint is used when we deploy the app on a server . It checks if the server is running properly.
# Machine readable description of the API
# Kubernetes and other deployment tools use this endpoint to check the health of the application.
@app.get("/health")
def health_check():
    return {
        "status": "ok", 
        "model_version": MODEL_VERSION , 
        "model_loaded": model is not None,  # to check if the model is loaded successfully
        }

@app.post("/predict" , response_model=PredictionResponse)
def predict(data : UserInput):
    
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,
    }
    
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200 , content = {'prediction_category': prediction})
    
    except Exception as e :
        
        return JSONResponse(status_code=500 , content = str(e))
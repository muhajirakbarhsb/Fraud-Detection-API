import joblib
# from pathlib import Path

import pandas as pd

from fastapi import FastAPI, status, Response
import numpy as np
import uvicorn
from pydantic import BaseModel
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import Histogram, Summary
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(
    title="Machine Learning - Fraud detector API",
    description="ML API to detect if a credit card transaction is fraudulent or not",
    version="0.0.1",
    debug=True
)

# BASE_DIR = Path(__file__).resolve(strict=True).parent

with open("fraud_detection_model-0.0.1.pkl", "rb") as file:
    model = joblib.load(file)

class DataValidation(BaseModel):
    step: int
    type: int
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float

REQUEST_COUNTER = Counter("api_requests_total", "Total number of API requests")
LATENCY_HISTOGRAM = Histogram("api_request_latency_seconds", "API request latency in seconds")
PROBABILITY_FRAUD_GAUGE = Gauge("probability_fraud", "Probability of fraud")
PROBABILITY_NON_FRAUD_GAUGE = Gauge("probability_non_fraud", "Probability of non-fraud")
SUM_FRAUD_GAUGE = Gauge("sum_fraud", "Sum of fraud")
SUM_NON_FRAUD_GAUGE = Gauge("sum_non_fraud", "Sum of non-fraud")

@app.get("/")
def home():
    return {
        "Message": "Machine learning API to detect credit fraud",
        "Health Check": "OK",
        "Version": "0.0.1"
    }

@app.post("/prediction", status_code=status.HTTP_201_CREATED)
def inference(data: DataValidation):
    REQUEST_COUNTER.inc()

    with LATENCY_HISTOGRAM.time():
        features = data.dict()
        features = pd.DataFrame(features, index=[0])

        pred = model.predict(features)
        pred_prob = model.predict_proba(features)

        prob_nofraud = np.round(pred_prob[0, 0] * 100, 2)
        prob_fraud = np.round(pred_prob[0, 1] * 100, 2)

        PROBABILITY_FRAUD_GAUGE.set(prob_fraud)
        PROBABILITY_NON_FRAUD_GAUGE.set(prob_nofraud)

        if pred == 1:
            SUM_FRAUD_GAUGE.inc()
            return {"Result": f"Transaction is potentially fraudulent with a probability of {prob_fraud}%"}
        else:
            SUM_NON_FRAUD_GAUGE.inc()
            return {"Result": f"Transaction is not potentially fraudulent with a probability of {prob_nofraud}%"}
@app.get("/metrics")
def prometheus_metrics():
    return PlainTextResponse(content=generate_latest().decode(), media_type=CONTENT_TYPE_LATEST)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

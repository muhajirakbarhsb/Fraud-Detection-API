FROM python:3.9
WORKDIR /PROJECT


# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt 
RUN pip install uvicorn 
RUN pip install joblib 
RUN pip install numpy
RUN pip install prometheus-client
RUN pip install fastapi
RUN pip install requests
RUN pip install pandas
RUN pip install xgboost
RUN pip install scikit-learn
RUN echo "Cache refresh"

# Copy the code
COPY main.py .
# COPY test.py .
COPY fraud_detection_model-0.0.1.pkl .
# Set the command to run
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "test.py"]
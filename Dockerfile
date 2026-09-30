FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY serve_api_class.py .
COPY flight_price_model.pkl .
EXPOSE 10000
CMD ["sh", "-c", "uvicorn serve_api_class:app --host 0.0.0.0 --port ${port:-10000}"]

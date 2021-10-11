pip install -r requirements.txt

PORT=8080
uvicorn app.main:app --port $PORT

# Requirements
- Python 3.6+
- pip


# Install dependencies
`pip install -r requirements.txt`

# Run application
`uvicorn app.main:app --port $PORT`

$PORT - port for launching server

# Run in development
`uvicorn app.main:app --reload --port $PORT`

$PORT - port for launching server

# Afya Handshake Service

## Setup
1. Extract zip
2. Rename `.env.example` to `.env`
3. Run:
   pip install -r requirements.txt
   python run.py

## Endpoints
- /initiate
- /complete
- /auto

## Docker
docker build -t afya-service .
docker run -p 5000:5000 afya-service

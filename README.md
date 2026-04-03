# Motion Detection API

This project detects motion using a webcam and logs events to a FastAPI server.

## Features
- Real-time motion detection using OpenCV
- Sends events to API when motion is detected
- Stores logs in memory
- API endpoints to view logs

## Technologies
- Python
- OpenCV
- FastAPI

## How to run

1. Install dependencies:
pip install opencv-python fastapi uvicorn requests

2. Run the app:
python FINAL.py

3. Open:
http://127.0.0.1:8000/logs

import cv2
import requests
import threading
from fastapi import FastAPI
import uvicorn

app = FastAPI()

logs = []

@app.post("/log")
def log_event(data: dict):
    logs.append(data)
    print("Event saved:", data)
    return {"message": "saved"}

@app.get("/logs")
def get_logs():
    return logs


def run_camera():

    cap = cv2.VideoCapture(0)

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while True:

        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

        motion = thresh.sum()

        if motion > 1000000:
            print("Motion detected")

            try:
                requests.post(
                    "http://127.0.0.1:8000/log",
                    json={"event": "motion"}
                )
            except:
                print("API error")

        cv2.imshow("Camera", frame1)

        frame1 = frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(10) == ord("c"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    camera_thread = threading.Thread(target=run_camera)
    camera_thread.start()

    uvicorn.run(app, host="127.0.0.1", port=8000)
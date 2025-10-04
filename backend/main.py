from fastapi import FastAPI, WebSocket
from ultralytics import YOLO
import cv2, time, asyncio
from collections import deque, Counter

app = FastAPI()
model = YOLO("models/best.pt")
cap = cv2.VideoCapture("rtmp://localhost/live/stream")

window = deque(maxlen=5)

@app.websocket("/ws/detect")
async def detect_ws(websocket: WebSocket):
    await websocket.accept()
    last_infer_time = 0
    infer_interval = 5  # seconds between YOLO inferences

    while True:
        ret, frame = cap.read()
        if not ret:
            await asyncio.sleep(1)
            continue

        now = time.time()
        if now - last_infer_time >= infer_interval:
            results = model.predict(frame, conf=0.3, verbose=False)
            detections = [
                {"class": model.names[int(b.cls.item())], "confidence": float(b.conf.item())}
                for b in results[0].boxes
            ]

            if detections:
                top = max(detections, key=lambda d: d["confidence"])
                window.append(top["class"])

            last_infer_time = now
            if window:
                msg = {
                    "smoothed_class": Counter(window).most_common(1)[0][0],
                    "recent_votes": list(window),
                    "timestamp": now,
                }
            else:
                msg = {"status": "no detections", "timestamp": now}

            await websocket.send_json(msg)
        await asyncio.sleep(0.2)

import cv2
import asyncio
import websockets
import time
import json
from ultralytics import YOLO

# Load your trained YOLO model
model = YOLO("models/best.pt")

# Try RTMP stream first
rtmp_url = "rtmp://localhost/live/stream"
cap = cv2.VideoCapture(rtmp_url)

if not cap.isOpened():
    print("⚠️ RTMP stream not available, falling back to local video...")
    cap = cv2.VideoCapture("../videos/plover.mp4")

if not cap.isOpened():
    raise RuntimeError("❌ Could not open RTMP stream or local video.")

# WebSocket server (FastAPI backend must be running on this port)
uri = "ws://localhost:8000/ws/detect"

# Detection settings
CONF_THRESHOLD = 0.5
BATCH_INTERVAL = 5  # seconds

async def detection_loop():
    async with websockets.connect(uri) as websocket:
        last_batch_time = time.time()
        batch_detections = []

        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ No more frames available.")
                break

            # Run YOLO inference
            results = model.predict(frame, conf=CONF_THRESHOLD, verbose=False)

            detections = []
            for box in results[0].boxes:
                detections.append({
                    "class": model.names[int(box.cls.item())],
                    "confidence": float(box.conf.item())
                })

            if detections:
                batch_detections.extend(detections)

            # Send batch every 5 seconds
            if time.time() - last_batch_time >= BATCH_INTERVAL:
                if batch_detections:
                    payload = {
                        "detections": batch_detections,
                        "timestamp": time.time()
                    }
                else:
                    payload = {
                        "detections": [],
                        "status": "no detections",
                        "timestamp": time.time()
                    }

                await websocket.send(json.dumps(payload))
                print("📤 Sent:", payload)

                # Reset batch
                batch_detections = []
                last_batch_time = time.time()

if __name__ == "__main__":
    try:
        asyncio.run(detection_loop())
    except KeyboardInterrupt:
        print("🛑 Detection stopped by user.")
    finally:
        cap.release()

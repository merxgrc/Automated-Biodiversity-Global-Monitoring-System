# ==============================
# BASE IMAGE: NVIDIA CUDA with Ubuntu (for GPU support)
# ==============================
FROM nvidia/cuda:12.1.0-base-ubuntu22.04

# ==============================
# INSTALL DEPENDENCIES
# ==============================
RUN apt-get update && apt-get install -y \
    python3 python3-pip ffmpeg nginx curl \
    && rm -rf /var/lib/apt/lists/*

# ==============================
# SET WORKDIR
# ==============================
WORKDIR /app

# ==============================
# COPY BACKEND FILES INTO CONTAINER
# ==============================
COPY ./backend /app

# ==============================
# INSTALL PYTHON DEPENDENCIES
# ==============================
RUN pip install --no-cache-dir -r requirements-gpu.txt

# ==============================
# EXPOSE PORTS
#  - 8000: FastAPI
#  - 1935: RTMP (video stream)
#  - 8080: optional front-end or Nginx
# ==============================
EXPOSE 8000 1935 8080

# ==============================
# STARTUP COMMAND
# ==============================
# This runs FFmpeg in the background to simulate a live drone stream from your video
# and then starts the FastAPI server for YOLO inference.
CMD ffmpeg -re -stream_loop -1 -i /app/videos/DronesVideos.mp4 \
    -c:v libx264 -f flv rtmp://localhost:1935/live/stream & \
    uvicorn main:app --host 0.0.0.0 --port 8000

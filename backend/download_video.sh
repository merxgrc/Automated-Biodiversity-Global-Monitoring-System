#!/bin/bash
set -e

echo "🎥 Downloading demo video..."
mkdir -p videos

# Replace FILE_ID with your Google Drive file ID
FILE_ID="YOUR_FILE_ID_HERE"

# Use the Drive API to download
curl -L "https://drive.google.com/uc?export=download&id=${FILE_ID}" -o videos/DronesVideos.mp4

echo "✅ Video downloaded successfully!"

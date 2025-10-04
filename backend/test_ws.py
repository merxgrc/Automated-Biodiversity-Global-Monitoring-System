import asyncio, websockets, json, time

async def test_ws():
    uri = "ws://localhost:8000/ws/detect"
    while True:
        try:
            async with websockets.connect(uri, ping_interval=20) as websocket:
                print("✅ Connected to server.")
                while True:
                    msg = await websocket.recv()
                    data = json.loads(msg)
                    print("[LOG]", data)
        except Exception as e:
            print("⚠️ Connection lost:", e)
            print("Reconnecting in 5s...")
            time.sleep(5)

asyncio.run(test_ws())


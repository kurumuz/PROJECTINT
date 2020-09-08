import asyncio
import websockets

print("PROJECTINT V0.0.1")

async def init(websocket, path):
    await parser_handler(websocket, path)

async def parser_handler(websocket, path):
    try: #TODO: Better error handling
        async for message in websocket:
            await parser(message, websocket, path)
    except:
        print("client disconnected")

async def parser(message, websocket, path):
    print(f"< {message}")
    await websocket.send("allah")

start_server = websockets.serve(init, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

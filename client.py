import asyncio
import websockets

data_buf = ""

def clear_buf():
    global data_buf
    data_buf = ""

def check_buf():
    global data_buf
    return len(data_buf) != 0

def verb_1():
    global data_buf
    data_buf = "eren"

def verb_2():
    return

async def send(data):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(data)
        print(f">{data}")
        ret = await websocket.recv()
        print(f"<{ret}")

async def main2():
    global data_buf
    if check_buf():
        await send(data_buf)
        clear_buf()

verb_1()
asyncio.get_event_loop().run_until_complete(main2())
asyncio.get_event_loop().run_forever()
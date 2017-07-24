import websockets
import asyncio

async def communication_handler(websocket, path):
    name = await websocket.recv()
    global clients
    clients.add(websocket)
    for client in clients:
        await client.send("{} joined the conversation".format(name))
    while True:
        try:
            message = await websocket.recv()
            new_message = "<b>{}:</b> {}".format(name, message)
            print(clients)
            for client in clients:
                await client.send(new_message)
        except:
            clients.remove(websocket)

if __name__ == "__main__":
    clients = set()
    start_server = websockets.serve(communication_handler, 'localhost', 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
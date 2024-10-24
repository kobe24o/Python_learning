import asyncio
import json
import websockets

# Store all connected clients
clients = set()
messages = []

# Handle client messages
async def handle_client(websocket, path):
    # Add the new client to the set of connected clients
    clients.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            if data['type'] == 'message':
                # Ensure the required keys are present
                if 'id' in data and 'username' in data and 'message' in data:
                    # Store the message with its ID and username
                    messages.append({'id': data['id'], 'username': data['username'], 'message': data['message'], 'userId': data['userId']})
                    # Broadcast the message to all connected clients
                    await broadcast(json.dumps(data))
            elif data['type'] == 'revoke':
                # Ensure the required keys are present
                if 'id' in data and 'userId' in data:
                    # Find the message by ID
                    msg = next((msg for msg in messages if msg['id'] == data['id']), None)
                    if msg and msg['userId'] == data['userId']:
                        messages.remove(msg)
                        # Broadcast the revoke message to all connected clients
                        await broadcast(json.dumps(data))
    finally:
        # Remove the client from the set of connected clients
        clients.remove(websocket)

async def broadcast(message):
    if clients:  # If there are connected clients
        await asyncio.wait([asyncio.create_task(client.send(message)) for client in clients])

# Start WebSocket server
async def start_server():
    async with websockets.serve(handle_client, "localhost", 6789):
        print("WebSocket server started")
        await asyncio.Future()  # Run the server until manually stopped

# Run the server
asyncio.run(start_server())
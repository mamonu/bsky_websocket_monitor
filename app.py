from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import asyncio
import websockets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

async def filter_and_forward_messages(ws, keyword):
    """Filter messages containing the keyword and forward them to the client."""
    try:
        async for message in ws:
            if keyword in message:  # Check if the keyword is in the message
                socketio.emit('log', {'message': message})
    except Exception as e:
        socketio.emit('log', {'message': f'Error: {str(e)}'})

@socketio.on('connect_to_ws')
def connect_to_ws(data):
    """Handle connection to the external WebSocket."""
    url = data.get('url')
    if not url:
        emit('log', {'message': 'No WebSocket URL provided!'})
        return

    # Keyword to filter messages
    keyword = " AI "

    async def external_ws():
        try:
            async with websockets.connect(url) as ws:
                emit('log', {'message': f'Connected to {url}'})
                await filter_and_forward_messages(ws, keyword)
        except Exception as e:
            emit('log', {'message': f'Error: {str(e)}'})

    # Run the external WebSocket connection
    asyncio.run(external_ws())

@socketio.on('disconnect_from_ws')
def disconnect_from_ws():
    """Handle disconnection from the WebSocket."""
    emit('log', {'message': 'Disconnected by user'})

if __name__ == '__main__':
    socketio.run(app)

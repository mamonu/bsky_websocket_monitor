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

@socketio.on('connect_to_ws')
def connect_to_ws(data):
    """Handle connection to the external WebSocket."""
    url = data.get('url')
    if not url:
        emit('log', {'message': 'No WebSocket URL provided!'})
        return

    async def external_ws():
        try:
            async with websockets.connect(url) as ws:
                emit('log', {'message': f'Connected to {url}'})
                async for message in ws:
                    emit('log', {'message': f'Received: {message}'})
        except Exception as e:
            emit('log', {'message': f'Error: {str(e)}'})

    asyncio.run(external_ws())

@socketio.on('disconnect_from_ws')
def disconnect_from_ws():
    """Handle disconnection from the WebSocket."""
    emit('log', {'message': 'Disconnected by user'})

if __name__ == '__main__':
    socketio.run(app)

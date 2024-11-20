# Bluesky WebSocket Feed Monitor

This is a Python Flask web application that monitors and logs messages from a WebSocket feed. It provides a simple interface to connect, disconnect, and view messages in real-time.

![synthwave BSky Websocket Feed Monitor](Bluesky-WebSocket-Feed-Monitor.png)

## Features

- **Connect to WebSocket**: Establish a connection to a predefined WebSocket URL.
- **Real-Time Logs**: Display messages received from the WebSocket in real-time.
- **Clear Logs**: Clear the log view with a single button.
- **Disconnect**: Gracefully disconnect from the WebSocket.

## Project Structure

```plaintext
websocket_monitor/
├── app.py                # Flask application with WebSocket functionality
├── templates/
│   └── index.html        # Frontend HTML template
├── static/
│   ├── style.css         # CSS styling for the frontend
│   └── script.js         # JavaScript logic for frontend interactivity
```

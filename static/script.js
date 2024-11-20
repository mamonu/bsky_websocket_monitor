const socket = io();
const output = document.getElementById('output');

// Log function to display messages
function log(message) {
    const timestamp = new Date().toISOString();
    output.value += `[${timestamp}] ${message}\n`;
    output.scrollTop = output.scrollHeight; // Auto-scroll to the latest message
}

// Connect button logic
document.getElementById('connect').addEventListener('click', () => {
    const url = 'wss://jetstream2.us-east.bsky.network/subscribe?wantedCollections=app.bsky.feed.post';
    socket.emit('connect_to_ws', { url });
});

// Disconnect button logic
document.getElementById('disconnect').addEventListener('click', () => {
    socket.emit('disconnect_from_ws');
});

// Clear log button logic
document.getElementById('clear').addEventListener('click', () => {
    output.value = '';
});

// Listen for filtered messages from the backend
socket.on('log', (data) => {
    log(data.message);
});


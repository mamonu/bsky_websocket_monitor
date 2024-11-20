const socket = io();
const output = document.getElementById('output');

function log(message) {
    const timestamp = new Date().toISOString();
    output.value += `[${timestamp}] ${message}\n`;
    output.scrollTop = output.scrollHeight;
}

document.getElementById('connect').addEventListener('click', () => {
    const url = 'wss://jetstream2.us-east.bsky.network/subscribe?wantedCollections=app.bsky.feed.post';
    socket.emit('connect_to_ws', { url });
});

document.getElementById('disconnect').addEventListener('click', () => {
    socket.emit('disconnect_from_ws');
});

document.getElementById('clear').addEventListener('click', () => {
    output.value = '';
});

socket.on('log', (data) => {
    log(data.message);
});

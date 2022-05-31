const WebSocketServer = require('ws').Server
const wss = new WebSocketServer({ port: 6969 });

wss.on('connection', function connection(ws) {
    console.log('Client connected');
    ws.on('message', function message(data) {
        console.log('received: %s', data);
    });

    ws.send('something');
});
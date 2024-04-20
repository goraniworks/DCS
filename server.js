const WebSocket = require('ws');
const net = require('net');

const WEB_SOCKET_PORT = 15348; // WebSocket 포트
const TCP_PORT = 15349;        // TCP 서버 포트

// 게임 스크립트는 여기에 있다. C:\Users\Jason\Saved Games\DCS\Scripts

// WebSocket 서버 생성
const wss = new WebSocket.Server({ port: WEB_SOCKET_PORT });
console.log(`WebSocket server is running on ws://localhost:${WEB_SOCKET_PORT}`);

// 모든 연결된 WebSocket 클라이언트를 관리하기 위한 세트
const clients = new Set();

wss.on('connection', function connection(ws) {
    clients.add(ws);
    console.log('WebSocket client connected');

    ws.on('close', () => {
        clients.delete(ws);
        console.log('WebSocket client disconnected');
    });
});

// TCP 서버 생성
const tcpServer = net.createServer((socket) => {
    console.log('TCP client connected');

    socket.on('data', (data) => {
        console.log(`Data received from TCP client: ${data}`);
        // 모든 WebSocket 클라이언트에게 데이터 전송
        for (const client of clients) {
            if (client.readyState === WebSocket.OPEN) {
                client.send(data.toString());
            }
        }
    });

    socket.on('end', () => {
        console.log('TCP client disconnected');
    });
});

tcpServer.listen(TCP_PORT, () => {
    console.log(`TCP server is running on port ${TCP_PORT}`);
});

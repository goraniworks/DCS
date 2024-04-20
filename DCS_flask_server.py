from flask import Flask, render_template
from flask_socketio import SocketIO
import socket
import threading

# app = Flask(__name__)
app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

def receive_data():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 15348))
    server_socket.listen(1)
    print("Waiting for DCS connection...")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            decoded_data = data.decode()
            print(f"Received Data: {decoded_data}")
            # 여기서 웹 클라이언트에 데이터를 전송합니다.
            socketio.emit('DCS_data', {'data': decoded_data})
    finally:
        conn.close()
        server_socket.close()

@app.route('/')
def index():
    return render_template('index.html')  # 계기판을 표시하는 HTML 파일

if __name__ == "__main__":
    # DCS 데이터 수신을 위한 별도 스레드 시작
    threading.Thread(target=receive_data).start()
    # Flask 애플리케이션 시작
    socketio.run(app, debug=True)

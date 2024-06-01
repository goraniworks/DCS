### DCS 게임 데이터 실시간 웹페이지 표현
### Real-Time Display of DCS Game Data on a Web Page

[YouTube 동영상 보기](https://youtu.be/8s-PyVehyP4)

[![Watch the video](https://img.youtube.com/vi/8s-PyVehyP4/hqdefault.jpg)](https://www.youtube.com/watch?v=8s-PyVehyP4&t=27s)
#### 목차
- [목차](#목차)
- [프로젝트의 기본적인 원리](#프로젝트의-기본적인-원리)
- [실행하는 법](#실행하는-법)
- [코드 설명](#코드-설명)
- [프로젝트의 의의](#프로젝트의-의의)

#### Table of Contents
- [Table of Contents](#table-of-contents)
- [Basic Principles of the Project](#basic-principles-of-the-project)
- [How to Run](#how-to-run)
- [Code Explanation](#code-explanation)
- [Significance of the Project](#significance-of-the-project)


#### [프로젝트의 기본적인 원리](#프로젝트의-기본적인-원리)

이 프로젝트는 DCS (Digital Combat Simulator) 게임에서 발생하는 실시간 데이터를 웹 페이지에 동적으로 표시하는 방법을 설명합니다. DCS는 실시간 전투기 시뮬레이션 게임이며, 게임 내의 다양한 비행 데이터를 외부 애플리케이션으로 전송할 수 있습니다. 이를 위해 Lua 스크립트를 사용하여 데이터를 수집하고, TCP/IP를 통해 Node.js 기반의 서버로 전송합니다. 이 서버는 WebSocket 프로토콜을 이용하여 웹 브라우저에 데이터를 전달하고, 브라우저는 이 데이터를 사용하여 사용자에게 시각적인 피드백을 제공합니다.
**이 프로젝트는 chat-GPT4에 의존해서 이루어 졌으며, 코드, 문서 작성의 90% 는 AI가 작성하였습니다.**

#### [Basic Principles of the Project](#basic-principles-of-the-project)
This project explains how to dynamically display real-time data from the DCS (Digital Combat Simulator) game on a web page. DCS is a real-time combat flight simulation game that can send various flight data to external applications. To achieve this, Lua scripts are used to collect the data, which is then sent to a Node.js-based server via TCP/IP. This server uses the WebSocket protocol to deliver the data to a web browser, which provides visual feedback to the user.
**This project relies on chat-GPT4, with 90% of the code and documentation written by AI.**

##### 데이터 수집 및 전송

1. **Lua 스크립트**: Lua는 경량 프로그래밍 언어로, DCS 같은 복잡한 게임에서 사용자 지정 스크립트를 통해 확장 기능을 구현할 수 있습니다. 이 프로젝트에서는 Lua 스크립트를 사용하여 비행 데이터(예: 지시 공기속도, 고도, 피치, 롤, 헤딩 등)를 실시간으로 수집합니다. 이 데이터는 게임 엔진에서 제공하는 API 함수를 호출하여 얻습니다. 예를 들어, `LoGetIndicatedAirSpeed()` 함수는 현재 항공기의 지시 공기속도를 반환합니다.

2. **TCP/IP를 통한 전송**: 수집된 데이터는 문자열 형태로 포맷되어 TCP 소켓을 통해 Node.js 서버로 전송됩니다. TCP (Transmission Control Protocol)는 인터넷에서 데이터를 안정적으로, 순서대로, 에러 없이 전송하기 위한 표준입니다. 이 프로젝트에서 Lua 스크립트는 TCP 클라이언트 역할을 하며, Node.js 서버와의 연결을 유지하면서 지속적으로 데이터를 전송합니다.

##### Data Collection and Transmission

1. **Lua Script**: Lua is a lightweight programming language that can implement custom scripts for extended functionality in complex games like DCS. This project uses Lua scripts to collect flight data (e.g., indicated airspeed, altitude, pitch, roll, heading) in real time. The data is obtained by calling API functions provided by the game engine. For example, the `LoGetIndicatedAirSpeed()` function returns the current indicated airspeed of the aircraft.

2. **Transmission via TCP/IP**: The collected data is formatted as a string and sent to a Node.js server via a TCP socket. TCP (Transmission Control Protocol) is a standard for reliably, sequentially, and error-free data transmission over the internet. In this project, the Lua script acts as a TCP client, continuously transmitting data while maintaining a connection with the Node.js server.


##### 데이터 수신 및 웹 브라우저로의 전달


1. **Node.js 서버**: 이 서버는 TCP 서버와 WebSocket 서버 두 가지 역할을 수행합니다. 먼저, TCP 서버는 DCS 게임으로부터 데이터를 수신합니다. 이 서버는 데이터를 받은 후 이를 처리하여 다수의 클라이언트에게 동시에 정보를 제공할 수 있도록 설계되었습니다.

2. **WebSocket 프로토콜**: WebSocket은 웹 브라우저와 서버 간에 실시간 양방향 통신을 가능하게 하는 프로토콜입니다. 이 프로젝트에서 Node.js 서버는 WebSocket 서버로도 기능하며, TCP 서버로부터 받은 데이터를 웹 브라우저에 연결된 클라이언트들에게 실시간으로 전송합니다. WebSocket 연결을 통해 데이터는 거의 지연 없이 웹 브라우저에 전달되며, 이를 통해 사용자는 데이터의 변화를 거의 실시간으로 시각화된 형태로 볼 수 있습니다.
   
##### Receiving Data and Delivering it to the Web Browser

1. **Node.js Server**: This server serves as both a TCP server and a WebSocket server. First, the TCP server receives data from the DCS game. After receiving the data, it processes it and is designed to provide information simultaneously to multiple clients.

2. **WebSocket Protocol**: WebSocket is a protocol that enables real-time, bidirectional communication between a web browser and a server. In this project, the Node.js server also functions as a WebSocket server, transmitting data received from the TCP server to connected web browser clients in real time. The data is delivered to the web browser with minimal latency, allowing users to visualize changes almost instantly.

![구성도](https://goraniworks.github.io/assets/images/favicon/DCS01.png)

#### [실행하는 법](#실행하는-법)

1. DCS 게임 데이터 추출 설정
DCS (Digital Combat Simulator) 게임에서 필요한 비행 데이터를 추출하기 위해 Lua 스크립트를 사용합니다. 이 스크립트는 게임 내에서 발생하는 데이터를 실시간으로 추출하여 TCP 서버로 전송합니다.

Lua 스크립트 설정:
파일 수정: C:\Users\[YourUserName]\Saved Games\DCS\Scripts\Export.lua 파일을 만들고, 제공된 스크립트 코드를 복사하여 붙여넣습니다. 스크립트에서 네트워킹 기능은 모두 게임에 구현이 되어있습니다. 게임의 미션이 실행 할때 마다 이 파일을 자동으로 읽고 실행합니다. 그냥 위치에 파일을 복사만 해 두면 됩니다. 

2. Node.js 서버 설정
이 프로젝트는 Node.js를 기반으로 한 WebSocket 서버를 통해 웹 브라우저로 데이터를 전송합니다. Node.js와 필요한 라이브러리 설치 후, 서버 스크립트를 설정합니다.
이 웹서버에 대한 내용은 방대함으로 실행하는 방법만 적습니다. 웹서버에 대한 경험이 없다면 꽤나 힘들 수가 있습니다.
server.js 파일에 대한 내용은 아래에 있습니다. 중요한것은 포트번호를 LUA스크립트와 HTML 파일과 맞추는 겁니다. 

#### [How to Run](#how-to-run)

1. DCS Game Data Extraction Settings
Use Lua scripts to extract necessary flight data from the DCS (Digital Combat Simulator) game. This script extracts data generated within the game in real time and sends it to a TCP server.

Lua Script Setup:
File Modification: Create a file named `C:\Users\[YourUserName]\Saved Games\DCS\Scripts\Export.lua` and copy the provided script code into it. The script will be automatically read and executed whenever the game's mission is run. Just copying the file to the specified location is sufficient.

2. Node.js Server Setup
This project uses a WebSocket server based on Node.js to transmit data to a web browser. After installing Node.js and the necessary libraries, configure the server script.
The content about the web server is vast, so only the execution method is described. It can be quite challenging if you have no experience with web servers.
The content of the server.js file is below. The important thing is to match the port numbers with the Lua script and HTML file.

```
게임에서 -> node.js 서버로 
TCP 서버 포트 = LUA스크립트 포트

node.js 서버에서 -> HTML(웹브라우저)로
WebSocket 포트 =  HTML파일 포트

From the game -> to the node.js server
TCP server port = LUA script port

From the node.js server -> to HTML (web browser)
WebSocket port = HTML file port
```

이 두가지를 일치 시키는 것이 가장 중요합니다.

Node.js 설치 및 서버 스크립트 실행:
Node.js 설치: Node.js 공식 웹사이트에서 Node.js를 다운로드하고 설치합니다.
필요한 라이브러리 설치: 프로젝트 폴더에서 터미널을 열고 npm install ws net 명령어를 실행하여 필요한 Node.js 라이브러리를 설치합니다.
서버 스크립트 실행: 터미널에서 node server.js 명령을 실행하여 WebSocket과 TCP 서버를 시작합니다.

Matching these two is the most important thing.

Node.js Installation and Server Script Execution:
Node.js Installation: Download and install Node.js from the official Node.js website.
Install Required Libraries: Open a terminal in the project folder and run the command `npm install ws net` to install the necessary Node.js libraries.
Run the Server Script: Execute the WebSocket and TCP server by running the command `node server.js` in the terminal.

3. 웹 클라이언트 설정
웹 클라이언트는 일반적으로 HTML, CSS, JavaScript로 구성되어 있으며, 웹소켓을 통해 서버로부터 데이터를 받아 사용자 인터페이스에 표시합니다. 이 프로젝트에서는 html 파일 하나에 HTML, CSS, JavaScript 를 모두 집어넣었고, 그냥 윈도우에서 더블 클릭해서 웹브라우저만 띄우면 됩니다. 중요한건 포트번호를 웹서버와 맞추는 겁니다.

3. Web Client Setup
The web client is typically composed of HTML, CSS, and JavaScript, receiving data from the server via WebSocket and displaying it in the user interface. In this project, everything is included in one HTML file. Just double-click the file to open it in a web browser. Ensure the port numbers match the web server.

Web Client Execution:
Prepare the Web File: Refer to the file below to compose the `index.html` file. 
Double-clicking it will run it in the web browser. Once the server starts operating, it will start moving automatically.

Final Check
After completing all the settings, run the DCS game, ensure the Node.js server is running, and the web client page is open. Check if the data is correctly displayed. The data should be reflected in real time on the web page's dashboard.

웹 클라이언트 실행:
웹 파일 준비: index.html 파일에 아래에 있는 파일을 참고하여 작섭합니다. 
작성하고 더블클릭하면 웹브라우저에 실행됩니다. 서버가 작동하기 시작하면 자동으로 움직이기 시작할 겁니다. 

최종 점검
모든 설정이 완료된 후, DCS 게임을 실행하고, Node.js 서버가 실행 중이며, 웹 클라이언트 페이지가 열려 있는 상태에서 데이터가 정상적으로 표시되는지 확인합니다. 데이터는 실시간으로 웹 페이지의 계기판에 반영되어야 합니다.

#### [코드 설명](#코드-설명)

1. **Lua Export Script**: DCS 게임의 데이터를 수집하고 TCP 서버로 전송합니다. 이 스크립트는 게임의 프레임마다 비행기의 속도, 고도, 피치, 롤 등의 데이터를 서버로 보냅니다. 게임 폴더내에 게임 회사에서 예시로 작성해놓은 파일이 있습니다. 이걸 수정하여 사용합니다. 이 파일은 Export.lua 라는 이름으로 저장하여 $HOME\Saved Games\DCS\Scripts\Export.lua 이 위치에 옮겨 놓으면 됩니다. 함수 3개만 수정하면 됩니다. 여기서 주의할 점은 포트를 정확하게 서버쪽과 일치시켜야 한다는 점입니다. 

#### [Code Explanation](#code-explanation)

1. **Lua Export Script**: Collects data from the DCS game and sends it to a TCP server. This script sends data such as speed, altitude, pitch, and roll of the aircraft to the server for each frame of the game. There is a sample file provided by the game company within the game folder, which can be modified for use. Save this file as `Export.lua` and move it to `$HOME\Saved Games\DCS\Scripts\`. Only three functions need to be modified. It is crucial to ensure the ports match accurately with the server side.

```lua

function LuaExportStart()
    package.path  = package.path..";"..lfs.currentdir().."/LuaSocket/?.lua"
    package.cpath = package.cpath..";"..lfs.currentdir().."/LuaSocket/?.dll"
    socket = require("socket")
    host = host or "localhost"
    
    port = port or 12345
    -- 이 포트 를 수정하라.
    connection = socket.try(socket.connect(host, port))
    connection:setoption("tcp-nodelay", true)
end

function LuaExportAfterNextFrame()
    -- Works just after every simulation frame.
    
    -- Call Lo*() functions to get data from Lock On here.
    -- For example:
        local IAS = LoGetIndicatedAirSpeed()
        local t = LoGetModelTime()
        local name = LoGetPilotName()
        local altBar = LoGetAltitudeAboveSeaLevel()
        local altRad = LoGetAltitudeAboveGroundLevel()
        local pitch, bank, yaw = LoGetADIPitchBankYaw()
        local engine = LoGetEngineInfo()
        local HSI    = LoGetControlPanel_HSI()
    -- Then send data to your file or to your receiving program:
    -- 1) File
    -- if default_output_file then
    --	  default_output_file:write(string.format("t = %.2f, name = %s, altBar = %.2f, altRad = %.2f, pitch = %.2f, bank = %.2f, yaw = %.2f\n", t, name, altBar, altRad, 57.3*pitch, 57.3*bank, 57.3*yaw))
    --	  default_output_file:write(string.format("t = %.2f ,RPM left = %f  fuel_internal = %f \n",t,engine.RPM.left,engine.fuel_internal))
    --	  default_output_file:write(string.format("ADF = %f  RMI = %f\n ",57.3*HSI.ADF,57.3*HSI.RMI))
    --	end
    -- 2) Socket
        socket.try(connection:send(string.format("IAS = %.2f, t = %.2f, name = %s, altBar = %.2f, alrRad = %.2f, pitch = %.2f, bank = %.2f, yaw = %.2f\n", IAS, t, name, altRad, altBar, pitch, bank, yaw)))
    
    end

function LuaExportStop()
    -- 종료 시 소켓 닫기
    if connection then
        connection:close()
    end
end

```

2. **Node.js 서버**: TCP 포트와 WebSocket 포트를 이용해 두 개의 서버를 구성합니다. TCP 서버는 DCS로부터 데이터를 받고, 이 데이터를 모든 연결된 WebSocket 클라이언트에게 전송합니다.

 **Node.js Server**: Configures two servers using TCP and WebSocket ports. The TCP server receives data from DCS and sends it to all connected WebSocket clients.

```javascript
const WebSocket = require('ws');
const net = require('net');

const WEB_SOCKET_PORT = 12346; // WebSocket 포트
const TCP_PORT = 12345;        // TCP 서버 포트
    -- 이 포트 를 수정하라.

// 게임 스크립트는 여기에 있다. C:\Users\(username)\Saved Games\DCS\Scripts

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
```

3. **HTML & JavaScript**: 웹 페이지는 WebSocket을 통해 서버로부터 데이터를 수신하고, 이를 가지고 SVG 요소를 동적으로 조정하여 계기판처럼 표현합니다. 예를 들어, `IAS` 값에 따라 삼각형 모양의 속도계가 회전합니다.

 **HTML & JavaScript**: The web page receives data from the server via WebSocket and dynamically adjusts SVG elements to represent a dashboard. For example, the triangle speedometer rotates based on the IAS value.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket 테스트</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #panel {
            display: flex;
            justify-content: center; /* Center the single gauge */
            margin-top: 20px;
        }
        .gauge-container {
            position: relative;
            width: 100px;
            height: 100px;
            margin: 10px;
        }
        .gauge {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 2; /* Ensure the SVG is above the image */
            transform-origin: center; /* Set the rotation center to the middle of the SVG */
        }
        #ias-info {
            text-align: center;
            margin-top: 110px; /* Adjust as needed */
        }
        #messages {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            min-height: 50px;
        }
        .background-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1; /* Place image below the SVG */
        }
    </style>
</head>
<body>
    <h1>WebSocket을 통한 서버 데이터 수신</h1>
    <div id="panel">
        <div class="gauge-container">
            <img src="circle.png" class="background-image" alt="Background Image">
            <!-- Adjust the polygon points to ensure it's centered correctly -->
            <svg id="ias" class="gauge" viewBox="0 0 100 100"><polygon points="50,30 30,70 70,70" fill="red"></polygon></svg>
            <div id="ias-info" class="info"></div>
        </div>
    </div>
    <div id="messages"></div>
    <script>
        const messages = document.getElementById('messages');
        const ws = new WebSocket('ws://localhost:12346');

        ws.onopen = function() {
            console.log('서버에 연결되었습니다.');
            messages.textContent = '서버에 연결되었습니다...';
        };

        ws.onmessage = function(event) {
            console.log('서버로부터 메시지 수신:', event.data);
            const data = event.data;
            const parts = data.split(', ').map(part => {
                const pair = part.split(' = ');
                return {key: pair[0], value: parseFloat(pair[1])};
            });
            const dataMap = Object.fromEntries(parts.map(part => [part.key, part.value]));

            updateGauges(dataMap);
        };

        ws.onerror = function(error) {
            console.log('WebSocket 오류:', error);
            messages.textContent = 'WebSocket 연결 오류 발생!';
        };

        ws.onclose = function() {
            console.log('서버와의 연결이 종료되었습니다.');
            messages.textContent += '\\n서버와의 연결이 종료되었습니다.';
        };

        function updateGauges(data) {
            const iasAngle = (30/28) * data.IAS; // Calculate the angle based on IAS value
            document.getElementById('ias').style.transform = `rotate(${iasAngle}deg)`; // Rotate without translation
            document.getElementById('ias-info').textContent = `IAS: ${data.IAS}, 각도: ${iasAngle.toFixed(2)}°`;
        }
    </script>
</body>
</html>
```

#### [프로젝트의 의의](#프로젝트의-의의)

이 프로젝트는 게임 데이터를 활용하는 새로운 방법을 탐색합니다. 실시간 데이터를 웹 페이지에 표현함으로써, 사용자는 게임 외부에서도 중요한 게임 정보를 실시간으로 확인할 수 있게 됩니다. 게임 데이터를 웹 페이지로 전송하고 실시간으로 시각화함으로써, 사용자는 게임 외부에서도 중요한 정보를 모니터링하고, 다양한 사용자 정의 기능을 개발할 수 있습니다. 이는 게임 스트리밍, 원격 모니터링 또는 트레이닝 도구로 활용될 수 있으며, 게임과 외부 시스템 간의 상호 작용 가능성을 확장합니다. 

#### [Significance of the Project](#significance-of-the-project)
This project explores new ways to utilize game data. By displaying real-time data on a web page, users can monitor important game information outside the game in real time. By transmitting game data to a web page and visualizing it in real time, users can monitor critical information and develop various custom functions outside the game. This can be used for game streaming, remote monitoring, or training tools, expanding the possibilities for interaction between the game and external systems.

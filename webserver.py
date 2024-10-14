import socket
import sys
import mimetypes

defaultServerIP = '127.0.0.1'
defaultServerPort = 28333

if (len(sys.argv) > 1):
    serverPort = int(sys.argv[1])
else:
    print(f'no port specified! setting server port to default(port {defaultServerPort})')
    serverPort = defaultServerPort
serverIP = defaultServerIP

s = socket.socket()
serverAddress = (serverIP,serverPort)
s.bind(serverAddress)
s.listen()


print(f'Server is listening on {serverIP}:{serverPort}')

while True:
    clientSocket, clientAddress = s.accept()
    request_data = clientSocket.recv(1024)
    
    if b'\r\n\r\n' in request_data:
        request_line = request_data.decode('ISO-8859-1').splitlines()[0]
        method, path, protocol = request_line.split(" ")
        mime_type, _ = mimetypes.guess_type(path)

        try:
            with open(path[1:], "r") as fp:
                data = fp.read()
            response = f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type or 'text/plain'}\r\n\r\n{data}"
        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>"

        clientSocket.sendall(response.encode("ISO-8859-1"))

    clientSocket.shutdown(socket.SHUT_RDWR)
    clientSocket.close()





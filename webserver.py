import socket
import sys

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
    print(f'Connection recieved from {clientAddress[0]}:{clientAddress[1]}')

    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 23\r\n"
        "\r\n"
        "Bro is not the client\r\n\r\n"
    )
    clientSocket.sendall(http_response.encode("utf-8"))
    clientSocket.shutdown(socket.SHUT_RDWR)  # Shutdown the connection properly
    clientSocket.close()
    # clientSocket.close()
          





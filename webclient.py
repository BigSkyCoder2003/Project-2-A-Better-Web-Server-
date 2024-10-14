import sys
import socket

defaultWebAddress = '127.0.0.1'
defaultRemotePort = 28333

if (len(sys.argv)== 3) :
    webAddress = sys.argv[1]
    remotePort = int(sys.argv[2])
elif (len(sys.argv) == 2):
    print(f'No port specified! using Default port ({defaultRemotePort})\n')
    webAddress = sys.argv[1]
    remotePort = defaultRemotePort
else:
    print("Wrong or no arguements given! Default port and web address selected!\n")
    webAddress = defaultWebAddress
    remotePort = defaultRemotePort




s=socket.socket()

remote = (webAddress,remotePort)
file_name ="file1.txt"

s.connect(remote)

request = f"GET /{file_name} HTTP/1.1\r\nHost: {webAddress}\r\nConnection: close\r\n\r\n"
s.sendall(request.encode())


while(data := s.recv(100)) != b'':
    data = data.decode("utf-8")
    print(data, end="")
    if not data:
        print("end")
        # x = False
        break
s.close()
        



        
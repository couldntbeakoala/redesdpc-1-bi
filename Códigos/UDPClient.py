from socket import *
serverName = "HOSTIP"
serverPort = HOSTPORT
addr = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode('utf-8'), addr)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()
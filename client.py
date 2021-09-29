import socket

# once the client requests, we need to accept it:
server = socket.gethostname()
port = 45678

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# because we are the client we need to connect to to a listening server
client_socket.connect((server, port))

# get some string as input
message_to_send = "Player 1 is here!"

# send the message
client_socket.sendall(bytes(message_to_send, "utf-8"))

# get a response
received_message = client_socket.recv(1024)

# print the decoded message
print(received_message.decode("utf-8"))

client_socket.close()
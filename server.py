import socket

server = socket.gethostname()
port = 45678

# create a streaming socket socket over IPv4:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to listen
try:
    server_socket.bind((server, port))
except socket.error as e:
    str(e)

# Listen for connections
server_socket.listen(1)



while True:
    # once the client requests, we need to accept it:
    connection, address = server_socket.accept()
    print(f"Connection from {address} has been established")

    connection.send("Welcome to Snowman!", "utf-8")

    # receive some data
    data = connection.recv(1024)

    # if it's blank, break the loop
    if not data:
        break

    # otherwise print it to screen
    print(repr(data).strip("b'"))

    # and then bounce it back to the client in uppercase
    connection.sendall(data.upper())

    

server_socket.close()
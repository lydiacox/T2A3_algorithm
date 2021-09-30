from snowperson import Snow
import socket

class SnowmanServer():
    '''A server to play the game Snowman
    '''
    def __init__(self):

        self.server = socket.gethostname()
        self.port = 45678

        # create a streaming socket socket over IPv4:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind to listen
        try:
            self.server_socket.bind((self.server, self.port))
        except socket.error as e:
            str(e)

    # Listen for connections
    def server_listen(self):
        self.server_socket.listen(1)

    # once the client requests, we need to accept it:
    def connect_server(self):
        self.connection, self.address = self.server_socket.accept()
        print(f"Connection from {self.address} has been established")


    def close_server(self):
        self.server_socket.close()

    def send_game(self):

        while True:
            self.connection.send(bytes("Welcome to Snowman!", "utf-8"))

            # receive some data
            data = self.connection.recv(1024)
            print(data)

            # if it's blank, break the loop
            if not data:
                break

            # otherwise print it to screen
            print("some text here")

            # and then bounce it back to the client in uppercase
            # self.connection.sendall(data.upper())

    

play_game = SnowmanServer()

play_game.server_listen()
play_game.connect_server()
play_game.send_game()
play_game.close_server()
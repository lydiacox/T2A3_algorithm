import socket
import classes

class Wizard_Server():
    '''A server to host the Wizard Book Shopping Extravaganza Experience!
    ...
    Running through the list of five Wizarding Books, the customer will have an
    opportunity to specify how many copies of each book they wish to purchase.

    Attributes
    ----------
    

    Methods
    -------
    server_listen
    connect_server
    close_server
    send_game

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
            self.connection.send(bytes("Shut up and take my money!", "utf-8"))

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

    

lets_shop = Wizard_Server()

lets_shop.server_listen()
lets_shop.connect_server()
lets_shop.send_game()
lets_shop.close_server()
import socket

class Client():
    '''A client to purchase books in the Wizarding Series.
    ...
    Methods
    -------
    buy_books
    close_client
    '''
    def __init__(self, port):
        # once the client requests, we need to accept it:
        self.server = socket.gethostname()
        self.port = port

        # create socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # because we are the client we need to connect to to a listening server
        self.client_socket.connect((self.server, self.port))

    def buy_books(self):
        for i in range (6):
            received_message = self.client_socket.recv(1024).decode("utf-8")
            if "How " in received_message:
                try:
                    no_of_books = False
                    while no_of_books is False:
                        no_of_books = input(received_message)
                        try:
                            no_of_books = int(no_of_books)
                            if no_of_books < 0:
                                print("Please see the service desk for returns.")
                                no_of_books = False
                        except ValueError:
                            print("Please enter the number of copies of this book you wish to buy.")
                            no_of_books = False
                except KeyboardInterrupt:
                    print("\nThank you for shopping at Blourish and Flotts!")
                    exit()
                message_to_send = str(no_of_books)
                self.client_socket.sendall(bytes(message_to_send, "utf-8"))
            else:
                print(received_message)  

    def close_client(self):
        self.client_socket.close()


class Wizard_Server():
    '''A server to host the Wizard Book Shopping Extravaganza Experience!
    ...
    Running through the list of five Wizarding Books, the customer will have an
    opportunity to specify how many copies of each book they wish to purchase.

    Methods
    -------
    server_listen
    connect_server
    close_server
    sell_books
    '''
    def __init__(self, port):
        self.port = port
        self.server = socket.gethostname()

        # create a streaming socket socket over IPv4:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind to listen
        try:
            self.server_socket.bind((self.server, self.port))
        except socket.error as e:
            str(e)

    # Listen for connections
    def server_listen(self):
        self.server_socket.listen()

    # once the client requests, we need to accept it:
    def connect_server(self):
        self.connection, self.address = self.server_socket.accept()
        print(f"Connection from {self.address} has been established")

    def close_server(self):
        self.server_socket.close()

    def sell_books(self):
        while True:
            shop = Shopping_list()
            self.connection.send(bytes(shop.welcome_message, "utf-8"))
            shop.get_list(self.connection)
            shop_list = shop.shopping_list
            full_price = shop.no_discount(shop_list)
            sets = shop.sets_of_books(shop_list)
            discounted = shop.discounted_price(sets)
            discounted_decimal = "{:.2f}".format(discounted)
            price = shop.print_price(full_price, discounted)
            self.connection.send(bytes(price, "utf-8"))
            print(f"The customer wishes to buy {sets}. Total price is €{discounted_decimal}.")
            break


class Shopping_list():
    '''
    A class to ask the customer what they would like to buy
    ...
    Running through the list of five Wizarding Books, the customer will have an
    opportunity to specify how many copies of each book they wish to purchase.

    Attributes
    ----------
    shopping_list : list
        A list of the books the customer wishes to purchase.

    Methods
    -------
    get_list :
        A function to iterate through the list of books available for purchase
        and get inputs from the customer.'
    no_discount :
        A function to calculate the total cost of the books with no discounts
        applied.
    sets_of_books :
        A function to break up the list of books into sets of books.
    discounted_price :
        A function to calculate the cost of the books with any discount(s)
        applied.
    print_price :
        A function to display the cost of the books and any discount received.
    '''

    def __init__(self):
        self.shopping_list = []
        self.welcome_message = f"""Welcome to Blourish and Flotts!\nThere are five books in the Wizarding Series, and the more books\nin the series you buy, the bigger your discount!\nEach book costs €8, but buy a set of books in the series\nfor a discount!\nTwo books: 5% discount\nThree books: 10% discount\nFour books:  20% discount\nFive books: 25% discount!!!\n"""
        self.books = ['The Coder\'s Algorithm', 
                      'The Chamber of Stack Overflow',
                      'The Prisoner of Infinite Loops', 'The Goblet of Coffee',
                      'The Order of Control Flow']

    def get_list(self, client_socket):
        for book in self.books:
            client_socket.send(bytes(f"How many copies of {book} do you want to buy?: \n", "utf-8"))
            how_many = client_socket.recv(1024).decode("utf-8")
            how_many = int(float(how_many))
            for i in range(how_many):
                self.shopping_list.append(book)

    def no_discount(self, shop_list):
        return len(shop_list) * 8

    def sets_of_books(self, shop_list):
        # An empty list, to be filled with more lists of the sets of books
        all_groups = []
        while shop_list:
            # Convert the shopping list to a set, so that it contains only
            # unique values
            shop_set = set(shop_list)
            # A temporary list, to be reset every time the loop runs
            this_group = []
            for book in shop_set:
                this_group.append(book)
                shop_list.remove(book)
            # Once the loop has iterated through every book in the set, add
            # the temporary list to the all_groups list
            else:
                all_groups.append(this_group)
        return all_groups

    def discounted_price(self, all_groups):
        costs_per_set = {
            1: 8,
            2: 15.2,
            3: 21.6,
            4: 25.6,
            5: 30
        }
        cost = 0
        # A loop to iterate through the list of sets of books
        for s in all_groups:
            # The length of the set corresponds with the key in the dictionary.
            # The value is the cost of the set, and is added to the total cost.
            cost += costs_per_set[len(s)]
        return cost

    def print_price(self, full_price, discounted):
        discounted_price = "{:.2f}".format(discounted)
        difference = full_price - discounted
        difference_decimal = "{:.2f}".format(difference)
        message = f"Accio price! Your total is €{discounted_price}."
        if difference:
            message += f"\nMerlin's beard! You've saved €{difference_decimal}."
        else:
            message += "\nBuy more books in the set next time! You could have saved Galleons!"
        return message

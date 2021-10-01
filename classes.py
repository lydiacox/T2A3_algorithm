import socket

class Client():
    '''A client to purchase books in the Wizarding Series.
    ...
    Methods
    -------
    close_client
    '''
    def __init__(self):
        # once the client requests, we need to accept it:
        self.server = socket.gethostname()
        self.port = 45678

        # create socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # because we are the client we need to connect to to a listening server
        self.client_socket.connect((self.server, self.port))

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
        self.server_socket.listen()

    # once the client requests, we need to accept it:
    def connect_server(self):
        self.connection, self.address = self.server_socket.accept()
        print(f"Connection from {self.address} has been established")


    def close_server(self):
        self.server_socket.close()

    def send_game(self):

        while True:
            self.connection.send(bytes(Shopping_list().welcome_message, "utf-8"))

            # receive some data
            data = self.connection.recv(1024).decode("utf-8")
            print(data)

            # if it's blank, break the loop
            if not data:
                break

            shop_list = Shopping_list()

            shop_list.get_list(self.connection)

            # and then bounce it back to the client in uppercase
            self.connection.sendall(data.upper())

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
    get_list : A function to iterate through the list of books available
               for purchase and get inputs from the customer.

    '''

    welcome_message = f"""Welcome to Blourish and Flotts!
        \nThere are five books in the wizarding series, and the more books in 
        the series you buy, the bigger your discount!\nEach book costs €8, 
        but if you buy two different books in the series, you get a 5% 
        discount. Buy three different books in the series, and get a 10% 
        discount. Buy 4 different books in the series for a 20% discount, 
        and for a full 25% discount, buy all five books in the series!"""

    def __init__(self):
        self.shopping_list = []
        self.books = ['The Coder\'s Algorithm', 
                      'The Chamber of Stack Overflow',
                      'The Prisoner of Infinite Loops', 'The Goblet of Coffee',
                      'The Order of Control Flow']

    def get_list(self, client_socket):

        for book in self.books:
            client_socket.send(bytes(f"""How many copies of {book} do you want 
            to buy?: """, "utf-8"))
            how_many = client_socket.recv(1024).decode("utf-8")
            how_many = int(how_many)
            if how_many == 0:
                break
            for i in range(how_many):
                self.shopping_list.append(book)


class Sets_of_Books():
    '''A class to determine how many sets of books are being purchased
    ...

    Attributes
    ----------
    shop_list : list
        A list of books the customer wishes to purchase

    Methods
    -------
    convert : A function to convert the list of all books to be purchased
              into a list of sets of books to be purchased.
    '''

    def __init__(self, shop_list):

        # An empty list, to be filled with more lists of the sets of books
        self.all_groups = []
        self.shop_list = shop_list

    # A loop to run while there are still books on the shopping list
    def convert(self):
        while self.shop_list:
            # Convert the shopping list to a set, so that it contains only
            # unique values
            shop_set = set(self.shop_list)
        # A temporary list, to be reset every time the loop runs
        this_group = []
        for book in shop_set:
            this_group.append(book)
            self.shop_list.remove(book)
        # Once the loop has iterated through every book in the set, add
        # the temporary list to the all_groups list
        else:
            self.all_groups.append(this_group)


class Calc_No_Discount():
    '''
    A class to calculate the cost of all the books at full price.

    '''
    def __init__(self, shop_list):
        self.cost = len(shop_list) * 8


class With_Discount():
    '''
    A class to calculate the cost of all the books with any discount(s)
    applied.
    ...

    Attributes
    ----------
    costs_per_set : dict
        A dictionary with the cost of a set of books, as values, and the number
        of books in the set as keys.

    '''
    costs_per_set = {
        1: 8,
        2: 15.2,
        3: 21.6,
        4: 25.6,
        5: 30
    }

    def __init__(self, sets_of_books):
        self.cost = 0
        # A loop to iterate through the list of sets of books
        for s in sets_of_books:
            # The length of the set corresponds with the key in the dictionary.
            # The value is the cost of the set, and is added to the total cost.
            self.cost += self.costs_per_set[len(s)]


class Print_Price():
    '''
    A class to print the price of the customer's purchase and any
    discount applied.
    ...

    Attributes
    ----------
    full_price : float
        The cost of all the books if they were charged at €8 each.
    discounted : float
        The cost of all the books with the discount(s) applied.

    Methods
    -------
    print_price : A function to print a statement showing the
    total cost and any savings, if applicable.

    '''
    def __init__(self, full_price, discounted):
        self.full_price = full_price
        self.discounted = "{:.2f}".format(discounted)
        self.difference = "{:.2f}".format(full_price - discounted)

    def print_price(self):
        print(f"Accio price! Your total is €{self.discounted}.")
        if self.difference:
            print(f"Merlin's beard! You've saved €{self.difference}.")
        else:
            print("Buy more books in the set next time! You could have saved Galleons!")

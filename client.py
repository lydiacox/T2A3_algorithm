import classes

buy_books = classes.Client()

# get a response
while True:
    received_message = buy_books.client_socket.recv(1024)

    # print the decoded message
    print(received_message.decode("utf-8"))

    message_to_send = "The buyer is here!"

    # send the message
    buy_books.client_socket.sendall(bytes(message_to_send, "utf-8"))

    break

buy_books.close_client()

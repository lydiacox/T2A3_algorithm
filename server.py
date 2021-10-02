import classes
import sys

if len(sys.argv) > 1:
    port = sys.argv[1]
else:
    port = 45678

make_bread = classes.Wizard_Server(port)

make_bread.server_listen()
make_bread.connect_server()
book_list = make_bread.sell_books()
convert_list = classes.Sets_of_Books(book_list)
make_bread.close_server()
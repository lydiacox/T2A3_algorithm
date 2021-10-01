import classes
import sys

if len(sys.argv) > 1:
    port = sys.argv[1]
else:
    port = 45678

buy_books = classes.Client(port)
buy_books.buy_books()
buy_books.close_client()

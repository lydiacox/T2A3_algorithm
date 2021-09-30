def shopping_list():
    '''A function to ask the customer what they would like to buy
    
    Returns:
        A list of all the books the customer wishes to purchase.
    '''
    print(f"Welcome to Blourish and Flotts!\nThere are five books in the wizarding series, and the more books in the series you buy, the bigger your discount!\nEach book costs €8, but if you buy two different books in the series, you get a 5% discount. Buy three different books in the series, and get a 10% discount. Buy 4 different books in the series for a 20% discount, and for a full 25% discount, buy all five books in the series!")

    books = ['The Coder\'s Algorithm', 'The Chamber of Stack Overflow', 'The Prisoner of Infinite Loops', 'The Goblet of Coffee', 'The Order of Control Flow']

    shopping_list = []

    for book in books:
        try:
            how_many = False
            while not how_many:
                how_many = input(f"How many copies of {book} do you want to buy?: ")
                try:
                    how_many = int(how_many)
                    if how_many < 0:
                        print("Please see the service desk for returns.")
                        how_many = False
                    elif how_many == 0:
                        break
                    for i in range(how_many):
                        shopping_list.append(book)
                except ValueError:
                    print("Please enter the number of copies of this book you wish to buy.")
                    how_many = False 
        except KeyboardInterrupt:
            print("\nThank you for shopping at Blourish and Flotts!")
            exit()
    
    return shopping_list

def sets_of_books(shop_list):
    '''A function to determine how many sets of books are being purchased
    
    Args:
        shop_list: A list of books the customer wishes to purchase
        
    Returns:
        A list of lists of unique books from the shopping list
    '''
    
    # An empty list, to be filled with more lists of the sets of books
    all_groups = []
    
    # A loop to run while there are still books on the shopping list
    while shop_list:
        # Convert the shopping list to a set, so that it contains only unique values
        shop_set = set(shop_list)
        # A temporary list, to be reset every time the loop runs
        this_group = []
        for book in shop_set:
            this_group.append(book)
            shop_list.remove(book)
        # Once the loop has iterated through every book in the set, add the temporary list to the all_groups list
        else:
            all_groups.append(this_group)
    
    return all_groups

def calculate_undiscounted_total(shop_list):
    '''A function to calculate the cost of all the books at full price
    Args:
        shop_list: A list of books the customer wishes to purchase.
    Returns:
        The total cost of the books with no discounts applied.
    '''
    return len(shop_list) * 8

def calculate_discounted_total(sets_of_books):
    '''A function to calculate the price for each set of books
    Args:
        shop_list: A list of books the customer wishes to purchase
    Returns:
        The total cost of the books with the discount(s) applied
    '''
    # A dictionary with the cost of a set of books
    costs_per_set = {
        1: 8,
        2: 15.2,
        3: 21.6,
        4: 25.6,
        5: 30
    }

    cost = 0
    
    # A loop to iterate through the list of sets of books
    for s in sets_of_books:
        # The length of the set corresponds with the key in the dictionary. The value is the cost of that set, and is added to the total cost.
        cost += costs_per_set[len(s)]

    return cost

def print_price(full_price, discounted):
    '''A function to print the price of the customer's purchase and any discount applied.
    Args:
        full_price:
            The cost of all the books if they were charged at €8 each.
        discounted:
            The cost of all the books with the discount(s) applied.
    Returns:
        A printed statement showing the total cost and any savings, if applicable.
    
    '''
    discounted_decimal = "{:.2f}".format(discounted)
    difference = full_price - discounted
    difference_decimal = "{:.2f}".format(difference)
    print(f"Accio price! Your total is €{discounted_decimal}.")
    if difference:
        print(f"Merlin's beard! You've saved €{difference_decimal}.")
    else:
        print("Buy more books in the set next time! You could have saved Galleons!")

shop_list = shopping_list()
full_price = calculate_undiscounted_total(shop_list)
sets = sets_of_books(shop_list)
discounted = calculate_discounted_total(sets)
print_price(full_price, discounted)
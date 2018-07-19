Property_Names = "Name Price Stock Sold Order"; # Row Headers for all Tables 

# A tuple of tuples for each Category.
# Category tuples identify a Category and its items 
All_Items = (("Category Food", "Egg ", "Bean", "Cake", "Chip"),
             ("Category Bits", "Sock", "Tie ", "Shoe"),
             ("Category Toys", "Car ", "Bear", "Doll", "Book", "Ball"));

Properties = { "Egg ":" 0.99 64 86 93",    # A Dictionary for all items 
               "Book":" 4.99 326 390 400", # and their properties. 
               "Sock":" 1.11 343 456 297",
               "Cake":" 2.73 229 436 144", # Item Names are acess Keys 
               "Ball":" 2.99 124 133 149", # Item Properties are Keyed Values 
               "Bean":" 0.34 897 992 931",
               "Bear":" 7.88 90 87 74",    # Note the order of Items can 
               "Tie ":" 3.11 257 201 222", # be random (as here). 
               "Doll":" 3.99 42 50 63",
               "Chip":" 0.55 604 451 557", # The order is not relevant 
               "Shoe":" 5.44 744 660 629", # in most Dictionaries. 
               "Car ":" 3.21 214 113 121",};

for Category_Items in All_Items: # For each Category tuple, 
    for Item in Category_Items:  # Consider each Item in turn. 
        if "Category" in Item: # If this element identifies the Category, 
            print "Table for the " + Item; # use it to make Table Title, 
            print Property_Names;          # and print a Header Row. 
        else:                        # If this element identifies the Item, 
            print Item + " " + Properties[Item]; # print the Item Name. 
                                                 # followed by its Properties. 
    print; # Print an empty line between Tables. 

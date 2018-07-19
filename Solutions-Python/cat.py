Property_Names = "Name    Price   Stock   Sold    Order";

All_Items = (("Category Food", "Egg ", "Bean", "Cake", "Chip"),
                  ("Category Bits", "Sock", "Tie ", "Shoe"),
                  ("Category Toys", "Car ", "Bear", "Doll", "Book", "Ball"));

Properties = {"Egg ":"  0.99      64     86      93",
              "Bean":"  0.34     897    992     931",
              "Sock":"  1.11     343    456     297",
              "Cake":"  2.73     229    436     144",
              "Chip":"  0.55     604    451     557",
              "Ball":"  2.99     124    133     149",
              "Bear":"  7.88      90     87      74",
              "Tie ":"  3.11     257    201     222",
              "Shoe":"  5.44     744    660     629",
              "Doll":"  3.99      42     50      63",
              "Book":"  4.99     326    390     400",
              "Car ":"  3.21     214    113     121",};

for Category_Items in All_Items:
    for Item in Category_Items:
        if "Category" in Item:
            print "Table for the " + Item;
            print Property_Names;
        else:
            print Item + "   " + Properties[Item];
    print;

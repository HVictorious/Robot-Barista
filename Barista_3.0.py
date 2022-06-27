#Robot Barista
#@Author:Hunter Victorious

def  main_loop():



    print("Hello, welcome to the Cafe!!!!!!")

    name = input("What is your name?\n")

    #Verifies that you are not Evil Ben 
    if name == "Ben":
        evil_status = input("Are you Evil?\n")
        if evil_status.lower() == "yes":
            print("You're not welcome here Evil Ben!! Get out!!")
            exit()
        else:
            print("Oh, so you're one of those good Bens. Come on in!!")
    else:
        print("Hello " + name + ", thank you so much for coming in today.\n\n")
    import time
    time.sleep(2)

    #Input for different types of coffee
    menu_list = ["Black Coffee", "Espresso", "Latte", "Cappucino", "Frappuccino", "Dark Roast"]

    while True:
        order = input("What would you like from our menu today? Here is what we are serving.\n" + ('\n'.join(map(str, menu_list))) + "\n")
        try:
            if order in menu_list:
                break
            else:
                print("Please Try again!")
        except:
            continue

    if order == "Frappuccino":
        price_coffee = 5
    elif order == "Black Coffee":
        price_coffee = 2
    elif order == "Espresso":
        price_coffee = 6
    elif order == "Cuppucino":
        price_coffee = 4
    elif order == "Latte":
        price_coffee = 7
    elif order == "Dark Roast":
        price_coffee = 3

    #Input for different price and cost difference by price
    size_list = ["Small", "Medium", "Large"]

    while True:
        size = input("\n\n" + name + ",What size would you like\n" + ('\n'.join(map(str, size_list))) + "\n")
        try:
            if size in size_list:
                break
            else:
                print("Please Try again!")
        except:
            continue

    if size == "Small":  
        price = price_coffee + int(1)
    elif size == "Medium":
        price = price_coffee + int(2)
    elif size == "Large": 
        price = price_coffee + int(3)

    #Enables customer to be able to buy more than one item
    quantity = input("How many coffees would you like?\n")

    #Calculates sales tax

    tax = .08

    #Calculates all inputs and gives your total price
    coffee_total = price * int(quantity)

    tax_total = coffee_total * tax

    total = coffee_total + tax_total

    print("Thank you. Your total is: $" + str(total))

    #Function to pay cash or card 
    payment = input("\n\n" + "Will you be paying with Cash or Card today.\n")

    if payment == "Card":
        input("Please insert/swipe/tap card\n")
        print("Processing...........\n")
        import time
        time.sleep(6)
        print("Approved\n\n")
        input("Please Remove Card\n\n\n")
    if payment == "Cash":
        input("Please insert your cash into the bill accepter below and your change into the coin slot!\n\n\n\n")

    print("Thank you for coming to The Cafe " + name + ", we'll have that out for you in just one moment\n\n\n\n\n\n\n\n\n\n\n\n\n")

   
while True:
    main_loop()

    #Ends loop
    end = input("Type END to exit\n")
    if end.lower() == "end":
       break 

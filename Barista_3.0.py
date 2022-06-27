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
        valid_order = 0
        order = input("What would you like from our menu today? Here is what we are serving.\n" + ('\n'.join(map(str, menu_list))) + "\n")
        order = order.lower()
        try:
            for item in menu_list:
                if order == item.lower():
                    valid_order = 1
                    if order == "frappuccino":
                        price_coffee = 5
                    elif order == "black coffee":
                        price_coffee = 2
                    elif order == "espresso":
                        price_coffee = 6
                    elif order == "cuppucino":
                        price_coffee = 4
                    elif order == "latte":
                        price_coffee = 7
                    elif order == "dark roast":
                        price_coffee = 3 
        except:
            continue
        if valid_order == 1:
            break
        else:
            print(str(order) + " is not available, Try again")

            
        
        
    #Input for different price and cost difference by price
    size_list = ["Small", "Medium", "Large"]

    while True:
        valid_size = 0
        size = input("\n\n" + name + ",What size would you like\n" + ('\n'.join(map(str, size_list))) + "\n")
        size = size.lower()
        try:
            for item in size_list:
                if size == item.lower():
                    valid_size = 1
                    if size == "small":  
                        price = price_coffee + int(1)
                    elif size == "medium":
                        price = price_coffee + int(2)
                    elif size == "large": 
                        price = price_coffee + int(3)
        except:
            continue
        if valid_size == 1:
            break
        else:
            print(str(size) + " is not available, Try again")
       
  

    #Enables customer to be able to buy more than one item
    quantity = input("How many coffees would you like?\n")

    #Calculates sales tax

    tax = 0.08

    #Calculates all inputs and gives your total price
    coffee_total = price * int(quantity)

    tax_total = coffee_total * tax

    total = coffee_total + tax_total

    print("Thank you. Your total is: $" + str(total))

    #Calculates discount codes 
    discount_code = ["MILITARY10", "JuIcEr30"] 
        
    while True: 
        discount_entered = input("Do you have any discount codes you'd like to enter\n")
        discount_savings = 0
        if discount_entered.lower() == "no":
            break  
        elif discount_entered == discount_code[0]:
            discount_savings = total * 0.10 
            total = total - discount_savings
            
        elif discount_entered == discount_code[1]:
            discount_savings = total * 0.30 
            total = total - discount_savings
            
        print("You saved $" + str(round(discount_savings, 2)))
        
        print("Your new total is $" + str(round(total, 2)) + ".\n")
        
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

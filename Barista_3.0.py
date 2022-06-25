#Robot Barista
#@Author:Hunter Victorious

print("Hello, welcome to the Cafe!!!!!!")

name = input("What is your name?\n")

#Verifies that you are not Evil Ben 
if name == "Ben":
    evil_status = input("Are you Evil?\n")
    if evil_status == "Yes" or evil_status == "yes":
        print("You're not welcome here Evil Ben!! Get out!!")
        exit()
    else:
        print("Oh, so you're one of those good Bens. Come on in!!")
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n\n")

#Input for different types of coffee
menu_list = ["Black Coffee", "Espresso", "Latte", "Cappucino", "Frappuccino", "Dark Roast"]

while True:
    order = input(name + ",what would you like from our menu today? Here is what we are serving.\n" + ('\n'.join(map(str, menu_list))) + "\n")
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
    size = input(name + ",what would you like from our menu today? Here is what we are serving.\n" + ('\n'.join(map(str, size_list))) + "\n")
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

def percentage(part, whole):
    percentage = 100 * float(part)/float(whole)
    return str(percentage) + "%"

tax = str(percentage(8, 100))

#Calculates all inputs and gives your total price
coffee_total = price * int(quantity)

tax_total = coffee_total * str(tax)

total = str(coffee_total) 

print("Thank you. Your total is: $" + str(total))

print("Sounds good " + name + ", we'll have that out for you in just one moment\n\n\n\n")

#Keeps program open so you can see the last line 
end = input("Press 'Enter' KEY to end")

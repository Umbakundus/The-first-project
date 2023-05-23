from data import MENU
from data import resources

#functions
def admin_access(data):
    print(f"Actual value of ingredients: {data}")

def pricing(calculate):
    check = 0
    for index in calculate:
        count = MENU[index]["cost"]
        check += count
    return check

def payment():
    attempts = 3
    
    print("Please insert your payment card into the terminal!")
    while attempts > 0:
        pin = input("Please enter your 4-digit PIN Code: ")
        password = list(pin)
        if len(password) == 4: 
            print("Processing...", "The payment was successful", "Thank you for the order, have a nice day and Bon Apetit!", "Next customer please!", sep="\n")
            order.clear()
            core_function()
        else:
            attempts -= 1
            print(f"The password you've entered is too long or too short. Try again! You have {attempts} attempts left.")


        if attempts == 0:
            print("You have entered wrong PIN 3-times in row!", "Cancelling your order!", "Calling the cops!", "See u in prison scamer!", "Next customer please!", sep="\n")
            order.clear()
            core_function()
           
            
def consuption():
    return resources

def consuption_ingredients(pizza, ingredience):
    for keys, numbers in ingredience.items():
        for key, number in MENU[pizza]["ingredients"].items():
            if keys == key:
                ingredience[keys] = ingredience[keys] - MENU[pizza]["ingredients"][key]
    return ingredience
                
                
def calculate_ingredients(food_name):
    if food_name == "margherita":
        consuption_ingredients(food_name, rest_of_ingredients)
        return True
    elif food_name == "italiana":
        consuption_ingredients(food_name, rest_of_ingredients)
        return True
    elif food_name == "funghi":
        consuption_ingredients(food_name, rest_of_ingredients)
        return True
    elif food_name == "spinacy":
        consuption_ingredients(food_name, rest_of_ingredients)
        return True
    elif food_name == "vegetariana":
        consuption_ingredients(food_name, rest_of_ingredients)
        return True
    elif food_name == "fabrizio":
        consuption_ingredients(food_name, rest_of_ingredients)
        return True
    elif food_name == "pirata":
        consuption_ingredients(food_name, rest_of_ingredients)
        return True
    elif food_name == "pollo":
        consuption_ingredients(food_name, rest_of_ingredients)
        return True
    else:
        return False
    

    
def ingredients_checker(item):
    for index, amount in item.items():
        if item[index] > 0:
            return True
        if item[index] < 0:
            return False
        
    
#Constants
rest_of_ingredients = consuption()
order = []

def core_function():
    #Intro
    print("Greetings! Welcome to MPH (Mobile Pizza Hut)! If u're already decided what would you like to pick from our Menu, I'm here to help with your order!")
    print("Our humble selection as it is: ", "Margherita", "Italiana", "Funghi", "Spinacy", "Vegetariana", "Fabrizio", "Pirata", "Pollo", sep="\n" )
    
    first_pick = input("What would you like to order ? ")
    if first_pick == "Admin":
        admin_access(rest_of_ingredients)
        core_function()
    elif first_pick != "Admin" and calculate_ingredients(first_pick) == True:
        determination = ingredients_checker(rest_of_ingredients)
        if determination == True:
            order.append(first_pick)
            letitroll = input("Would u like to add another item ? Yes/No: ")
            if letitroll == "yes":
                cycle_function()
            elif letitroll == "no":
                print(f"A total cost is up to {pricing(order)}")
                payment()
            else:
                print("I'll take as 'no' answer")
                print(f"A total cost is up to {pricing(order)}")
                payment()
        elif determination == False:
            print("We are pretty much out of an ingredients, not able to proceed with your order! We apologize, you can visit us tomorow again.")
            print("Oh yes and everything you've put as an order will be served as a dinner for our employees and therefore go home... hungry!")
            exit()
    elif first_pick != "Admin" and calculate_ingredients(first_pick) == False:
        print("Try it again and don't be dumb this time!")
        core_function()
   
    

def cycle_function():
    lets_continue = True
    while lets_continue:
        user_choice = input("What would u like to order additionaly? ")
        if user_choice == "Admin":
            admin_access(rest_of_ingredients)
            cycle_function()

        elif user_choice != "Admin" and calculate_ingredients(user_choice) == True:
            lets_continue = ingredients_checker(rest_of_ingredients)

            if lets_continue == False:
                print("We are pretty much out of an ingredients, not able to proceed with your order! We apologize, you can visit us tomorow again.")
                print("Oh yes and everything you've put as an order will be served as a dinner for our employees and therefore go home...hungry!")
                exit()

            elif lets_continue == True:
        
                order.append(user_choice)
                another = input("Would u like to add another item ? Yes/No: ")
                if another == "yes":
                    cycle_function()
                elif another == "no":
                    print(f"A total cost is up to {pricing(order)}")
                    payment()
                else:
                    print("I'll take as 'no' answer")
                    print(f"A total cost is up to {pricing(order)}")
                    payment()
        elif user_choice != "Admin" and calculate_ingredients(user_choice) == False:
            print("Try it again and don't be dumb this time!")
            cycle_function()
        
        
core_function()
from data import MENU
from data import resources

#functions
def admin_access(data):
    print(f"Initial ingredients: {data}")

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
            core_function()
        else:
            attempts -= 1
            print(f"The password you've entered is too long or too short. Try again! You have {attempts} attempts left.")
            

        if attempts == 0:
            print("You have entered wrong PIN 3-times in row!", "Cancelling your order!", "Calling the cops!", "See u in prison scamer!", "Next customer please!", sep="\n")
            core_function()

def consuption():
    return resources




def consuption_ingredients(pizza, ingredience):
    for keys, numbers in ingredience.items():
        for key, number in MENU[pizza]["ingredients"].items():
            if keys == key:
                ingredience[keys] = ingredience[keys] - MENU[pizza]["ingredients"][key]
    print(ingredience)
                
                



def calculate_ingredients(food_name):
    if food_name == "margherita":
        consuption_ingredients(food_name, rest_of_ingredients)
    elif food_name == "italiana":
        consuption_ingredients(food_name, rest_of_ingredients)
    elif food_name == "funghi":
        consuption_ingredients(food_name, rest_of_ingredients)
    elif food_name == "spinacy":
        consuption_ingredients(food_name, rest_of_ingredients)
    elif food_name == "vegetariana":
        consuption_ingredients(food_name, rest_of_ingredients)
    elif food_name == "fabrizio":
        consuption_ingredients(food_name, rest_of_ingredients)
    elif food_name == "pirata":
        consuption_ingredients(food_name, rest_of_ingredients)
    elif food_name == "pollo":
        consuption_ingredients(food_name, rest_of_ingredients)
    
        
    
    



#Intro
print("Greetings! Welcome to MPH (Mobile Pizza Hut)! If u're already decided what would you like to pick from our Menu, I'm here to help with your order!")
print("Our humble selection as it is: ", "Margherita", "Italiana", "Funghi", "Spinacy", "Vehetariana", "Fabrizio", "Fabricio", "Pollo", sep="\n" )

#Constant
rest_of_ingredients = consuption()

def core_function():
    #Intro
    print("Greetings! Welcome to MPH (Mobile Pizza Hut)! If u're already decided what would you like to pick from our Menu, I'm here to help with your order!")
    print("Our humble selection as it is: ", "Margherita", "Italiana", "Funghi", "Spinacy", "Vehetariana", "Fabrizio", "Fabricio", "Pollo", sep="\n" )

    #Variable points
    lets_continue = True
    order = []
    first_pick = input("What would you like to order ? ")
    calculate_ingredients(first_pick)
    if first_pick == "Admin":
        admin_access(rest_of_ingredients)
    order.append(first_pick)
    #Logic
    while lets_continue:
        lets_continue = input("Would u like to add another item ? Yes/No: ")
        if lets_continue == "yes":
            user_choice = input("What would u like to order additionaly? ")
            calculate_ingredients(user_choice)
            order.append(user_choice)
        elif lets_continue == "no":
            print(f"A total cost is up to {pricing(order)}")
            payment()
        else:
            print("I'm just a dumb program which doesn't understand your other needs for now. Keep it simple Yes/No.")

core_function()
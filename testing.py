import random
# Menu and introduction 
no_responses = [
    "No problem! Feel free to browse our menu at your leisure!",
    "Sure, take your time. If you have any questions, let me know.",
    "Thank you for taking a look. Hope to see you next time!"

]
 


while True:
    guest_input = input(f"Thank you {user_name}. How many people would need seat?")

    try:
        guest_number = int(guest_input)
    
        if guest_number > 6 :
            print("Please wait for staff to explain group policies.Thank you")
            break
        elif guest_number >= 1 and guest_number <= 6:
            print("""We got 3 Hookah flavors and 3 drinks
A hookah cost $20 (mix any flavor free of charge) and a drink cost $3""")
            break
        else: 
            print("Please enter number of guest 1 or more")

    except ValueError:
        print("Invalid input, Please enter number")

drinks = ["Soda", "Coffee", "Tea"]
hookahs = ["Mint", "Cherry", "Blue Mist"]
guest_order = {}
print("Drink options:")
for i, drinks in enumerate(drinks):
    print(f"{i+1}. {drinks}")

print("Hookah Flavors")
for i, hookahs in enumerate(hookahs):
    print(f"{i+1}. {hookahs}")


while True:
    try:
        drink_choice_str = input("Please select a drink by number (or '0' if no drink): ")
        drink_choice_index = int(drink_choice_str) - 1

        if drink_choice_index == -1: # User entered '0'
            print("No drink selected.")
            break
        elif 0 <= drink_choice_index < len(drinks):
            chosen_drink = drinks[drink_choice_index]
            while True:
                try:
                    quantity = int(input(f"How many {chosen_drink} would you like? "))
                    if quantity > 0:
                        guest_order['drink'] = chosen_drink
                        guest_order['drink_quantity'] = quantity
                        print(f"Added {quantity} x {chosen_drink} to your order.")
                        break
                    else:
                        print("Please enter a positive quantity.")
                except ValueError:
                    print("Invalid input. Please enter a number for quantity.")
            break
        else:user_name = (input("""Hello there
Welcome to RC Hookah Cafe!!
What is your name?"""))
            print("Invalid drink number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        #the number of specific drinks
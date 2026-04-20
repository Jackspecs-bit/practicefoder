import random
# Menu and introduction 
no_responses = [
    "No problem! Feel free to browse our menu at your leisure!",
    "Sure, take your time. If you have any questions, let me know.",
    "Thank you for taking a look. Hope to see you next time!"]

drinks = ["Soda", "Coffee", "Tea"]
hookahs = ["Mint", "Cherry", "Blue Mist"]

print("Drink Options")
for i drink, in enumerate (drinks, start=1):
    print(f"{i}. {drink}")
# teas = ["Mango Passion", "Dragon Fruit", "Milk Tea", "Peach", "Jasmine", "Strawberry"]
# desserts = ["Glazed Donut", "Lemon Pie", "Carrot Cake", "Ice Cream", "Cheesecake"]
#Dictionary is a list of key that retrieve its value, which can be anytype, strings, floats, integer
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# drinks_menu = {"Mango Passion": "$5.00"}

# cars = ["tesla", "honda", "audi"]# key is the index, index is an ordered list
tesla = {
    "brand"  : "Tesla", # key is a string that refer to a value.
    "model" : "xyz",
    "year" : "2024",
    "miles" : 28500,
}
honda = {
    "brand"  : "Honda", # key is a string that refer to a value.
    "model" : "y",
    "year" : "1988",
    "miles" : 10000,
}
audi = {
    "brand"  : "Audi", # key is a string that refer to a value.
    "model" : "z",
    "year" : "2024",
    "miles" : 4000,
}
cars_list = [tesla, honda, audi]
print(cars_list)
print(cars_list[2]["miles"])


drinks  = {
    "Mango" : 5.00,
    "Peach" : 5.00,
    "Passion Fruit" : 4.90,
    "Orange" : 5.60,
}

desserts = {
    "Donuts": 2.00,
    "Cakes" : 2.50,
    "Pies" : 2.50,
    "Ice Cream" : 4.00,
    
}

cafe_menu = [drinks, desserts]
print("------drinks-------")
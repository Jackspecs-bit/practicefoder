
#comparison operator (==) used to test data equality 
#Semi-colon (:) used at end of format
#of code that take their orders
#from a line that ends in a colon are indented. 
#As a rule of thumb: indent after a colon.
#             ------------
#Another comparison operator, !=,It means is not equal to.
#The keyword else gets its own line and a colon at the end.
#Statements that execute in the else case are indented.
#As in the if case, any number of statements can execute in the else case
#else: is catchall (meaning its at the end)
#You can have any number of elif statements.
# elif code runs only if the first test fails.


your_ticket_number = 487208
if your_ticket_number != 487208:
 print("Better luck next time.")

 

test = 2
if test == 2: 
  print(test)
else: 
   print("Dont Test")


age = 21
num_age = int(input("How old are you?"))
if num_age >= 21:
    print("""You can have a drink
# enjoy your day 
# drink responsibly""")
elif num_age <= 20:
    print("You are not allowed to purchase order.")
else:
   print("Please see a staff member.")

    
Weather = int(input("what is the teampture out side?"))
if Weather >= 21:
   print("its getting warm")
else:
    print("It is starting to get cold")


speed = 50  # Keep speed at 50, or any other value
if speed >= 65:
    print("You are driving over speed limit")
else: # This part runs if the 'if' condition (speed >= 65) is False
    print("You are driving within the speed limit")

drinks = ["Soda", "Coffee", "Tea"]
hookahs = ["Mint", "Cherry", "Blue Mist"]


#-----------Testing sets of conditions------------
#suppose not one but two conditions
#have to be met in order for a test to succeed.

if weight > 300 and time < 6:
 status = "try to recruit him"

if SAT > avg or GPA > 2.5 or parent == "alum":
 message = "Welcome to Leeds College!"

if age > 65 or age < 21 and res == "U.K.":
   
#Code a line that tests whether the variable city is "London" or "Tel Aviv."
if city == "London" or city == "Tel Aviv":
   
#Code a line that tests whether the variable total is 10 or 20.
if total == 10 or total == 20:

#If the variable animal is "dog", "cat", or "mouse" display "mammal".
if animal == "dog" or animal == "cat" or animal == "mouse":
  print("mammal")

#If the variable nationality is "UK" 
#and either the variable age is under 21 or it's over 64 display "qualified"
if nationality == "UK" and (age < 21 or age > 64):
  print("qualified")


# -------if nested statments---------
#build logic structure through hierarchy
if (x == y or a == b) and c == d:
 g = h
else:
  e = f
  # changed to :

if c == d:# If the condition tested by the top first-level if—that c has the same value
#as d—is true…
    if x == y:
     g = h
    elif a == b:
     g = h
    else:
    e = f
else:
      e = f

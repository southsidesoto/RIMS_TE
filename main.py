import random
#The purpose of this program is to aid in inventory management at the local restaurant: "Spurghetters"

#To those reading: This is just a sample of what I am expecting. When it comes to your dishes, make sure that they are more specific ingredients-wise. There are LOADS of ingredients.

#Establishing the Initial Supply
'''In order for this section to be complete, we would need to make some estimates based on the average number of people visiting a family restaurant per day. Once we have that information, we can math it up in order to predict a good starting amount that may last a week. Once the random generator comes into play, then we'll be able to better predict when a restaurant should be putting in orders for restocking in the best case scenario of 7 days.'''

#Establishing Static Meal Ingredient Variables Used
'''
The meatballs and patties will both be using the same meat supply,
so that needs to be taken into account.

Additionally, ingredient amounts will be listed as per serving.
The types of measurements will vary from pounds to ounces.
'''
#buns will be considered separate in this program
buns = 2
patty = .25
cheese = 1
spaghetti = 2
sauce = ""
meatball = .03
potato = ""
macaroni = ""
lettuce = ""
carrot = ""
crouton = ""
onion = ""
tomato = ""
#salt will be tricky, and to make it simple, we'll use the same per dish (tsp)
salt = .5

#Establishing Bulk Orders
'''This area is to keep track of how much of the starting bulk supply of the ingredients is. This will be handy when figuring out when is a good time to start ordering more ingredients. Keep in mind that bulk patty will cover the meat necessary for meatballs as well. The types of measurements will vary from pounds to ounces.
*will be represented as b_'''

'''Box will be measured by how many individual packs fit into the measurement box (the cardboard box in my room). 
For Example: 
1 pack of hamburger buns contains 8 buns (as half). The box in my room will hold 9 packs.
Box Bun order would be 9x8: 72 buns(top and bottom)'''
#buns * [number of buns per box]
b_buns = 72
#meat will be by the pound
b_meat = 12
#cheese will be by the slice (10 per pack)
b_cheese = 36 
#spaghetti measured by oz.
b_spaghetti = ""
#this will need to be re-evaluated
b_sauce = ""
b_potato = ""
b_macaroni = ""
b_lettuce = ""
b_carrot = ""
b_crouton = ""
b_onion = ""
b_tomato = ""
b_salt = 122.75

'''
Also keep in mind that you will need variables to keep track of the ingredients that were used throughout the day, but this could be part of your randomization function. You just need to make sure to return the value and that it subtracts from the bulk order

Sample conditional: psuedocode
if stock_item is less than or equal to 1/3 of the bulk order: 
  Restaurant should put in an order.
  
'''
'''1225 is the average traffic weekly.
If we go off the idea that each dish is ordered equally, 408 is our starting ingredient supply multiple to start off the week'''

#Establishing Item Stock
#listed by individual ingredient
stock_buns = 1632
stock_meat = 217.6
stock_cheese = 408
stock_spaghetti = 816
stock_sauce = ""
stock_potato = ""
stock_macaroni = ""
stock_lettuce = ""
stock_carrot = ""
stock_crouton = ""
stock_onion = ""
stock_tomato = ""
stock_salt = 612.5

#Establishing Entree Lists
hamburger = [buns, patty, salt]
cheeseburger = [buns, patty, salt, cheese, onion, lettuce, tomato]
spag_n_meat = [spaghetti, salt, sauce, meatball]

#Establishing Side Lists
fries = [potato, salt]
mac_n_cheese = [macaroni, cheese]
salad = [lettuce, carrot, crouton, onion, tomato]

#Establishing Optional Lists
entrees = [hamburger, cheeseburger, spaghetti]
sides = [fries, mac_n_cheese, salad]
'''I'm pretty sure that the above code isn't really necessary (hence the name), but you never know.'''

#Restock Info
#by the pallet
re_buns = 1800/5
re_meat = 450/5
re_cheese = ""
#spaghetti measured by oz.
re_spaghetti = ""
#this will need to be re-evaluated
re_sauce = ""
re_potato = ""
re_macaroni = ""
re_lettuce = ""
re_carrot = ""
re_crouton = ""
re_onion = ""
re_tomato = ""
re_salt = 122.75


#Stock Subtraction (Hamburgers)
def stock_sub_ham(burgers_daily, hamburger, stock_buns, stock_meat,stock_salt):
  global leftover_buns
  global leftover_meat
  global leftover_salt
  
  print("Starting Stock Buns by Bun")
  print(stock_buns)
  print("Starting Stock Meat by Pound")
  print(stock_meat)
  print("Starting Stock Salt by Ounce")
  print(stock_salt)

  while len(burgers_daily) > 0:
    buns_used = hamburger[0] * burgers_daily[0]
    meat_used = hamburger[1] * burgers_daily[0]
    salt_used = hamburger[2] * burgers_daily[0]
    #print("Buns Used:")
    #print(buns_used)
    #print("Meat Used:")
    # print(meat_used)
    # print("Salt Used:")
    # print(salt_used)
    stock_buns = stock_buns - buns_used
    stock_meat = stock_meat - meat_used
    stock_salt = stock_salt - salt_used
    # print("Bun Stock")
    # print(stock_buns)
    # print("Meat Stock")
    # print(stock_meat)
    # print("Salt Stock")
    # print(stock_salt)
    burgers_daily.pop(0)
  
  # print("Leftover Stock Buns")
  # print(stock_buns)
    leftover_buns = stock_buns
  # print("Leftover Stock Meat")
  # print(stock_meat)
    leftover_meat = stock_meat
  # print("Leftover Stock Salt")
  # print(stock_salt)
    leftover_salt = stock_salt
  
  return(leftover_buns, leftover_meat, leftover_salt)


#Stock Subtraction (Cheeseburgers)
def stock_sub_cheese(): 
  print("")

def restock_check(current_stock, restock_amount):
  if current_stock < restock_amount:
    print("Sending in re-stock order.")
  else:
    print("Stock is sufficient.")

###Random Program###
def random_customer_orders():
  global burgers_daily
  global cheese_daily
  global spag_daily
  choice1 = "hamburger"
  choice2 = "cheeseburger"
  choice3 = "spag_n_meat"
  choice_list = [choice1, choice2, choice3]
#The visits were based off a google search for average customers a day
  customer_orders = []
  customer_weekly = []
#This list will list days in groups of three (ham, cheese, spag)
  orders_daily = []
  burgers_daily = []
  cheese_daily = []
  spag_daily = []

  while len(customer_weekly) < 7:
    customer_visits = random.randint(100,250)
  #instead of doing it day to day, generate 7 days right off the bat, then randomize the orders with the code you used originally. your problem is making a list of 7 random counts
    customer_weekly.append(customer_visits) 
    while customer_visits > 0:
      customer_orders.append(random.choice(choice_list))
      customer_visits = customer_visits - 1
    orders_daily.append("Day:" + str(len(customer_weekly)))
  #print(len(customer_orders))
  #print("# of Hamburgers")
  #print(customer_orders.count(choice1))
    burgers_daily.append(customer_orders.count(choice1))
  #print("# of Cheeseburgers")
  #print(customer_orders.count(choice2))
    cheese_daily.append(customer_orders.count(choice2))
  #print("Spaghetti and Meatballs")
  #print(customer_orders.count(choice3))
    spag_daily.append(customer_orders.count(choice3))
  #need to clear customer_orders list at the end of each iteration
  #print("Totals Daily:")
  #print(len(customer_orders))
    customer_orders.clear()
  
#   print("Weekly Customer Visits")
#   print(customer_weekly)
#   print()
#   print("According to the data presented, the average number of customers per day is: " + str(int(sum(customer_weekly, 0)/7)) + ".")
 
# #Day One
#   print("Day 1:")
#   print("H  C  S")
#   print(burgers_daily[0] , cheese_daily[0] , spag_daily[0])
#   print()
# #Day Two
#   print("Day 2:")
#   print("H  C  S")
#   print(burgers_daily[1] , cheese_daily[1] , spag_daily[1])
#   print()
# #Day three
#   print("Day 3:")
#   print("H  C  S")
#   print(burgers_daily[2] , cheese_daily[2] , spag_daily[2])
#   print()
# #Day Four
#   print("Day 4:")
#   print("H  C  S")
#   print(burgers_daily[3] , cheese_daily[3] , spag_daily[3])
#   print()
# #Day Five
#   print("Day 5:")
#   print("H  C  S")
#   print(burgers_daily[4] , cheese_daily[4] , spag_daily[4])
#   print()
# #Day Six
#   print("Day 6:")
#   print("H  C  S")
#   print(burgers_daily[5] , cheese_daily[5] , spag_daily[5])
#   print()
# #Day Seven
#   print("Day 7:")
#   print("H  C  S")
#   print(burgers_daily[6] , cheese_daily[6] , spag_daily[6])

#   print("Average Hamburgers Ordered Daily")
#   print(round(sum(burgers_daily)/7))
#   print("Total Hamburgers Ordered Weekly")
#   print(sum(burgers_daily, 0))
#   print()

#   print("Average Cheeseburgers Ordered Daily")
#   print(round(sum(cheese_daily)/7))
#   print("Total Cheeseburgers Ordered Weekly")
#   print(sum(cheese_daily, 0))
#   print()

#   print("Average Spaghetti Ordered Daily")
#   print(round(sum(spag_daily)/7))
#   print("Total Spaghetti Ordered Weekly")
#   print(sum(spag_daily, 0))
### What will be returned to the program?
  return (burgers_daily, cheese_daily, spag_daily)
'''After running the program, we will operate under the assumption that 175 is the global average for our branch.'''

print("--------------------------------")
print("THIS IS WHERE THE PROGRAM BEGINS")
print("--------------------------------")
print()
print("Initiating Randomization Program...")
print()
random_customer_orders()
print("--------------------------")
print("MEALS ORDERED FOR THE WEEK")
print("--------------------------")
print("Burgers:")
print(burgers_daily)
print("Cheese Burgers")
print(cheese_daily)
print("Spaghetti N' Meatballs")
print(spag_daily)
print()
print("--------------")
print("CHECKING STOCK")
print("--------------")
stock_sub_ham(burgers_daily, hamburger, stock_buns, stock_meat,stock_salt)
print()
print("----------------------")
print("SUBTRACTION INITIATING")
print("----------------------")
print("Starting Stock")
print(stock_buns, stock_meat, stock_salt) 
print("Stock Depleted")
print((stock_buns - leftover_buns),(stock_meat - leftover_meat), (stock_salt - leftover_salt))
print("New Stock")
print(leftover_buns, leftover_meat, leftover_salt)
stock_buns = leftover_buns
stock_meat = leftover_meat
stock_salt = leftover_salt

print()
print("-------------")
print("RESTOCK CHECK")
print("-------------")
restock_check(stock_buns, re_buns)

# stock_sub_ham(burgers_daily, hamburger, stock_buns, stock_meat,stock_salt)
# stock_buns = leftover_buns
# stock_meat = leftover_meat
# stock_salt = leftover_salt

# print(stock_buns, stock_meat, stock_salt) 
# restock_check(stock_buns, re_buns)


#program works by the week, but make sure to add user input so that the program can run based off of choice. 
#May also need to adjust a day-to-day code that can check more specifically when to put in a restock order.
#for example: LOOP 
###run a check for the list[0] orders. restock where needed, .pop the list[0], then run it again. Print out the ingredient supply, maybe list the percentage of ingredient left, and in the restock statement, say what was ordered for restock.
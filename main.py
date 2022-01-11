print("Hello! Welcome to Max's sandwich shop. Let's get an order started for you.\n")

name = input("What's your name? --> ")

#Sandwich Creation

#Bread

print("\nHey " + str(name) + ", We have 2 types of sandwich lengths. 6 inch or foot long.")
sandwich_size=["6 inch","footlong"]
sandwich_size_selections=int(input("Enter 0 for '6 inch' or enter 1 for 'foot long' --> "))


#Meat

choice=input("\nDo you want meat? ('yes' or 'no') --> ")
meat_selections=[]
while choice=='yes':

  sandwich_meat=["steak","salami","turkey","ham","chicken","bacon","pepperoni"]

  meat_choice=int(input("\n0 for steak, 1 for salami, 2 for turkey, 3 for ham, \n4 for chicken, 5 for bacon, 6 for pepperoni, 9 if done with meat --> "))

  if meat_choice==9:
    choice='no'
  else:
    meat_selections.append(sandwich_meat[meat_choice])
  

print("You chose: " + str(meat_selections))

#Cheese

print("\nLet's get some cheese on here.")
choice=input("Do you want cheese? --> ")
cheese_selections=[]
while choice=='yes':

  sandwich_cheese=["provolone","cheddar","american","pepper jack"]

  cheese_choice=int(input("\n0 for provolone, 1 for cheddar, 2 for american, \n3 for pepperjack, 9 if you're done with cheese. --> "))

  if cheese_choice==9:
    choice='no'
  else:
    cheese_selections.append(sandwich_cheese[cheese_choice])

print("You chose: " + str(cheese_selections))

#Vegetables

print("\nOkay, now for the vegetables.")
choice=input("Do you want vegetables? --> ")
vegetable_selections=[]
while choice=='yes':

  sandwich_vegetables=["lettuce","spinach","tomatoes","pickles","onions","peppers", "olives"]

  vegetables_choice=int(input("\n0 for lettuce, 1 for spinach, 2 for tomatoes, \n3 for pickles, 4 for onions, 5 for peppers, \n6 for olives, Enter 9 when you're done. --> "))
  if vegetables_choice==9:
    choice='no'
  else:
      vegetable_selections.append(sandwich_vegetables[vegetables_choice])


print("You chose: " + str(vegetable_selections))
#Drink and Chips

print("\nWe have created your sandwich, but we need a drink and chips too.\n")
print("Here is our selection.")
drinks=["Coke","Sprite","Mountain Dew","Fanta","lemonade","water"]
drink=int(input("0 for Coke, 1 for Sprite, 2 for Mountain Dew, 3 for Fanta, \n4 for lemonade, 5 for water. --> "))

print("\nNow for Chips")
chips=["Lays Potato Chips","Lays BBQ Chips","Doritos","Sun Chips"]
chip=int(input("0 for Lays Potato chips, 1 for Lays BBQ chips, 2 for Doritos, \n3 for Sun chips. --> "))

#Pricing variables

sixinch_price = 1.75
footlong_price = 2.50

steak_price = 0.45
salami_price = 0.45
turkey_price = 0.25
ham_price = 0.30
chicken_price = 0.35
bacon_price = 0.35
pepperoni_price = 0.25

provolone_price = 0.45
cheddar_price = 0.45
american_price = 0.45
pepper_jack = 0.45

lettuce_price = 0.15
spinach_price = 0.15
tomatoes_price = 0.15
pickles_price = 0.15
onions_price = 0.15
peppers_price = 0.20
olives_price = 0.15

drink_price = 2.00
chip_price = 1.50

#Check out

print("\nOkay, we have created your order!\n")

bread_price = 0

if sandwich_size_selections==0:
  bread_price += 1.75
elif sandwich_size_selections==1:
  bread_price += 2.50

meat_price = 0

def set_meat_price(meat_price, meat_selections):
  for meat in meat_selections:
    if meat == "steak":
      meat_price += steak_price
    elif meat == "salami":
      meat_price += salami_price
    elif meat == "turkey":
      meat_price += turkey_price
    elif meat == "ham":
      meat_price += ham_price
    elif meat == "chicken":
      meat_price += chicken_price
    elif meat == "bacon":
      meat_price += bacon_price
    elif meat_price == "pepperoni":
      meat_price += pepperoni_price
  return meat_price

meat_price = set_meat_price(meat_price, meat_selections)

cheese_price = 0

def set_cheese_price(cheese_price, cheese_selections):
  for cheese in cheese_selections:
    if cheese == "provolone":
      cheese_price += provolone_price
    elif cheese == "cheddar":
      cheese_price += cheddar_price
    elif cheese == "american":
      cheese_price += american_price
    elif cheese == "pepper_jack":
      cheese_price += "pepper_jack"
  return cheese_price

cheese_price = set_cheese_price(cheese_price, cheese_selections)

vegetable_price = 0

def set_vegetable_price(vegetable_price, vegetable_selections):
  for vegetables in vegetable_selections:
    if vegetables == "lettuce":
      vegetable_price += lettuce_price
    elif vegetables == "spinach":
      vegetable_price += spinach_price
    elif vegetables == "tomatoes":
      vegetable_price += tomatoes_price
    elif vegetables == "pickles":
      vegetable_price += tomatoes_price
    elif vegetables == "onions":
      vegetable_price += onions_price
    elif vegetables == "peppers":
      vegetable_price += peppers_price
    elif vegetables == "olives":
      vegetable_price += olives_price
  return vegetable_price

vegetable_price = set_vegetable_price(vegetable_price, vegetable_selections)

price = bread_price + meat_price + cheese_price + vegetable_price + drink_price + chip_price

tax_price = price * 0.056

total_price = tax_price + price

print("Here is the total price:")

total_price = round(total_price, 2)

print("$" + str(total_price))


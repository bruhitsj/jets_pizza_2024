def Pizza_price(""" I would like to order a pizz""") 
base_price = 15
toppings_price = 0
for toppings in requested_toppings:
  if toppings == "T":
    toppings_price += 1.5

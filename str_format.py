quantity = 300
item_no = 5670
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
myorder_dup = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, item_no, price))
print(myorder_dup.format(quantity, item_no, price))
print("We are so called \"Vikings\" from the north")
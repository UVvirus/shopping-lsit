import datetime

time=datetime.datetime.now()
year=str(time.year)
month=str(time.month)
day=str(time.day)
hour=str(time.hour)
minute=str(time.minute)
list_of_items=['Meat','Cheese']
print(day+"/"+month+"/"+year)
print(hour+":"+minute)
print("Items in your list are:",list_of_items)

user_input=input("Enter the item to add:").title().strip()
list_of_items.append(user_input)
print(list_of_items)
list_of_items.sort()
print("sorted list :",list_of_items)
print("length of list:",len(list_of_items))
food_purchased=input("Enter the purchased food:").title()
list_of_items.remove(food_purchased)
new_food=input("Enter a new food:").title()
list_of_items.insert(0,new_food)
print(list_of_items)
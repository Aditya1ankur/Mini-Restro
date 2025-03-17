#define the menu of restro
menu = {
    "Burger": 80,
    "Pasta": 120,
    "Pizza": 150,
    "Fries": 50,
    "Shake": 30
}

#greet
print("welcome to the restro")
print("Burger: Rs. 80\n Pasta: Rs. 120\n Pizza: Rs. 150\n Fries: Rs. 50\n Shake: Rs. 30")

order_total = 0
#80 +120 = 200


item_1 = input("Enter the first item: ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 80 = 80
    print(f"Your item {item_1} has been added to your order")
          
else:
    print(f"Please order something from the menu")
    
another_order = input("Do you want to order another item? (yes/no): ")  
if another_order == "yes":
    item_2 = input("Enter the second item: ")
    if item_2 in menu:
        order_total += menu[item_2] #80 + 120 = 200
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Please order something from the menu")
        
    print(f"Your total bill is: Rs. {order_total}")
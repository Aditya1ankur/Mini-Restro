Here's a **README.md** file for your **Restaurant Menu Python Project**:  

---

## **Restaurant Menu Ordering System (Python)**
This Python script allows users to order items from a restaurant menu and calculates the total bill.

### **Features**
- Displays a predefined restaurant menu.
- Takes user input to order items.
- Calculates and displays the total bill.
- Allows ordering a second item.

---

## **Installation**
Ensure you have Python installed, then simply run the script:

```bash
python restro_menu.py
```

---

## **Usage**
1. The program displays the menu with item prices.
2. The user enters the name of an item to order.
3. If the item exists in the menu, it is added to the order.
4. The user is asked if they want to order another item.
5. The total bill is displayed.

---

## **Code Explanation**
```python
menu = {
    "Burger": 80,
    "Pasta": 120,
    "Pizza": 150,
    "Fries": 50,
    "Shake": 30
}
```
- Defines a dictionary with menu items and their prices.

```python
item_1 = input("Enter the first item: ")
if item_1 in menu:
    order_total += menu[item_1]
```
- Takes user input and checks if the item is in the menu.
- If valid, adds its price to the total.

```python
another_order = input("Do you want to order another item? (yes/no): ")  
if another_order == "yes":
```
- Asks the user if they want to order another item.

```python
print(f"Your total bill is: Rs. {order_total}")
```
- Displays the final bill.

---

## **Example Output**
```
Welcome to the restro
Burger: Rs. 80
Pasta: Rs. 120
Pizza: Rs. 150
Fries: Rs. 50
Shake: Rs. 30
Enter the first item: Pizza
Your item Pizza has been added to your order
Do you want to order another item? (yes/no): yes
Enter the second item: Shake
Your item Shake has been added to your order
Your total bill is: Rs. 180
```

---

## **Future Enhancements**
- Allow multiple items to be ordered at once.
- Implement discounts or combo offers.
- Improve error handling for invalid inputs.

---

Let me know if you need any modifications! 🚀

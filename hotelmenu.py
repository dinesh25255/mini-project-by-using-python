print("Welcome to PYTHON Restaurant")
menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'coffee': 80
}

for item, price in menu.items():
    print(f"{item.capitalize()}: RS{price}")

order = []
another_order = "yes"  # Initialize another_order to enter the loop

while another_order.lower() == "yes":
    item = input("Enter the name of item you want to order: ").lower()
    if item in menu:
        order.append(item)
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu.")

    another_order = input("Would you like to place another order? (yes/no): ").lower()

print("Your final order is:")
for item in order:
    print(f"{item.capitalize()}: RS{menu[item]}")

total_cost = sum(menu[item] for item in order)
print(f" the Total amount to pay : RS{total_cost}")

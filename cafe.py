#1. Define the Menu Structure:
menu = {
    "food": ["Chiken Roll", "Tuna Sandwich", "Salad", "Creeps", "Scone"],
    "drinks": ["Coffee", "Tea", "Juice", "Coke", "Sparklin Water"],
    "books": ["Where the Crawdads Sing by Delia Owens",
              "Becoming by Michelle Obama",
              "Educated by Tara Westover",
              "The Silent Patient by Alex Michaelides",
              "The Testaments by Margaret Atwood"]
}

specials = {
    "food": [],
    "drinks": [],
    "books": []
}

orders = []
employees = {"admin": "password"}  # Sample employee credentials

#2. Utility Functions:
def display_menu():
    print("Menu:")
    for category, items in menu.items():
        print(f"  {category.capitalize()}:")
        for item in items:
            print(f"    - {item}")

def display_specials():
    print("Specials:")
    for category, items in specials.items():
        print(f"  {category.capitalize()}:")
        for item in items:
            print(f"    - {item}")

def add_to_menu(item, category):
    if category in menu:
        menu[category].append(item)
    else:
        print("Invalid category")

def add_to_specials(item, category):
    if category in specials:
        specials[category].append(item)
    else:
        print("Invalid category")

def view_customers():
    for order in orders:
        print(order)

#3. Customer Functions:
def place_order():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    order_items = []

    while True:
        display_menu()
        item = input("Select an item to order (type 'done' to finish): ")
        if item.lower() == 'done':
            break
        for category in menu.values():
            if item in category:
                order_items.append(item)
                break
        else:
            print("Item not in menu")

    orders.append({"name": name, "address": address, "order": order_items})


#4. Employee Functions:
def employee_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in employees and employees[username] == password:
        return True
    return False

def employee_interface():
    if not employee_login():
        print("Invalid credentials.")
        return

    while True:
        print("\nEmployee Interface:")
        print("1. Update Menu")
        print("2. Add Specials")
        print("3. View Customer Details")
        print("4. Logout")
        choice = input("Select an option: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            category = input("Enter the category (food/drinks/books): ")
            add_to_menu(item, category)
        elif choice == "2":
            item = input("Enter the item to add as special: ")
            category = input("Enter the category (food/drinks/books): ")
            add_to_specials(item, category)
        elif choice == "3":
            view_customers()
        elif choice == "4":
            break
        else:
            print("Invalid option")

#5. Main Function and User Interface:
def main():
    while True:
        print("\nMain Menu:")
        print("1. View Menu")
        print("2. View Specials")
        print("3. Place an Order")
        print("4. Employee Login")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            display_specials()
        elif choice == "3":
            place_order()
        elif choice == "4":
            employee_interface()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
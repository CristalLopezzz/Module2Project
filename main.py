# North Loop Provisions - Donut Shop Management System

def welcome_message():
    # Displaying a welcome message for the donut shop 
    print("🍩 Welcome to North Loop Provisions! 🍩")
    print("crafting artisinal donuts in Minneapolis's North Loop")
    print("-------------------------------------------")

def show_menu():
    #Display current menu
    menu = {
        "Classic Glazed": 3.50,
        "Maple Bacon": 4.50,
        "Spyhouse Coffee": 4.00,
        "MN Berry": 4.25,
        "Local Honey": 4.00,
    }

    print("\nToday's Donut Menu: ")
    print("------------------")
    for donut, price in menu.items():
        print(f"{donut}: ${price:.2f}")

# Main program
if __name__ == "__main__":
    welcome_message()
    show_menu()
    print("\nReady to serve our community with the finest donuts!")
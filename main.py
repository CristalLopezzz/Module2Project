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

# Initializing priced menu items
small_batch_price = 5.50 # Signature donuts
seasonal_price = 6.50 # Using local seasonal ingredients
collab_price = 75.0 # Local business collaborations

# Daily small-batch inventory
small_batch_inventory = 36 # Classic varieties
seasonal_inventory = 24 # Made with local seasonal ingredients
collab_inventory = 12 # Special collaboration items

# Calculate morning inventory value 
total_value = (small_batch_price * small_batch_inventory +
seasonal_price * seasonal_inventory +
collab_price * collab_inventory)

# Format total value to 2 decimal places using string formatting
print("Morning inventory value: $" + str("{:.2f}".format(total_value)))

# Customer information 
purchase_total = 28
is_local_resident = True
bike_commuter = True
brought_mug = False

# Initialize rewards 
discount = 0

if is_local_resident:
    discount += 0.10 # Supporting out neighbors with 10% off

if bike_commuter:
    discount += 0.05 # Ecnourzging sustainable transportation

if brought_mug:
    discount += 0.05 # Reducing waste

if purchase_total >= 25:
    discount += 0.05 # Bulk order appreciation

# Calculate and display final discount
final_discount = discount * 100
print("Your community rewards discount: " + str(final_discount) + "%")
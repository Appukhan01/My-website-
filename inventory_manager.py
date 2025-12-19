# Inventory System for HM Store
# Developer: Appu Khan

inventory = {
    "Laptop": 10,
    "Mobile": 25,
    "Headphones": 50,
    "Charger": 100
}

def display_inventory():
    print("\n--- Current Stock in HM Store ---")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity} units")
    print("---------------------------------")

def add_stock(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"\nAdding {quantity} new {item} to stock.")
    display_inventory()

# Main Program
if __name__ == "__main__":
    print("System Started...")
    display_inventory()
    
    # New stock arrived
    add_stock("Mobile", 10)
    add_stock("Screen Guard", 50) 

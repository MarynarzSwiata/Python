# Inventory list with product details
inventory = [
    {"id": 101, "name": "Classic T-Shirt", "stock": 20},
    {"id": 102, "name": "Leather Wallet", "stock": 5},
    {"id": 103, "name": "Bluetooth Headphones", "stock": 8},
    {"id": 104, "name": "Coffee Mug", "stock": 35}
]

def find_items_to_reorder(products_list, min_threshold):
    items_to_reorder = []
    for product in products_list:
        if product["stock"] < min_threshold:
            items_to_reorder.append({"name": product["name"], "stock": product["stock"]})
    return items_to_reorder

min_inventory = int(input("Enter the minimum inventory threshold: "))

items_needed = find_items_to_reorder(inventory, min_inventory)

if items_needed:
    print("Items that need to be reordered:")
    for item in items_needed:
        print(f'- {item["name"]} (Current stock: {item["stock"]})')
else:
    print("No items need to be reordered.")
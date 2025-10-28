import json

inventory = [
    {"id": 101, "name": "Classic T-Shirt", "stock": 20},
    {"id": 102, "name": "Leather Wallet", "stock": 5},
    {"id": 103, "name": "Bluetooth Headphones", "stock": 8},
    {"id": 104, "name": "Coffee Mug", "stock": 35}
]

file_scr = "100daysChallenge/mini-projects/inventory.json"

def write_file():
    with open(file_scr, "w") as f:
        json.dump(inventory, f, indent=4)

def read_file():
    with open (file_scr, "r") as f:
        print(json.load(f))

write_file()
read_file()
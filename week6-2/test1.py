# Initial inventory
inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

# 1. Update Inventory
def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0].lower() == item_name.lower():
            if quantity_sold <= item[1]:
                item[1] -= quantity_sold
            else:
                print(f"Not enough {item_name} in stock.")
            return
    print(f"{item_name} not found.")


# 2. Calculate Total Value
def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total += item[1] * item[2]
    return total


# 3. Find Most Expensive Item
def find_most_expensive(inventory):
    most_expensive = max(inventory, key=lambda x: x[2])
    return most_expensive[0]


# 4. Add or Update Item
def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0].lower() == item_name.lower():
            item[1] = quantity
            item[2] = price
            return
    inventory.append([item_name, quantity, price])


# -----------------------------
# Actions
# -----------------------------

# Update inventory after selling 20 bananas
update_inventory(inventory, "Banana", 20)

# Calculate total value
total_value = calculate_total_value(inventory)

# Find most expensive item
most_expensive = find_most_expensive(inventory)

# Add Eggs with 30 units at $0.25
add_item(inventory, "Eggs", 30, 0.25)

# Update Eggs to 50 units at $0.30
add_item(inventory, "Eggs", 50, 0.30)

# Display results
print("Updated Inventory:")
for item in inventory:
    print(item)

print(f"\nTotal Inventory Value: ${total_value:.3f}")
print(f"Most Expensive Item: {most_expensive}")
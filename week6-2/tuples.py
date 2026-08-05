# my_tuple = 1,2,3
# print(my_tuple)


# a,b,c = my_tuple
# print(a)
# print(b)
# print(c)




inventory = [
    ["apple",50, 0.75],
    ["Banana",100, 0.50],
    ["Orange",50, 0.80]
]


def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0].lower() == item_name.lower():
            if quantity_sold <= item[1]:
                item[1] -= quantity_sold
            else:
                print(f"Not enough {item_name} in stock.")
            return
    print(f"{item_name} not found.")

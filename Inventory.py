stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item in inventory:
        print(str(inventory[item])+' '+item)
        item_total += inventory[item]
    print("Total number of items: " + str(item_total))
displayInventory(stuff)
# 8)Print items that cost more than ₹50
# items = {"pen": 20, "notebook": 55, "bag": 120, "eraser": 10}

items = {"pen": 20, "notebook": 55, "bag": 120, "eraser": 10}
for item,price in items.items():
    if price > 50:
        print("The item cost more than 50 is",item)
print(items)
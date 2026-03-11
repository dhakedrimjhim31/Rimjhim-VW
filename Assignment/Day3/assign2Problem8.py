# Unit price
unit_price = 5

# Take quantity from user
quantity = int(input("Enter quantity: "))

# Calculate total price
total = quantity * unit_price

# Apply discount
if quantity > 50:
    total = total - (total * 0.50)
elif quantity > 30:
    total = total - (total * 0.10)

print("Total price after discountis: Rs", total)
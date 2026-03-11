# list of lambda functions
conversions = [
    lambda t: t * 1000,             # tonns to kg
    lambda kg: kg * 1000,           # kg to grams
    lambda g: g * 1000,            # grams to mg
    lambda mg: mg * 0.00000220462   # mg to pounds
]

tons = float(input("Enter weight in tons: "))

kg = conversions[0](tons)
grams = conversions[1](kg)
mg = conversions[2](grams)
lbs = conversions[3](mg)

print("Kilograms:", kg)
print("Grams:", grams)
print("Milligrams:", mg)
print("Pounds:", lbs)

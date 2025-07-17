# Electricity Bill Calculator

units = float(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2
elif units <= 300:
    bill = 100 * 1.5 + 100 * 2 + (units - 200) * 3
else:
    bill = 100 * 1.5 + 100 * 2 + 100 * 3 + (units - 300) * 5

print(f"Your total electricity bill is ₹{bill:.2f}")

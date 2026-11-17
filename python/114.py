num = int(input("Enter a number: "))

digits = str(num)
power = len(digits)
total = 0

for digit in digits:
    total += int(digit) ** power

if num >= 0 and total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
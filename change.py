cents = int(input("Please enter an amount in cents less than a dollar: "))
quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

print("\n"
      f"Q: {quarters}\n"
      f"D: {dimes}\n"
      f"N: {nickels}\n"
      f"P: {pennies}")

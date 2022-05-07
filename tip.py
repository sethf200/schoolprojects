print('''
 ____________________ 
|  ________________  |
| | Tip Calculator | |
| |________________| |
|____________________|
''')

#Get price from user, calculate 15 and 20 percent tip amount.

price = float(input("Please enter your total: "))

tip15 = price * 15 / 100

tip20 = price * 20 / 100

#Calculate totals for both 15 and 20 percent.

tip15Total = tip15 + price

tip20Total = tip20 + price

print(f"\n15%: ${tip15}")
print(f"\n20%: ${tip20}")

tipAmount = int(input("\n15 or 20 percent? "))

#Calculate total.
if tipAmount == 15:
    print(f"\nTip: ${tip15}")
    print(f"Total: ${tip15Total}")
    exit()
elif tipAmount == 20:
    print(f"\nTip: ${tip20}")
    print(f"Total: ${tip20Total}")
    exit()
else:
    
    print("\nSorry, I couldn't calculate that. Please enter 15 or 20 percent next time!")
    exit()








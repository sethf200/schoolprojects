print("""
     __________________
    |  ______________  |
    | | Taxes & fees | |
    | |______________| |
    |__________________|
        """)

basePrice = int(input("Base price of vehicle: "))


tax = basePrice * .06

license = basePrice * .05

dealerPrep = 2500

destinationCharge = 500 

grandTotal = basePrice + tax + license + dealerPrep + destinationCharge

print(f"""
        Base price: ${basePrice}
        Tax: 6%
        License fee: 5%
        Dealer prep: $2500
        Destination charge: $500
        """)

print(f"\nYour new total including taxes and fees is: ${grandTotal}")

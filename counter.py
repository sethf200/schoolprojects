#Counting program
#Asks a user what number to start from, end from, and the amount by which to count.
#Seth Foster

startnumber = int(input("Please enter a starting number: "))
endnumber = int(input("\nPlease enter an ending number: "))
amnttocount = int(input("\nAmount to count by: "))
print("")

for i in range(startnumber, endnumber, amnttocount):
    print(i)
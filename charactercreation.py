#Seth Foster
#This program is supposed to simulate character creation in a video game.

print("Create your character! You have 30pts to assign to each attribute. Choose carefully!")

attributes = {"Strength":0, "Health":0, "Wisdom":0, "Dexterity":0}

points = 30

while True:
    print("\nYou have", points, "points left")
    print("""
    1. Add points
    2. Remove points
    3. Show current stats
    4. Exit
    """)
    
    choice = int(input("Select an option in the menu: "))
    #If the user chooses choice 1, it sends them to a menu where they can select which attribute to add points to.
    if choice == 1:
       attrToEdit = int(input("""
       1. Strength
       2. Health
       3. Wisdom
       4. Dexterity
       
       Which attribute do you want to edit?(1-4): """))
       
       if attrToEdit == 1:
           ptsToAdd = int(input("How many points do you want to add? "))
           if ptsToAdd > points:
               print("\nNot enough points!")
           else:
               attributes["Strength"] += ptsToAdd
               points -= ptsToAdd
       
       elif attrToEdit == 2:
            ptsToAdd = int(input("How many points do you want to add? "))
            if ptsToAdd > points:
               print("\nNot enough points!")
            else:
               attributes["Health"] += ptsToAdd
               points -= ptsToAdd
       
       elif attrToEdit == 3:
           ptsToAdd = int(input("How many points do you want to add? "))
           if ptsToAdd > points:
               print("\nNot enough points!")
           else:
               attributes["Wisdom"] += ptsToAdd
               points -= ptsToAdd
       elif attrToEdit == 4:
           ptsToAdd = int(input("How many points do you want to add? "))
           if ptsToAdd > points:
               print("\nNot enough points!")
           else:
               attributes["Dexterity"] += ptsToAdd
               points -= ptsToAdd
       else:
           print("Invalid option!")

    #Same as above, except removes points!
    elif choice == 2:
       attrToEdit = int(input("""
       1. Strength
       2. Health
       3. Wisdom
       4. Dexterity
       
       Which attribute do you want to edit?(1-4): """))

       if attrToEdit == 1:
           ptsToRemove = int(input("How many points do you want to remove? "))
           if ptsToRemove > attributes["Strength"]:
               print("\nYou can't remove points that don't exist!")
           else:
               attributes["Strength"] -= ptsToRemove
               points += ptsToRemove
       
       elif attrToEdit == 2:
           ptsToRemove = int(input("How many points do you want to remove? "))
           if ptsToRemove > attributes["Health"]:
               print("\nYou can't remove points that don't exist!")
           else:
               attributes["Health"] -= ptsToRemove
               points += ptsToRemove
       
       elif attrToEdit == 3:
           ptsToRemove = int(input("How many points do you want to remove? "))
           if ptsToRemove > attributes["Wisdom"]:
               print("\nYou can't remove points that don't exist!")
           else:
               attributes["Wisdom"] -= ptsToRemove
               points += ptsToRemove
       
       elif attrToEdit == 4:
           ptsToRemove = int(input("How many points do you want to remove? "))
           if ptsToRemove > attributes["Dexterity"]:
               print("\nYou can't remove points that don't exist!")
           else:
               attributes["Dexterity"] -= ptsToRemove
               points += ptsToRemove
       else:
           print("Invalid option!")
       
    elif choice == 3:
        print("")
        print(attributes)
    
    elif choice == 4:
        exit()
    else:
        print("Sorry, invalid option!")





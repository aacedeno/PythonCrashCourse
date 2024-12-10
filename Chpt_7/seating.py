reserve = input('How many people are in your dinner party? ')
reserve = int(reserve)

if reserve > 8:
    print("Please wait for the next avaiable table")
else:
    print("Your table is ready, please follow me.")
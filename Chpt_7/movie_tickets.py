prompt = 'What is your age? '

while True:
    age = input(prompt)
    
    # Allow user to exit the loop by entering '0'
    if age == '0':
        print("Exiting the program. Goodbye!")
        break
    
    # Convert the input to an integer
    age = int(age)
    
    # Check the ticket price
    if age < 3:
        print('Ticket is free')
    elif 3 <= age <= 12:
        print('Ticket is $10')
    else:
        print("Your ticket costs $15.")

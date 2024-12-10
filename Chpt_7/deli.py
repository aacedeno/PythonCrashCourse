finished_sandwhiches = []
sandwhich_orders = ['Italian', 'Pastrami', 'Ham and Cheese', 'Pastrami', 'Chicken', 'Tuna', 'Pastrami']

print('We are out of Pastrami, sorry for the inconvience')

while 'Pastrami' in sandwhich_orders:
        sandwhich_orders.remove('Pastrami')

while sandwhich_orders:

    #Takes most recent order
    current_order = sandwhich_orders.pop()

    # if current_order == 'Pastrami':
    #     continue  # Skip adding it to finished_sandwiches or printing
    
    print(f'I made you {current_order}')
    finished_sandwhiches.append(current_order)

    #Checks on the amount of orders left 
    if len(sandwhich_orders) == 0:
        print('All sandwhiches have been made')
        print(finished_sandwhiches)






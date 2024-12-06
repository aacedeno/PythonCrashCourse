current_users = ['Mike', 'Dave', 'Sandra', 'KELLY', 'Jack']

# Convert all current usernames to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

new_users = ['Mike', 'Kelly', 'Katy', 'Brett', 'Pedro']


for user in new_users:
    if user.lower() in current_users_lower:
        print('Enter a new name')
    else:
        print("username is avaiable")

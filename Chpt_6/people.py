people = {
    'rmaxwell': {
        'first_name': 'Ryan',
        'last_name': 'Maxwell',
        'city': 'Chicago',
    },
    'mwebb': {
        'first_name': 'Mike',
        'last_name': 'Webb',
        'city': 'Miami',
    },
    'rsanchez': {
        'first_name': 'Mark',
        'last_name': 'Sanchez',
        'city': 'Dallas'
    }
}

for user, user_info in people.items():
    print(f'Username: {user}')
    full_name = (user_info['first_name'], user_info['last_name'])
    location = user_info['city']

    print(f'\tFull name: {full_name}')
    print(f'\tLocation: {location}')

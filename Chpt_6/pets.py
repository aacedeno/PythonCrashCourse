pets = {
    'cat': {
        'Name': 'Cosmos',
        'Owner': 'Bill',
        'Species': 'Feline',
    },
    'dog': {
        'Name': 'Zeus',
        'Owner': 'Mike',
        'Species': 'Cannine',
    },
    'bird': {
        'Name': 'Peter',
        'Owner': 'Tony',
        'Species': 'Aves'
    }
}

for animal, pet_info in pets.items():
    print(f'Animal: {animal}')
    print(f'Owner: \t{pet_info['Owner']}')
    print(f'Pet name: \t{pet_info['Name']}')
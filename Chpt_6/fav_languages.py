favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

poll_takers = ['jen', 'mike', 'phil', 'bill']

for name in poll_takers:
    if name in favorite_languages:
        print(f'Thanks for responding {name}')
    else:
        print(f'Please take some time to complete the poll {name}')

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
    }

rivers.update({'rio grande': 'brazil', 'yellow': 'china'})

for k, v in rivers.items():
    print(f'The {k} run through {v}')
    
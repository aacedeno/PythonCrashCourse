pizzas = ["cheese", "Sausage", "Vegan"]

friends_pizzas = pizzas[:]

pizzas.append('hawaiian')

friends_pizzas.append('meat lovers')

for i in pizzas:
    print(f'My favorite pizzas are: {i}')


for i in friends_pizzas:
    print(f'My favorite pizzas are: {i}')
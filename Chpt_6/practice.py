person = {"name": "John", "age": 30, "profession": "Engineer"}

print(person['age'])

person.update({'city': 'chicago'})
print(person['city'])
person['profession'] = 'lawyer'
print(person)


print(person.get('hobbies', 'No hobbies'))

print(person.pop('age'))
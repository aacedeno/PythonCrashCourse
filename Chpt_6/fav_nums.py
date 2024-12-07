fav_nums = {
    'Jack': ['4', '5', '10'],
    'Ryan': ['6', '2'],
    'Ricky': ['16'],
    'Emily': ['22', '36'],
    'Mike': ['3', '11']
}

# Values assigned to vars in for statement can be used later on in a different conditional statement 
for person, number in fav_nums.items():
    print(f'{person} faavorite number(s) are: ')
    #num is iterating through the list assinged to number 
    for num in number:
        print(f'\t{num}')
    

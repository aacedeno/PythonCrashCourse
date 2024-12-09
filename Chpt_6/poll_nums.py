fav_nums = {
    'Jack': '6',
    'Ryan': '8',
    'Ricky': '16',
    'Emily': '22',
    'Mike': '2'
}

#.key() is not needed since looping though the kery is a default behavior when looping through a dicitonary
for key in fav_nums:
    print(f'{key}', fav_nums[key])

for name, value in fav_nums.items():
    print(name, value)
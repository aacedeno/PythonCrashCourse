nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in nums:
    if n > 3:
        print(f'{n}th')
    elif n == 1:
        print(f'{n}st')
    elif n == 2:
        print(f'{n}nd')
    else:
        print(f'{n}rd')
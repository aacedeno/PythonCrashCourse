#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
#Make sure you use each character combination, "\t" and "\n", at least once.
#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

first_name = " Monica Webb "
second_name = "\tRyan Cedeno "
thrid_name = "\tJenny Smith\n"

print(first_name)
print(first_name.strip())

print(second_name)
print(second_name.lstrip())

print(thrid_name)
print(thrid_name.strip())
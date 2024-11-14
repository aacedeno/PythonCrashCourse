
#Use insert() to add one new guest to the beginning of your list.
#Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.

guest_list = ["MJ", "Messi", "Nelson"]

print(f"Hello, {guest_list[0]}, come join me for dinner")

print(f"Hello, {guest_list[1]}, come join me for dinner")

print(f"Hello, {guest_list[2]}, come join me for dinner")

print(f"{guest_list[2]} is not able to attend")

guest_list[2] = "Lebron"

print(guest_list)

print("I've found a bigger table")

guest_list.append("Kendrick")
guest_list.insert(0, "Drake")
guest_list.insert(2, "Tyreek")


print(guest_list)

#Use pop() to remove guests from list one at a time until only two naes remain in your list
#print a message to each of the two people still on your list
# Use del to remove the last 2 names deom your list so it's empty. Print the list to verify you have an empty list

guest_list = ["MJ", "Messi", "Nelson"]

print(f"Hello, {guest_list[0]}, come join me for dinner")

print(f"Hello, {guest_list[1]}, come join me for dinner")

print(f"Hello, {guest_list[2]}, come join me for dinner")

print(f"{guest_list[2]} is not able to attend")

guest_list[2] = "Lebron"

print("I've found a bigger table")

guest_list.append("Kendrick")
guest_list.insert(0, "Drake")
guest_list.insert(2, "Tyreek")

print("I have enough space for only 2 guests")

guest_removal = guest_list.pop()
print(f"{guest_removal} is no longer invited to the dinner party")

guest_removal_01 = guest_list.pop()
print(f"{guest_removal_01} is no longer invited to the dinner party")

guest_removal_02 = guest_list.pop()
print(f"{guest_removal_02} is no longer invited to the dinner party")

guest_removal_04 = guest_list.pop()
print(f"{guest_removal_04} is no longer invited to the dinner party")

print(f"{guest_list} are still invited to dinner party")

del guest_list[:]

print(guest_list)
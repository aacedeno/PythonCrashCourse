#Think of at least 5 places in the world you'd like to visit
#Store the locations in a list

world_travels = ["South Africa", "China", "New Zeleand", "Peru", "Vancouver"]

print(world_travels)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(world_travels))

#Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(sorted(world_travels,reverse=True))

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
world_travels.reverse()
print(world_travels)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order
world_travels.reverse()
print(world_travels)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
world_travels.sort()
print(world_travels)



#Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
world_travels.sort(reverse=True)
print(world_travels)
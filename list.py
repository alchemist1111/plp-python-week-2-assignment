# An empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert an element at the 2nd position of the list
my_list.insert(1, 15)

# Extend my_list with another list
new_list = [50, 60, 70]
my_list.extend(new_list)

# Remove the last element from the list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)

# Output the result
print(f"The index of 30 in the list is: {index_of_30}")
print("Final list after all operations:", my_list)

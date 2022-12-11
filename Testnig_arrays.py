import array

array_type = array.array('i',[1,2,3,4])

# Print the array
print(array_type)

# Print the type 
print(type(array_type))

# Print the length 
print(len(array_type))

# Print elements 

print(array_type[0])
print(array_type[-1])

# Print the index of an element

print(array_type.index(3))
try:
    print(array_type.index(10))
except ValueError:
    print("The value is not existed on the array")

# Looping through the array
for i in array_type:
    print(i) 

# Slicing the array

print(array_type[:2])

# Change the value of an element

print(array_type[0])

# Adding elements to the array

array_type.append(5)

print(array_type)

# Remove the value from the array

array_type.remove(5)

print(array_type)

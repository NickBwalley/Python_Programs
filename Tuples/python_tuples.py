# This are basically Immutable lists
# Declared using brackets()
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2)

tiny_tuple = (123, 'john')
print(tuple) # Prints complete list
print(tuple[0]) # Prints first element of the list
print(tuple[1:3]) # Prints elements starting from 2nd till 3rd
print(tuple[2:]) # Prints elements starting from 3rd element
print(tiny_tuple * 2) # Prints list two times
print(tuple + tiny_tuple) # Prints concatenated lists



# generator functions

# what?: 
# a function that returns an Iterated Object with a sequence of values when iterated over.
# generator functions are used to produce a large sequence of values, without storing all them in memory at once.

# How?
# the GF uses the YIELD key word instead of the RETURN key word. 

# ------YIELD Vs RETURN
# RETURN keyword - the functions result is not remembered by the call stack, so when the function runs again, the previous result is forgotten.

# YIELD keyword - when called the result of the function is remembered in state, so when the function runs again it continues from the previous result

# Use cases:
# when working with data streams or large files like csv files. used to create iterators for abstract containers.

# basic iterator:
my_iterator= iter([0,1,2,3,4,5])#creating an iterator object/instance data type 
print(next(my_iterator)) #output 0
print(next(my_iterator)) #output 1
print(next(my_iterator)) #output 2
print(next(my_iterator)) #output 3
next(my_iterator) #next returns next value in sequence
print(next(my_iterator))#output 5
print('-----------------------------')
# 


# basic generator func
def finite_sequence(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Create an instance of the generator function
gen = finite_sequence(30)
next(gen)# the next() return the next vallue in the iterator
print(type(gen))
print(next(gen))
# Iterate over the first X numbers in the sequence
# for i in range(10):
#     print(next(gen))


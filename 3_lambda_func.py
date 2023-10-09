# Lambda 
# what? :
# a lambda function is a simple nameless functions
# in python the lambda function is written in one line
# lambda function always return something

# when to use?: 
# it's best to use lambda functions inside other function
#when you need to return a result in just one simple line 


# normal function: 
def multiply(a,b):
    result = a*b
    return result

print(multiply(2,4))

# lambda functions

# e.g.1
greeting = lambda:'hello world'
print(type(greeting()))
print(greeting())

# e.g.2
result = lambda x,y: x * y
print(result(6,2))



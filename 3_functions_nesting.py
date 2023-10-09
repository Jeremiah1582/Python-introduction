# # basic function 
# def function_name(num1, num2):
#     value = num1 + num2
#     return value

# adding = function_name(2, 5)

# complexDataType=5j #the j at the end of the value represents a complexdatatype
# print(type(complexDataType))


# # renaming functions

# new_name_func = function_name #renaming a function
# print(new_name_func(2, 1))
# print(adding) 



# # parsing a function through a function
# # use cases:
# # we would pass a function into a function if we intend to modify the function
# def sub_func(a,b):
#     return a*b
    

# def wrapper_func(func):
#     print(func) #output signature of the function
#     x = func(5,5)
#     print(x)
#     return x
    
# wrapper_func(sub_func) #function parsing a function


# # Function returning a function
# def outer_func():
#     print('i am outer function !!!!! ')
#     def inner_func(): 
#         return ('i am inner function')
#     print('signature object of the INNER func, from within outer_func----',inner_func)
#     return inner_func #you don't initiate the function with (), this allows you to return the function object

# x=outer_func
# print('running outerfunction & inner function.... ',x()) 

# # print('the signature object of the INNER function....',outer_func()) #returns the signature object of the inner function 
# # print('the signature object of the OUTER function ...',outer_func) # returns the signature of the outer function 



# # ----------Higher Order functions & referring function-----------
# # higher order function:
# # a function that takes another function as an arg

# # referring function:
# # this is where you would pars a function into a function with arguements. then use the arguements inside the parsed arguement.

def sum(a,b):
    print(a*b)

# Higher Order Function:
def operation(func,args): #here we are parsing a func and array
    func(*args) #referring function: #calling the function, *unpacking the array and parsing as args
    
operation(sum,[2,5]) #calling our function


# closures: 
# this allows you to access local-function data outside of the function.
# allows you to remember the state inside of a function even after function has run
def make_printer(text):
    def printer():
        print(text)
    return printer
pr= make_printer('hello world')
pr()


# DEcorators concept -- design pattern 
# a closure that uses a function as an arg and uses it inside the function
def make_pretty(func):
    def inner():
        print('im a decorator')
        func()
        
    return inner


def ordinary():
    print("this is a decorator")
    
ordinary()
pretty = make_pretty(ordinary)
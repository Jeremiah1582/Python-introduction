# ------------------Decorators---------------
# what?
# decorators in python are used to add functionality to existing function
# 3 types of decorators: 
# 1 - function decorators
# 2 - class decorators
# 3 - method decorators

# how? 
# they work by parsing the OG-definned function into the decorator where additional functionality resides.
# this functionality is executed along with the og-func 
# decorators start with the @ symbol
# python will wraps your og-function in the decorators nested wrapper function automatically 


# why:
#reusability
#to save time- if you have 100's of functions that need the same abilities, adding a 
#decorator will will save you having to manually add features

# decorators
import time

# decorator 
def timer(func): #func reps the function decorated with the decorator (simple_func())
    
    # nested functionality below
    def wrapper_func(*args, **kwargs): #*args & **kwargs are equal to the input to the original function
        start = time.time()
        result= func(*args,**kwargs) #original function that is parsed in runs here
        end = time.time()
        print(end-start) # run time taken to run- decorator has done its job
        return result #return func results to wrapper
    
    return wrapper_func #return wrapper to timer
        


ran=0
@timer #adding functionality
def simple_func(num): #as this func has a decorator, the func will run inside the wrapper-function of the decorator 
    # for x in range(0,99):
    num =+1
    time.sleep(3)
    # print(x)
    return num
    
print(simple_func(ran))


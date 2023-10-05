# def functionName(num1, num2):
#     value = num1 + num2
#     return value

# adding = functionName(2, 5)

complexDataType=5j #the j at the end of the value represents a complexdatatype
print(type(complexDataType))

print('---------------Packing & Unpacking-----------')

# --------PACKING & UNPACKING----------
# Packing allows you to pass through an unlimited number of arguments
#*args -this is packing 
# args1,args2,args3 = args -this is unpacking
print('---------------Tuple Packing-----------')
#Tuple packing 
def full_name(*args):# *args is a tuple
    print(args[2])#output value_of_3rd_arg
    
    # OR !
    
    args1,args2,args3 = args #unpacking/destructuring in python 
    print(args1)
    
full_name('Jeremiah',28,'Berlin')



# dictionary Packing 
print('---------------Dictionary Packing-----------')
def full_name_dict(**kwargs):# **kwargs is a dict (key word arguments)
    print(kwargs) #output the entire dictionary 
    print(kwargs['name'])#returns Value of KEY
    
    # OR !
    
    kwarg1,kwarg2,kwarg3 =kwargs#dictionary Unpacking
    print(kwarg2)# returns KEY 
    print(kwargs[kwarg2])# returns VALUE 
    
full_name_dict(name='Jeremiah',age=28,city='Berlin')


print('-------------- mixed packing methods--------------')
# full packing 
def full_mix(*args,**kwargs):#
    print(args,kwargs)#output Tuple & Dictionary
    print(*args,*kwargs) #output Tuple Values, Dict Key 
   
    
    
full_mix(1,2,3,4,name= 'bob', city='Accra', age=15)
    

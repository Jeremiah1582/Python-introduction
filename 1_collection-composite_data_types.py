# ------------------Collections & Composite Data Types---------------------

# what?: 
# a Collection is a made up of multiple units of data. 
# a composite data type made up of different types of data types
# in python lists can be composite data types unlike Javascript arrays are just collections
# all composite data types are collections not all collections are composite data types

# -----------primitive data types---------
#String, Integer, Boolean, Long, Float, 
movie= "brave heart"
year=1999
isGood=True

# ----------Composite Data Types--------
# list
movieList= [movie,year,isGood]
print(movieList)

# Lists
myList = ['hello', 1234, {'who':'Kwame'}]
print(myList[2]['who']) #accessing the nested dict in python

# dictionary datatype
movieDict={ 
    "name":"brave heart",
    "year":1999,
    "isGood":True,
    "cast": {
        'lead': 'William Wallace', 
        'support': 'Robert Burns'
    }
}
# print(movieDict)
print(movieDict["year"])
print(movieDict["cast"]['lead'])
print(type(movieDict))

# Tuple
myFruitTuple=("grapes", "Mango", "kiwi", "Lemon")
print(type(myFruitTuple)) #output <class 'tuple'>
print(myFruitTuple[3]) #output Lemon 
print(myFruitTuple)

print(type(["hello", "1993", ""])) #output <class 'list'>






# coffee 



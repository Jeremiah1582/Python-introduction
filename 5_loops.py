# in this script we will learn:
# 1) how to write a FOR LOOP
# 2) how to write a WHILE LOOP
# 3) how to write a FOR LOOP that iterates through a DICTIONARY Data Structure/ COmposite dataType 


myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
# for loop
for item in myMixedTypeList:
     print(type(item))
   
# for loop + range() function
for x in range(1,25):
    print(x)
    
# while loop 
i=0
while i < 10:
    i+=1
    print(i)


# For loop with Dictionaries and KEY:VALUES
fruits = {
    "orange":74,
    "apples":65,
    "mango":74,
    "banana":0.54
    }    

for key,value in fruits.items():
    print(f"the {key} costs {value}")
     


     


     


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
    i+=1 #increment the 'i' variable
    print(i)
    
    
# infinate while loop: 
temp = 17
while True: 
    if temp<20:
        temp+=1
        print(f'turn on the heating {temp}')
        if temp ==20:
            break
    elif temp>20 and temp<25:
        print(f'temp is perfect {temp}')
        break
    elif temp>25:
        temp-=1
        print(f'turn on air conditioner {temp}') 
        if temp ==25:
            break 
    


# For loop with Dictionaries and KEY:VALUES
fruits = {
    "orange":74,
    "apples":65,
    "mango":74,
    "banana":0.54
    }    

veg = {
    'carrots': 10,
    'beets': 32,
    'corn': 15,
    'tomatoes':8,
    'cabbage': 14
}

# to expend the dictionary
fruit_veg = veg.copy()
fruit_veg.update(fruits)
print(fruit_veg)


# for key,value in fruit_veg.items():
    # print(f"the {key} costs {value}")

print({range(1,5):x for x in list(veg)})

     


     


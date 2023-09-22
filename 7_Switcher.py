# SWITCH 
# What?:
# you can create a switch function that returns a key's Value
#creating a switch function can reduce syntax compared to an 'if statement'.


# dictionary Switch hashed with number Keys
def switch_example(argument):
    my_switch = {
    0: "zero",
    1: "one",
    2: "two",
    } #this is a set switch and immutable
    return my_switch.get(argument, "your input argument doesn't exist")

print(switch_example(5))



# dictionary with string Keys Switch 
def switch_example2(argument):
    my_switch = {
    'none': "zero",
    'single': "one",
    'double': "two",
    } #this is a dictionary switch
    return my_switch.get(argument, "your input argument doesn't exist")

print(switch_example2('double'))

# Switch with an List
# this method doesn't make sense as it would be easier to access the LIST directly rather than through a func
def switch_example3(argument):
    my_switch = [
        "zero",
        "one",
        "two",
     ] #switch used with a List 
    if my_switch[argument] == my_switch.index(argument):
        return my_switch[argument]
    else:
        return "your input argument doesn't exist"
print(switch_example3(10))

# print(9+9)
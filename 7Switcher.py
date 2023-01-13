
def switch_example(argument):
    switcher = {
    0: "zero",
    1: "one",
    2: "two",
    }
    return switcher.get(argument, "nothing")

print(switch_example(1))
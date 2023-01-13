name= input("what is your name?:")
admin= "Jeremiah"
user= "User"

# Condition Statement
if name.lower() == admin.lower():
    print(f'Hello  {name} you activated the CONDITIONAL Statement, Welcome to procedural programming')
elif name.lower() == user.lower():
    print(f"hello {user}, you are dont have the same access as admin, But WELCOME anyway!")
else:
    print(f"You're not the right dude my guy...Sorry {name}!")




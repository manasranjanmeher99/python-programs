import re
def pass_check(password):
    strength=0
    # length check
    if len(password)<8:
        print("Password should be more then 8 character")
    else:
        strength+=1
    
    # uppercase
    if re.search(r'[a-z]',password):
        strength+=1
    else:
        print("Add upper case letter")

    #lowercase
    if re.search(r'[A-Z]',password):
        strength+=1
    else:
        print("Add upper case letter")

    # numbers check
    if re.search(r'\d',password):
        strength+=1
    else:
        print("Add integer number")
    
    # Special character
    if re.search(r'[,./?><:;|+_*&^%$#@!~]', password):
        strength+=1
    else:
        print("Add special character")
    
    if strength==5:
        return "strength password"
    elif strength>=3:
        return "Medium password"
    else:
        return "Week password"


password= input("Enter the password: ")
result = pass_check(password)
print(result)
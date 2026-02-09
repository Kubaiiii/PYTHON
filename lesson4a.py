# nested if statements 
# these are if statements inside other if statements

age = 1728              
weight = 20
if (age >= 16)  :
    if (weight >= 50) :
        print("You can donate")
    else :
        print("You are underweight")
else :
    print("You're too young to donate")
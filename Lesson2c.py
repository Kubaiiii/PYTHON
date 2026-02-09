# python dictionary 
person = {
    "Firstname" : "Trump" ,
    "Lastname" : "Diddy" ,
    "Age" : 75 ,
    "colors" : ["Blue" , "Green"] ,
    "salary" :100
}

# show output
print(person)

# print age
print(person["Age"])

# print salary
print(person["salary"])

# add new key value
person["passport"] = "B008Hn"

# show output
print(person)

# change age to 34
person["Age"] = 34

# show output
print(person)

# delete lastname
del person["Lastname"]

# show output
print(person)
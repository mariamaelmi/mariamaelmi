# dictionaries

person = {
    "name" : 'Alice',
    "age" : 17,
    "city" : 'New york'
}
print (person)

print (person['name'])
print (person['age'])

person ['name'] = 'Mary'
print (person)

# we can delete elements using the del keyword 
del person ['name']
print (person)
# we can add new keys to 
person ['address']='124 london street'
print (person)

#updating can be done using the update function 
person.update({"address": "500 london street"})
print(person)

# a dictionary can be cleared using the 'clear' function 
person.clear()
print (person)

# dictionary methods 
# return all of the keys to the dictionary
print (person.values)


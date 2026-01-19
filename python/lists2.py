# adding , replacing and removing items in a list 

# we can add items with append , insert and extend
fruits = [ 'apple', 'plums', ' cherrys']

fruits.append('orange') # append always add the items to the end of the lists 

print (fruits)

fruits.insert (0,'banana') # this locates the banana at the beginging of the list 

print (fruits)

fruits.extend(['pear', 'appricot']) # extend adds it in the end of the list 
print (fruits)

# we remove items with clear, remove and pop 
fruits.pop() #pop removes the last item of the list 
print(fruits)

fruits.remove('orange') # removes the specific 
print (fruits)

fruits.clear () # 
print(fruits)
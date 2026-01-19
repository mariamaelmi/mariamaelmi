# string formatting - format ()
name ="Alice"
age = 30
message ="my name is {} an i am {} years old".format(name,age)
print (message)


# string formatting -fstrings
message = f"my name is {name} and i am {age} years old." # better when you have a lot variables
print (message)
# string formatting -addition / concatenation
message = "my name is " + name + "and i am " +str(age) + "years old"
print(message)
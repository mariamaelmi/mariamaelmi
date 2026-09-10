try:
# a code that might raise an exception
  age = input ("please enter your age")
  age =int(age)
except:
  # a code that runs if an excpetion occurs
  print("Erro: unable to conver that into a number")
else:
  # a code that runs if theres no expception 
 print(f"Your age is {age}")
finally:
# a code that always runs
 print ("Programe finsihed ")
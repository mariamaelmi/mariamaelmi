# modules allow you to use other peoples code 
import math # includes lots of mathematical functions 
import datetime # lots of helper functions with date and time manipulation 
import timeit # can time programe code 

#DATETIME
current_date =datetime.datetime.now() # this is the current time you will be running the code, the date and time
print (current_date)

new_date= datetime.date(2026,9,3) # this just prints the date 
print (new_date)

# we can format the date however we would like:
print(new_date.strftime('%a'))
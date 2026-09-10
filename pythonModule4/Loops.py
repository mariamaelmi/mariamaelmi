# for loops 
# i is out iteration variable , essentially a tempory variable, range (5) is our iterable 
for i in range(5):
 print(i) # the code we are going to execute in each run. 
total =0 
for number in range(3): # remember this takes the value of 0,1,2

  print (f'current total: {total}')
  total = total + number
  print(f'new total: {total}')
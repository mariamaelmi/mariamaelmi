# if/else statements or conditional statements
response = input ("Have you completed your to do list?")
if response == 'yes':
    print ('Well done you have completed everything')
else:
    print ('Uh oh you still have some items to do')

# condition statements with multiple conditions 
temperature = 0

if temperature > 30:
     print('its a hot day')
elif temperature > 20:
    print ('its a warm day')
elif temperature >10:
    print ('its a cool day')
else: 
    print ('its a cold day') 
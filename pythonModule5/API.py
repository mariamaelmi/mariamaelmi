import requests 

response = requests.get('http://catfact.ninja/fact')
print (response.json())
print (response.status_code) # this tells us whether the response has been successful or not 

# lets look at another API for different request methods : 
import requests
# a get reques:
response = requests.get ('https://reqres.in/api/users?page=2')

print (response.status_code)
print (response.json())
# json , information exchange acroos the web 
import json
person ={
   "name": 'Alice',
   "age" : 25,
   "city" : "new york"
}
print (person)
json_person = json.dumps(person) # converts a python dictionary to a json string 
print (json_person)


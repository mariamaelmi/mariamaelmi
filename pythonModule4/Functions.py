# def defines the function 
# hello is the function 
# f is important because it makes the string an f-string, which lets you put a variable directly inside { }.

def Hello (name, job= 'developer'):
    print (f' {name} is a {job}')

Hello('Mary',)
# sometimes we want to 'return' the value 
def sum(a,b):
    return a+b
result =sum (5,10)
print (result )
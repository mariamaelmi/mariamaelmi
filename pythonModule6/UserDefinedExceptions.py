# create an exception for too high and too low
class ValueTooHigh (Exception):
    pass
class ValueTooLow (Exception):
    pass

try:
    input= int(input("please enter a number between 5 and 10:"))
    if input <5:
        raise ValueTooLow
    
    if input >10:
        raise ValueTooHigh
except:
    print("ERROR: please enter a number between 5 and 10")
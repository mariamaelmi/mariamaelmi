# using the raise keyword 
try:
    input= int(input("please enter a number between 5 and 10:"))
    if input <5 or input >10:
        #our input is not between 5 and 10 so we want to raise an expcetion 
        raise Exception
except:
    print("ERROR: please enter a number between 5 and 10")
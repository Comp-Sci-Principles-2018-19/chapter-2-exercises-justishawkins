time=int(input("what time is it")) 
long=int(input("how long do you want your alarm to be for?"))
longmodulo=long%24
alarmt=time+longmodulo
print("I will set off at", alarmt)
#x=5100 % 1400
#y=x+1400
#print(y)
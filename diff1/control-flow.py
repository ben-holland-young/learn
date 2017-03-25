#to choose between two options you can use an if else statement like this
this = True
if this == True:
    #Do this if the condition is true
    print("something")
else:
    print("something else")
    #If the condition isnt true do this

#To look for multiple conditions you can use elif
if this == True:
    #DO this
    print("something")
elif somethingElse == False:
    #DO this
    print("elif")
else:
    #This
    print("else")

#you could use it for numbers too
if 5 > 3 or 5 <= 6:
    print("do this")
else:
    print("do this instead")

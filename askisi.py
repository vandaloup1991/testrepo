import random
def randominteger():
    randomnumber=random.randint(1,100)
    return randomnumber
def askusernumber(message='Μάντεψε αριθμό'):
    usernumber=int(input(message))
    return usernumber
def numbercomparison( usernumber, randomnumber ):
    if usernumber < randomnumber:
        return 'Είναι μεγαλύτερος'
    elif usernumber > randomnumber :
        return 'Eίναι μικρότερος'
    elif usernumber==randomnumber:
        return 'ΣΥΓΧΑΡΗΤΗΡΙΑ ΤΟ ΒΡΗΚΕΣ!'

usercongratulated = False
letstart = True
while usercongratulated == True or letstart == True:
    numberofguesses = 0
    randomnumber = randominteger()
    usernumber = askusernumber()
    numberofguesses = numberofguesses + 1
    message = numbercomparison( usernumber, randomnumber )
    while message !='ΣΥΓΧΑΡΗΤΗΡΙΑ ΤΟ ΒΡΗΚΕΣ!':
        print(message)
        usernumber= askusernumber('Δοκίμασε ξανά')
        numberofguesses = numberofguesses + 1
        message = numbercomparison( usernumber, randomnumber )
print(message,"Σου πήρε {:} προσπάθειες".format(numberofguesses))
usercongratulated = True

                              

#PROJECT-2

import random
randNumber=random.randint(1,100)
print(randNumber)

userguess=None
guesses=0

while(userguess!=randNumber):
    userguess=int(input("Enter your guess ! "))
    guesses=guesses+1
    
    if(userguess==randNumber):
        print("You guessed it right !")
    else:
        if(userguess>randNumber):
            print("You guessed it wrong ! Enter a smaller number ")
        else:
             print("You guessed it wrong ! Enter a larger number ")  
        

print(f"You guessed the number in {guesses} guesses ")


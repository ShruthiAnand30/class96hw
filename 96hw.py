number = input("Guess a number (from 1-9)") 

import random
random.randint(1,9)

    if(number>=random):
        print("Your guess was too high, guess a number higher than ")
        print(number)
    elif(number<=random):
        print("Your guess was too low, guess a number lower than ")
        print(number)
    else:
        print("You Won, Congratulations")
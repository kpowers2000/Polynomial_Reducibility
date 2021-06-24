'''
Created on Jun 23, 2021

@author: keenan
'''
from polynomial import *
from modp import *
from finitefield import *
import time
import sys

def delay_print(s,t):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)


def main():
    tries = 1
    exit = 0
    print("Hello, I hope you are doing well! \nMy name is Reducibility Reader, and I am here to play a game. \nYour goal is to try and guess a polynomial that can't be reduced in a given finite field. \n")
    time.sleep(5)
    delay_print("Can you do it? Let's find out!",0.05)
    isYes = raw_input("\nIf you are ready to start the game, type 'yes' \nIf you want to play, but aren't sure what a finite field is, type 'finite' \n")
    
    if isYes.lower() == 'yes':
        field = raw_input("\nHooray! First lets set the parameters.  What do you want the characteristic of the field to be? \nP.S. Remember that the characteristic of a finite field should always be a prime number. \nP.P.S. If you do not know what the characteristic of a field is, type 'char': \n")
    elif isYes.lower() == 'finite':
        print("\nA finite field is a field that contains a finite number of elements.  \nFor simplicity you can imagine that the characteristic, or size, \nof a finite field to be the mod that acts on the coefficients of each polynomial.  \nThe characteristic of a field must be prime.  \nFor example, for a field F if char(F) = 3 then the coefficients for each x power can be 0, 1, or 3.  \nIn other words, x^2+4x+4 = x^2+x+1 in F3.  \nFinite fields can get interesting. To illustrate, lets look at x^2+x+1 again.  \nIt is irreducible in polynomials in the rational field or any of its subfields. \nHowever, it is reducible in F3 since (x+2)^2 = x^2+4x+4 which, as we said earlier, is the same as x^2+x+1 in mod 3 space.  Neat right?")
        field = raw_input("\nOkay, now this is interesting right?  Are you ready to start? Specify the characteristic of your finite field to continue \n")
    else: 
        print("\nOkay I guess you just aren't up for the challenge")
        return  
    if field.lower() == 'char':
        print("\nIn mathematics, the characteristic of a ring R (often denoted char(R)), \nis defined to be the smallest number of times one must sum the ring's \nmultiplicative identity (1) to get the additive identity (0). \nIf this sum never reaches the additive identity the ring is \nsaid to have characteristic zero. \n\nOkay, above is a pretty wordy definition.\nFor simplicity you can imagine that the characteristic, or size, \nof a finite field to be the mod that acts on the coefficients of each polynomial.  \nFor example, for a field F if char(F) = 3 then the coefficients for each x power can be 0, 1, or 3.  \nIn other words, x^2+4x+4 = x^2+x+1 in F3.  \nFinite fields can get interesting. To illustrate, lets look at x^2+x+1 again.  \nIt is irreducible in polynomials in the rational field or any of its subfields. \nHowever, it is reducible in F3 since (x+2)^2 = x^2+4x+4 which, as we said earlier, is the same as x^2+x+1 in the mod 3 space.  Neat right?")
        field = raw_input("\nStarting to understand the importance and fascinating math of abstract algebra are you?  \nGo ahead and input a number so I know what finite space we are dealing with \n\nNote: make sure the characteristic is a prime number!")
        
    field2 = int(field)
    print("\nGreat! Now its time to find a polynomial that reduces in F%d " % field2)
    time.sleep(1.5)
    print("\nI have 3 requirements on the polynomials that you give me:  \nFirst, the coefficients must all be nonnegative integers.  \nSecond, the coefficients of your polynomial should be typed in increasing degree \n with a space in between each letter (ex: 1 2 0 3 1 = 1 + 2x + 3x^4 + x^5). \nThird, the leading coefficient (which is the last number you will type) must be 1. \n so 2 4 3 1 is valid, but 2 4 3 2 is not.  \nGood luck trying to find an irreducible polynomial")
    poly = raw_input("\nPlease type the coefficients of the polynomial in the format specified above\n")
    while exit == 0:
        
        delay_print("the polynomial you gave me is\n", 0.05)
        field2 = int(field)
    
        Zp = IntegersModP(field2)
        Polynomial = polynomialsOver(Zp)
        coefficients = [Zp(s) for s in poly.split(' ')]
        poly = Polynomial(coefficients)
        print(poly)
        delay_print("Working my magic...",.03)
        time.sleep(.2)
        delay_print("Calculating possibilities...",.03)
        time.sleep(.2)
        delay_print("Almost finished andddddddd \nDone!",.03)
        time.sleep(.1)
    
        irreducible = isIrreducible(poly, field2)
        if irreducible:
            print("\nCongratualtions, you win! The polynomial you entered is irreducible!")
            if tries == 1:
                delay_print("Wow, you got it on your first try.  You're a polynomial pro.  Play again in a different field to increase you irreducible intuition.", .01)
            if tries <= 3:
                delay_print("Wow, it only took you %d tries.  You might be a polynomial pro." % tries, .01)
            elif tries <=5:
                delay_print("You did pretty good, it took you %d tries.  Play again to become a polynomial pro." % tries, .01)
            else:
                delay_print("It took you %d tries. Good job, though you still have a long way to go to become a polynomial pro." % tries, .01)
            break
        else:
            print("\nLooks like I win this round, the polynomial you entered can be reduced. Keep trying!\n")
        
        delay_print("Number of tries: %d" % tries, .04)
        poly = raw_input("\nPlease type the coefficients of the polynomial in the format specified above.\n Or, if you wish to quit, just type 'q'\n")
        if poly.lower() == 'q':
            print("Well, I'm sorry to hear that :(")
            break
        tries = tries + 1
    print("\nIf you have any questions about abstract algebra or this code, feel free to email me @keenan.f.powers27@gmail.com\n Have a nice day!")
    return



if __name__ == '__main__':
    main()

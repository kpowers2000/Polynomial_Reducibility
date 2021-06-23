'''
Created on Jun 23, 2021

@author: keenan
'''
from polynomial import *
from modp import *
from finitefield import *


def main():
    isYes = raw_input("Hello, I hope you are doing well! \nMy name is Reducibility Checker, and I am here to help \nIs your polynomial reducible? Let's find out! \nAre you ready to get started?  \nType 'yes' if you are. ")
    
    if isYes.lower() == 'yes':
        poly = raw_input("Hooray!  Please type the coefficients of your polynomial in increasing degree with a space in between each letter. \nFor example 1 2 0 3 equates to 1 + 2x + 3x^4 ")
    else: 
        print("Okay!  Sorry I could not be of more service to you.")
    field = raw_input("Great! Could you also tell me characteristic of the field. \nIf you do not know this please type 'help': ")
    print("Working my magic...")
    if field.lower() == 'help':
        print("In mathematics, the characteristic of a ring R (often denoted char(R)), \nis defined to be the smallest number of times one must use the ring's \nmultiplicative identity (1) in a sum to get the additive identity (0). \nIf this sum never reaches the additive identity the ring is \nsaid to have characteristic zero.")
        return
    else:
        field2 = int(field)
    Zp = IntegersModP(field2)
    Polynomial = polynomialsOver(Zp)
    coefficients = [Zp(s) for s in poly.split(' ')]
    poly = Polynomial(coefficients)
    print(poly)
    
    irreducible = isIrreducible(poly, field2)
    if irreducible:
        print("Hooray! The polynomial you entered is irreducible!")
    else:
        
        print("Oops! Looks like the polynomial you entered can be reduced. Keep trying!")
    return



if __name__ == '__main__':
    main()

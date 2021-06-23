'''
Created on Jun 23, 2021

@author: keenan
'''
from finitefield import isIrreducible


def main():
    poly = input("Hello, I hope you are doing well! My name is Reducibility Checker, and I am here to help you find out if your polynomial is reducible or not. Let's get to it!  Can you enter the polynomial you wish to check:")
    field = input("Great! Could you also tell me characteristic of the field.  If you do not know this please type 'Help':")
    print("Working my magic...")
    '''TODO: If characteristic of the field is 0'''
    if field.lower() == "help":
        print("In mathematics, the characteristic of a ring R, often denoted char(R), is defined to be the smallest number of times one must use the ring's multiplicative identity (1) in a sum to get the additive identity (0). If this sum never reaches the additive identity the ring is said to have characteristic zero.")
    canReduce = isIrreducible(poly, field)
    if canReduce == 1:
        print("Oops! Looks like the polynomial you entered can be reduced. Keep trying!")
    elif canReduce == 0:
        print("Hooray! The polynomial you entered is irreducible!")
    if canReduce == -1:
        print("Error")
    return



if __name__ == '__main__':
    main()

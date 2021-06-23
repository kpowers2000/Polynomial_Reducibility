from finitefield import generateIrreduciblePolynomial
from finitefield import generateRandomDegreePolynomial
from finitefield import generatePolynomial
from finitefield import isIrreducibleV3
from finitefield import isIrreducible
import modp
import numbertype
import euclidean
import polynomial

def main():
    mod = 7
    degree = 15
    myBool = True
    for i in range(100):
        
        randPoly = generatePolynomial(mod,degree)
        if isIrreducibleV3(randPoly,mod) != isIrreducible(randPoly, mod):
            print(randPoly)
            print(isIrreducibleV3(randPoly, mod))
            print(isIrreducible(randPoly, mod))
            myBool = False
        randPoly2 = generateRandomDegreePolynomial(mod)
        if isIrreducibleV3(randPoly2, mod) != isIrreducible(randPoly2, mod):
            print(randPoly2)
            print(isIrreducibleV3(randPoly2, mod))
            print(isIrreducible(randPoly2, mod))
            myBool = False
    
    
    print("Results incoming...")
    print(myBool)
    return


if __name__ == '__main__':
    main()
'''
Created on Apr 19, 2021

@author: keenan
'''

from polynomial import polynomialsOver
from euclidean import *
from modp import *



def toPowP(p,d,r):
    oldCoefs = r.getCoefs()
    
    newCoefs = [0]*p*len(oldCoefs)
      #create list of size p*m where m is the deg(r)
    #create coefs for r^p = a0 + a1x^p +a2x^2p + ... + am-1x^(p(m-1)) + amx^pm
    for i in range(len(oldCoefs)):
        newCoefs[p*i] = oldCoefs[i]
    return polynomialsOver(r.field)(newCoefs)

#input (p,d,poly) and output gcd such that s(x^p-x) + t(f(x)) = a = gcd(x^p-x,f(x)).
def shortCut(p,d,poly):
    #where p is prime and is p in Fp
        
    ZmodP = IntegersModP(p)
    if poly.field is not ZmodP:
        raise TypeError("Given a polynomial that's not over %s, but instead %r" %
                        (ZmodP.__name__, poly.field.__name__))
    #coefs = [0]*(p+1)
    #coefs[-1] = 1
    #r = polynomialsOver(ZmodP)(coefs).factory
    r = polynomialsOver(ZmodP).factory
    r = r([0,1])
    #loop through finding remainder (in mod f(x)) d times
    for i in range(d):
        
        #take r to the pth power
        #find the remainder in mod f
        r = r.powmod(p,poly)
        #q, r = divmod(r,poly)
        #r = toPowP(p,d,r)
        
    #q, r = divmod(r,poly)
    gc =gcd(r-polynomialsOver(poly.field)([0,1]),poly)
        
    return gc











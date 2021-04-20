'''
Created on Apr 19, 2021

@author: keenan
'''

from polynomial import polynomialsOver
from euclidean import *
from modp import *

""""
f(x) = x^n+an-1x^n-1… a0

Euclid 

(1) Let temp = x
Loop
(2)Take temp to the pth power (temp2 = temp^p)
(3)temp2 = f(x)*q(x) + r1(x); find r1(x)
→ x^p = r1(x) in quotient ring→ xp^2 = (r1(x))p = rmpxpm + … + r0 =rmxpm + … + r0 

…

Let temp = r1(x)
(5) end at rd(x)
Go to (2)
x^p^d -x = rd(x) -x 
Check if gcd(rd(x)-x,f(x)) = 1*c where c is constant 
If it equals 1 for all d|n st n/d is prime then f(x) is irreducible
"""

def toPowP(p,d,r):
    oldCoefs = r.getCoefs()
    m = abs(r)
    newCoefs = [0]*p*m  #create list of size p*m where m is the deg(r)
    #create coefs for r^p = a0 + a1x^p +a2x^2p + ... + am-1x^(p(m-1)) + amx^pm
    for i in range(p):
        newCoefs[p*i] = oldCoefs[i]
    return polynomialsOver(r.field)(newCoefs)

#input (p,d,poly) and output gcd such that s(x^p-x) + t(f(x)) = a = gcd(x^p-x,f(x)).
def shortCut(p,d,poly):
    #where p is prime and is p in Fp
    ZmodP = IntegersModP(p)
    if poly.field is not ZmodP:
        raise TypeError("Given a polynomial that's not over %s, but instead %r" %
                        (ZmodP.__name__, poly.field.__name__))
    r = polynomialsOver(ZmodP)([0,1])
    #loop through finding remainder (in mod f(x)) d times
    for j in range(d):
        #take r to the pth power
        for i in range(p):
            r = r*r
        #find the remainder in mod f
        q, r = divmod(r,poly)
        
    gcd =gcd(r-polynomialsOver(poly.field)([0,1]),poly)
        
    return gcd











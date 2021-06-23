# Polynomial_Reducibility
This program was created to analyze the reducibility of polynomials in finite fields.  There is a 
  polynomial and finite field class, as well as a Euclidean algorithm. These classes and function are to
  apply the the theorem that f(x) is irreducible if and only if for any d|n with d!=n, gcd(f,x^p^d−x) = 1 
  and f|x^p^n−x.

A proof for this theorem can be found here https://drive.google.com/file/d/1qumikcTN5DQCxDQScuSVCYEqGjtUHgIN/view?usp=sharing

Give it a try!!!! As of June 23 2021, there is now an interactive program I instituted where you can specify a polynomial 
and our Reducibility Reader will test the polynomial for irreducibility in a given finite field.

For a more in depth discussion on this topic please refer to https://drive.google.com/file/d/1pyuoHKK0tJjoAwWCbR_JKdif784hjFz5/view?usp=sharing
This document is broken into 3 parts
Part a) Proof of theorem (1)
Part b) Analysis of code and its complexity
Part c) Analysis of irreducible polynomials and patterns that form
  
Here is pseudocode that gives the basic logical progression of the program
1. Create polynomial, poly=x
2. Let i = 0
3. If i == n/2 then the polynomial is irreducible. Exit 
4. i = i + +
5. Let poly=polyp mod f(x)
6. If n mod i == 0, then go to step (7), otherwise, return to step (3).
7. Find gcd(f(x), poly − x)
8. If gcd 6= c ∈ Fp, then the polynomial is irreducible. Exit
9. Return to step (3).

Note: this uses a generalized conclusion of the proof given above: 
f(x) is irreducible if and only if gcd(f,x^p^d−x) = 1 for all d < n/2 (not just d|n) and f|x^p^n−x.

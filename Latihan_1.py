import math
from this import s 

def a(x) :
    return x**2

def b(x, y):
    return math.sqrt(x**2 + y**2)

def c(*args):
    return sum(args)/len(args)

def d(S):
    return "".join(set(s))

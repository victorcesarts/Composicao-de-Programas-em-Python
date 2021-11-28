from functools import reduce

def firstChars(L):
    if not L:
        return None
    else:
        return map(lambda x: x[0][0], L)

def sum(L):
    if not L:
        return None
    else:
        return reduce(lambda x, y: x + y, L)

def avg(L):
    if not L:
        return None
    else:
        length = len(L)
        return sum(L)/length
     
def maxString(L):
    if not L:
        return None
    else:
        return max(L, key=len)

def add2Dict(D, N, S):
    D[N] = D[N] + [S] if N in D else [S]
    return D

def buildLenFreq(L):
    if not L:
        return None
    else:
        dictL = {}
        reduce(lambda D, x: add2Dict(D, len(x), x), L, dictL)
        return dictL
          
def incValue(D, N):
    D[N] = D[N] + 1 if N in D else 1
    return D

def countFirsts(L):
    if not L:
        return None
    else:
        dictL = {}
        reduce(lambda dictL, x: incValue(dictL, x), firstChars(L), dictL)
        return dictL

def mostCommonFirstChar(L):
    if not L:
        return None
    else:
        v = countFirsts(L)
        return max(v, key=v.get)
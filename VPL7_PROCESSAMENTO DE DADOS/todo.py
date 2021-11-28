def lastNames(L):
    if not L:
        return None
    else:
        return map(lambda x: x[-1], L)

def citations(L):
    newL = list(L)
    if not newL:
        return None
    else:
        last = list(lastNames(newL))
        return map(lambda x, y: x[0][0].capitalize()+ '.'+y, newL, last)
        
def getLetters(N, last):
    length = len(N)
    i = 0
    firstLetters = []
    while i < length:
        firstLetters.append(N[i][0].capitalize()+'.')
        i += 1
    firstLetters.append(last)
    return firstLetters
    
def fullCitations(L):
    newL = list(L)
    if not newL:
        return None
    else:
        N = map(lambda x: x[0:len(x)-1], newL)
        last = list(lastNames(newL))
        return map(getLetters, N, last)
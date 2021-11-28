from functools import reduce

def delInitials(L):
    return [S.capitalize() for S in L if S.isalpha() if len(S) > 1]

def everyOccurrence(S, Q):
    return [a for a, b in enumerate(S) for c in Q if c == b]

def factors(N):
    return [div for div in range(2, N-1) if N % div == 0]

def isPerfect(N):
    return(True if sum(factors(N))+1 == N else False)
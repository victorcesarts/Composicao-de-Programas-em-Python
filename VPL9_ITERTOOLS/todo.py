from itertools import *

# The list of week days:
dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

# The list of possible shifts: Day or Night.
periodos = ["D", "N"]

def buildTurns(profs):
    turns = product(dias, periodos)
    tXprof = zip(turns, cycle(profs), count(1))
    return ([a, b, c, d] for (a, b), c, d in tXprof)

def printCSV(profs):
    print("indice, dia, periodo, profissional")
    turns = list(buildTurns(profs))
    for (dia, periodo, profissional, indice) in turns:
        print ("%s, %s, %s, %s" %(indice, dia, periodo, profissional))
    return 'fim'

def firstDay(profs, prof):
    if prof in profs:
        turns = buildTurns(profs)
        firstD = list(dropwhile(lambda x: not x[2] == prof, turns))
        return firstD[0][0]
    else:
        return "Inexistente"

def countTurns(profs, prof):
    if prof in profs:
        turns = list(buildTurns(profs))
        numbTurn = len(list(filter(lambda x: x[2] == prof, turns)))
        return numbTurn
    else:
        return 0

def payTurns(profs, prof):
    if prof in profs:
        turns = list(buildTurns(profs))
        tD = 1000
        tN = 1333
        salary = 0
        numbTurn = list(filter(lambda x: x[2] == prof, turns))
        for periodo in numbTurn:
            if periodo[1] == 'D':
                salary += tD
            else:
                salary += tN        
        return salary
    else:
        return 0
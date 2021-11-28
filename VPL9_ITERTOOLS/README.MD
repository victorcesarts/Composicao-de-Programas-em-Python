# Módulo Itertools

(Esses exercícios/códigos fazem parte do curso "Composição de Programas em Python" oferecido pelo DCC/UFMG)

    def buildTurns(profs):
        """Esta funcao recebe uma lista profs de profissionais, e constroi uma
        lista de tuplas. Cada tupla possui quatro elementos:
        - Um dia da semana;
        - Um periodo de trabalho (dia ou noite);
        - Um nome de profissional
        - Um indice indicando qual eh aquele turno. O primeiro turno (Seg/D) possui
        indice 1. O segundo turno (Seg/N) possui indice 2, o terceiro turno (Ter/D)
        possui indice 3, e assim por diante.
        """

    def printCSV(profs):
        """Esta funcao recebe uma lista de profissionais, e imprime uma tabela
        CSV com os turnos, usando as colunas: indice, dia, periodo e profissional:
        """

    def firstDay(profs, prof):
        """Esta funcao imprime o primeiro dia em que trabalha o profissional 'prof'.
        Caso 'prof' nao esteja presente na lista profs, ou nao exista em um turno
        valido, a funcao precisa retornar a string 'Inexistente'
        """

    def countTurns(profs, prof):
        """Esta funcao retorna o numero de turnos em que trabalha o profissional
        'prof'. Caso 'prof' nao trabalhe em algum turno, entao a funcao retorna
        zero.
        """

    def payTurns(profs, prof):
        """Esta funcao retorna o salario semanal de um profissional, assumindo que
        cada turno diurno lhe paga 1000 e cada turno noturno lhe paga 1333.
        Caso 'prof' nao trabalhe em algum turno, a funcao deve retornar zero.
        """
# Processamento de Dados
(Esses exercícios/códigos fazem parte do curso "Composição de Programas em Python" oferecido pelo DCC/UFMG)

Neste exercício, assim como nos anteriores, você deverá completar algumas funções disponíveis em um arquivo todo.py. O arquivo possui 3 funções que precisam ser completadas.
    São as funções:
    
    lastNames(L): 
        Mapeia uma lista de nomes para o ultimo nome de cada item.
        Por exemplo, seja:
        L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
        Então lastNames(L) == ['Franco', 'Vitelus', 'Buarque']

    citations(L):
        Mapeia uma lista de nomes para a primeira letra mais sobrenome.
        Por exemplo, seja:
        L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
        entao citations(L) = ['A. Franco', 'C. Vitelus', 'C. Buarque']
        Note que a primeira letra precisa estar capitalizada.

    fullCitations(L):
        Mapeia uma lista de nomes para as iniciais mais o ultimo nome.
        Por exemplo, seja:
        L = [
        ['Antonio', 'Franco', 'Molina'],
        ['Caius', 'vitelus', 'Aquarius'],
        ['cristovao', 'buarque', 'Holanda']]
        então fullCitations(L) = ['A. F. Molina', 'C. V. Aquarius', 'C. B. Holanda']
        Note que as iniciais precisam estar capitalizada.
 

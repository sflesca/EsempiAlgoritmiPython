# implementare un metodo che riceva in input un alberobinario e restituisca il livello più piccolo in cui appare una foglia, sollevare eccezione se albero nullo
from alberi.alberibinari import AlberoBin


def minlivellofogli(a: AlberoBin) ->int:
    if a is None:
        raise ValueError
    return 0 #TOTO

# implementare un metodo che riceva in input un alberobn a e un intero l e restituisca vero se tutti i nodi che appaiono al livello l hanno valore 0
def tuttizero(a:AlberoBin, l: int)-> bool:
    pass

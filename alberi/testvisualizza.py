from alberibinari import AlberoBin
from visualizzaalberi import write_png   # o nel file dove hai messo la funzione

r = AlberoBin(50)
r.setfigliosin(AlberoBin(30))
r.setfigliodes(AlberoBin(70))
r.sin.setfigliosin(AlberoBin(20))
r.sin.setfigliodes(AlberoBin(40))

write_png(r, "mio_albero")
# → salva mio_albero.png nella directory corrente
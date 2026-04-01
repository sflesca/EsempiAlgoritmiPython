"""
Albero AVL — implementazione basata su AlberoBin/ABR esistenti.

Ogni nodo memorizza il fattore di bilanciamento (bf = altezza(des) - altezza(sin)).
Valori ammessi: -1, 0, +1.  Valori fuori range innescano una rotazione.

Parametro di debug
------------------
Passare  debug_rotazioni=True  al costruttore di AVL per abilitare la
generazione automatica di immagini PNG (via graphviz) prima e dopo ogni
rotazione.  I file vengono salvati nella directory corrente con nomi del tipo:
    rot_001_prima.png
    rot_001_dopo.png
"""

from __future__ import annotations
from graphviz import Digraph


# ---------------------------------------------------------------------------
# Nodo AVL
# ---------------------------------------------------------------------------

class NodoAVL:
    """Nodo di un albero AVL.

    Attributi
    ---------
    val    : valore memorizzato
    sin    : figlio sinistro (NodoAVL | None)
    des    : figlio destro  (NodoAVL | None)
    parent : nodo padre     (NodoAVL | None)
    bf     : fattore di bilanciamento  =  altezza(des) - altezza(sin)
             valori leciti: -1, 0, +1
    """

    def __init__(self, val):
        self.val = val
        self.sin: NodoAVL | None = None
        self.des: NodoAVL | None = None
        self.parent: NodoAVL | None = None
        self.bf: int = 0          # fattore di bilanciamento

    # ------------------------------------------------------------------ repr
    def __repr__(self):
        return f"NodoAVL(val={self.val}, bf={self.bf})"


# ---------------------------------------------------------------------------
# Classe principale AVL
# ---------------------------------------------------------------------------

class AVL:
    """Albero AVL (Adelson-Velsky e Landis).

    Parametri
    ---------
    debug_rotazioni : bool
        Se True, genera un'immagine PNG dell'albero prima e dopo ogni
        rotazione.  Richiede graphviz installato (pip install graphviz +
        pacchetto di sistema graphviz).
    cartella_output : str
        Cartella in cui salvare le immagini di debug (default: '.').
    """

    def __init__(self, debug_rotazioni: bool = False, cartella_output: str = "."):
        self.radice: NodoAVL | None = None
        self.debug_rotazioni = debug_rotazioni
        self.cartella_output = cartella_output
        self._contatore_rotazioni = 0   # usato per numerare i file PNG

    # ================================================================ search
    def search(self, val) -> bool:
        """Restituisce True se val è presente nell'albero."""
        return self._search(self.radice, val) is not None

    def _search(self, curr: NodoAVL | None, val) -> NodoAVL | None:
        """Ricerca standard su BST; restituisce il nodo o None."""
        if curr is None:
            return None
        if curr.val == val:
            return curr
        elif val < curr.val:
            return self._search(curr.sin, val)
        else:
            return self._search(curr.des, val)

    # ================================================================ min/max
    def min(self):
        """Valore minimo dell'albero (None se vuoto)."""
        if self.radice is None:
            return None
        curr = self.radice
        while curr.sin is not None:
            curr = curr.sin
        return curr.val

    def max(self):
        """Valore massimo dell'albero (None se vuoto)."""
        if self.radice is None:
            return None
        curr = self.radice
        while curr.des is not None:
            curr = curr.des
        return curr.val

    # ================================================================ insert
    def insert(self, val):
        """Inserisce val nell'albero AVL mantenendo il bilanciamento."""
        if self.radice is None:
            self.radice = NodoAVL(val)
            return

        # Inserimento BST standard
        padre = self._trova_padre_inserimento(self.radice, val)
        if padre is None or padre.val == val:
            return          # valore già presente, non inseriamo duplicati

        nuovo = NodoAVL(val)
        nuovo.parent = padre
        if val < padre.val:
            padre.sin = nuovo
        else:
            padre.des = nuovo

        # Risalita per aggiornare bf e, se necessario, ribilanciare
        self._aggiorna_bf_dopo_inserimento(nuovo)

    def _trova_padre_inserimento(self, curr: NodoAVL, val) -> NodoAVL | None:
        """Restituisce il nodo che diventerà padre del nuovo nodo."""
        if curr.val == val:
            return curr     # duplicato
        if val < curr.val:
            if curr.sin is None:
                return curr
            return self._trova_padre_inserimento(curr.sin, val)
        else:
            if curr.des is None:
                return curr
            return self._trova_padre_inserimento(curr.des, val)

    def _aggiorna_bf_dopo_inserimento(self, nodo: NodoAVL):
        """Risale verso la radice aggiornando i fattori di bilanciamento.
        Si ferma quando il bilanciamento non propaga ulteriormente o
        quando esegue una rotazione (che ripristina l'altezza del sottoalbero).
        """
        curr = nodo
        while curr.parent is not None:
            padre = curr.parent
            if padre.sin == curr:
                padre.bf -= 1   # il sottoalbero sinistro è cresciuto
            else:
                padre.bf += 1   # il sottoalbero destro è cresciuto

            if padre.bf == 0:
                # L'altezza del sottoalbero radicato in padre NON è cambiata
                break
            elif padre.bf in (-1, 1):
                # L'altezza è cambiata ma il nodo è ancora bilanciato: continua
                curr = padre
            else:
                # |bf| == 2 → serve una rotazione
                self._bilancia(padre)
                break   # la rotazione ripristina l'altezza: propagazione finita

    # ================================================================ delete
    def delete(self, val):
        """Rimuove val dall'albero AVL mantenendo il bilanciamento."""
        nodo = self._search(self.radice, val)
        if nodo is None:
            return

        # Caso con due figli: sostituiamo con il successore in-order
        if nodo.sin is not None and nodo.des is not None:
            successore = nodo.des
            while successore.sin is not None:
                successore = successore.sin
            nodo.val = successore.val
            nodo = successore   # ora dobbiamo rimuovere il successore (≤ 1 figlio)

        # Ora nodo ha al massimo un figlio
        figlio = nodo.sin if nodo.sin is not None else nodo.des
        padre = nodo.parent

        if figlio is not None:
            figlio.parent = padre

        if padre is None:
            self.radice = figlio
        elif padre.sin == nodo:
            padre.sin = figlio
            padre.bf += 1       # il sottoalbero sinistro è diminuito
        else:
            padre.des = figlio
            padre.bf -= 1       # il sottoalbero destro è diminuito

        # Stacca nodo dall'albero
        nodo.parent = None
        nodo.sin = None
        nodo.des = None

        # Risalita per aggiornare bf e ribilanciare
        if padre is not None:
            self._aggiorna_bf_dopo_cancellazione(padre)

    def _aggiorna_bf_dopo_cancellazione(self, nodo: NodoAVL):
        """Risale verso la radice dopo una cancellazione."""
        curr = nodo
        while curr is not None:
            if curr.bf == 0:
                # L'altezza del sottoalbero è diminuita: continuiamo a risalire
                curr = curr.parent
            elif curr.bf in (-1, 1):
                # L'altezza NON è cambiata: propagazione finita
                break
            else:
                # |bf| == 2 → rotazione
                padre_dopo = self._bilancia(curr)
                # Dopo la rotazione il bf della radice del sottoalbero ruotato
                # potrebbe essere 0 (altezza diminuita) o ±1 (altezza invariata)
                if padre_dopo.bf == 0:
                    curr = padre_dopo.parent
                else:
                    break

    # ================================================================ bilancia
    def _bilancia(self, z: NodoAVL) -> NodoAVL:
        """Applica la rotazione necessaria al nodo z (|bf| == 2).

        Restituisce la nuova radice del sottoalbero ruotato.
        """
        if z.bf == -2:
            y = z.sin
            if y.bf <= 0:
                # Caso Sinistra-Sinistra  →  rotazione destra semplice
                return self._rotazione_destra(z)
            else:
                # Caso Sinistra-Destra    →  doppia rotazione sin-des
                self._rotazione_sinistra(y)
                return self._rotazione_destra(z)
        else:   # z.bf == +2
            y = z.des
            if y.bf >= 0:
                # Caso Destra-Destra      →  rotazione sinistra semplice
                return self._rotazione_sinistra(z)
            else:
                # Caso Destra-Sinistra    →  doppia rotazione des-sin
                self._rotazione_destra(y)
                return self._rotazione_sinistra(z)

    # ============================================================= rotazioni
    def _rotazione_destra(self, z: NodoAVL) -> NodoAVL:
        """Rotazione a destra intorno a z.  Restituisce la nuova radice (y)."""
        if self.debug_rotazioni:
            self._salva_immagine_debug("prima", z, "RD")

        y = z.sin
        T3 = y.des

        # --- esegui rotazione ---
        y.parent = z.parent
        if z.parent is None:
            self.radice = y
        elif z.parent.sin == z:
            z.parent.sin = y
        else:
            z.parent.des = y

        y.des = z
        z.parent = y
        z.sin = T3
        if T3 is not None:
            T3.parent = z

        # --- aggiorna fattori di bilanciamento ---
        # Usando le formule derivate dall'analisi delle altezze:
        #   bf(z)_nuovo = bf(z)_vecchio - 1 - max(bf(y)_vecchio, 0)
        #   bf(y)_nuovo = bf(y)_vecchio - 1 + min(bf(z)_nuovo, 0)
        z.bf = z.bf + 1 - min(y.bf, 0)
        y.bf = y.bf + 1 + max(z.bf, 0)

        if self.debug_rotazioni:
            self._salva_immagine_debug("dopo", y, "RD")

        return y

    def _rotazione_sinistra(self, z: NodoAVL) -> NodoAVL:
        """Rotazione a sinistra intorno a z.  Restituisce la nuova radice (y)."""
        if self.debug_rotazioni:
            self._salva_immagine_debug("prima", z, "RS")

        y = z.des
        T2 = y.sin

        # --- esegui rotazione ---
        y.parent = z.parent
        if z.parent is None:
            self.radice = y
        elif z.parent.sin == z:
            z.parent.sin = y
        else:
            z.parent.des = y

        y.sin = z
        z.parent = y
        z.des = T2
        if T2 is not None:
            T2.parent = z

        # --- aggiorna fattori di bilanciamento ---
        z.bf = z.bf - 1 - max(y.bf, 0)
        y.bf = y.bf - 1 + min(z.bf, 0)

        if self.debug_rotazioni:
            self._salva_immagine_debug("dopo", y, "RS")

        return y

    # ======================================================== debug / graphviz
    def _salva_immagine_debug(self, fase: str, radice_sottoalbero: NodoAVL, tipo_rot: str):
        """Genera un PNG dell'intero albero, evidenziando il sottoalbero coinvolto.

        fase         : 'prima' | 'dopo'
        tipo_rot     : 'RD' (rotazione destra) | 'RS' (rotazione sinistra)
        """
        if fase == "prima":
            self._contatore_rotazioni += 1

        numero = self._contatore_rotazioni
        nome_file = f"{self.cartella_output}/rot_{numero:03d}_{tipo_rot}_{fase}"

        # Raccogli gli id dei nodi del sottoalbero per evidenziarli
        nodi_coinvolti = set()
        self._raccogli_id(radice_sottoalbero, nodi_coinvolti)

        dot = Digraph(
            graph_attr={"rankdir": "TB", "label": f"Rotazione {tipo_rot} — {fase}",
                        "labelloc": "t", "fontsize": "16"},
            node_attr={"shape": "circle", "style": "filled",
                       "fontname": "Helvetica", "fontsize": "12"}
        )

        def _aggiungi(nodo: NodoAVL | None):
            if nodo is None:
                return
            evidenziato = id(nodo) in nodi_coinvolti
            fillcolor = "#FF8C00" if evidenziato else "#E6F1FB"
            color     = "#8B4500" if evidenziato else "#185FA5"
            label     = f"{nodo.val}\nbf={nodo.bf}"
            dot.node(str(id(nodo)), label=label,
                     fillcolor=fillcolor, color=color)
            if nodo.sin is not None:
                dot.edge(str(id(nodo)), str(id(nodo.sin)), label="S")
                _aggiungi(nodo.sin)
            if nodo.des is not None:
                dot.edge(str(id(nodo)), str(id(nodo.des)), label="D")
                _aggiungi(nodo.des)

        _aggiungi(self.radice)
        dot.render(nome_file, format="png", cleanup=True)
        print(f"[debug] immagine salvata: {nome_file}.png")

    def _raccogli_id(self, nodo: NodoAVL | None, risultato: set):
        if nodo is None:
            return
        risultato.add(id(nodo))
        self._raccogli_id(nodo.sin, risultato)
        self._raccogli_id(nodo.des, risultato)

    # ================================================= utility / ispezione
    def visita_infissa(self) -> list:
        """Restituisce i valori in ordine crescente."""
        l = []
        self._infissa(self.radice, l)
        return l

    def _infissa(self, nodo: NodoAVL | None, l: list):
        if nodo is None:
            return
        self._infissa(nodo.sin, l)
        l.append(nodo.val)
        self._infissa(nodo.des, l)

    def altezza(self) -> int:
        """Altezza dell'albero (0 se vuoto)."""
        return self._altezza(self.radice)

    def _altezza(self, nodo: NodoAVL | None) -> int:
        if nodo is None:
            return 0
        return 1 + max(self._altezza(nodo.sin), self._altezza(nodo.des))

    def is_bilanciato(self) -> bool:
        """Verifica (ricorsivamente) che tutti i bf siano in {-1, 0, 1}."""
        return self._check_bf(self.radice)

    def _check_bf(self, nodo: NodoAVL | None) -> bool:
        if nodo is None:
            return True
        if nodo.bf not in (-1, 0, 1):
            return False
        return self._check_bf(nodo.sin) and self._check_bf(nodo.des)

    def stampa_struttura(self, nodo: NodoAVL | None = None, indent: int = 0,
                         prefisso: str = "R: "):
        """Stampa l'albero in forma testuale indentata (utile per debug rapido)."""
        if indent == 0:
            nodo = self.radice
        if nodo is None:
            print(" " * indent + prefisso + "None")
            return
        print(" " * indent + prefisso + f"{nodo.val} (bf={nodo.bf})")
        self.stampa_struttura(nodo.sin, indent + 4, "S: ")
        self.stampa_struttura(nodo.des, indent + 4, "D: ")

    def write_png(self, filename: str = "avl_albero") -> None:
        """Genera un PNG dell'intero albero AVL (indipendente dal debug)."""
        dot = Digraph(
            graph_attr={"rankdir": "TB"},
            node_attr={"shape": "circle", "style": "filled",
                       "fillcolor": "#D4EDDA", "color": "#155724",
                       "fontname": "Helvetica", "fontsize": "14"}
        )

        def _aggiungi(nodo: NodoAVL | None):
            if nodo is None:
                return
            dot.node(str(id(nodo)), label=f"{nodo.val}\nbf={nodo.bf}")
            if nodo.sin is not None:
                dot.edge(str(id(nodo)), str(id(nodo.sin)), label="S")
                _aggiungi(nodo.sin)
            if nodo.des is not None:
                dot.edge(str(id(nodo)), str(id(nodo.des)), label="D")
                _aggiungi(nodo.des)

        _aggiungi(self.radice)
        dot.render(filename, format="png", cleanup=True)
        print(f"Immagine salvata in: {filename}.png")


# ---------------------------------------------------------------------------
# Piccolo test manuale
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Test AVL ===")

    # --- inserimento con debug rotazioni abilitato ---
    avl = AVL(debug_rotazioni=True, cartella_output="./screen")

    valori = [10, 20, 30, 15, 25, 5, 3, 7]
    for v in valori:
        avl.insert(v)
        print(f"Inserito {v:3d}  |  altezza={avl.altezza()}  |  bilanciato={avl.is_bilanciato()}")

    print("\nVisita infissa (deve essere ordinata):", avl.visita_infissa())
    print()
    avl.stampa_struttura()

    # --- ricerca ---
    for v in [10, 25, 99]:
        print(f"search({v}) = {avl.search(v)}")

    # --- cancellazione ---
    print("\n--- Cancellazione ---")
    for v in [20, 10, 3]:
        avl.delete(v)
        print(f"Eliminato {v:3d}  |  altezza={avl.altezza()}  |  bilanciato={avl.is_bilanciato()}")
        print("  visita infissa:", avl.visita_infissa())

    avl.write_png("avl_finale")
from graphviz import Digraph

from alberi.alberibinari import AlberoBin


def write_png(root: AlberoBin, filename: str = "albero") -> None:
    """
    Genera un'immagine PNG dell'albero binario radicato in `root`.
    Equivalente di t.pydot_graph().write_png("bst.png") di binarytree.

    Parametri:
        root     - nodo radice (istanza di AlberoBin)
        filename - nome del file di output, senza estensione

    Requisiti:
        pip install graphviz
        apt install graphviz  (oppure brew install graphviz su macOS)
    """
    dot = Digraph(graph_attr={"rankdir": "TB"},
                  node_attr={"shape": "circle", "style": "filled",
                             "fillcolor": "#E6F1FB", "color": "#185FA5",
                             "fontname": "Helvetica", "fontsize": "14"})

    def _aggiungi_nodi(nodo: AlberoBin) -> None:
        if nodo is None:
            return
        dot.node(str(id(nodo)), label=str(nodo.val))
        if nodo.sin is not None:
            dot.edge(str(id(nodo)), str(id(nodo.sin)))
            _aggiungi_nodi(nodo.sin)
        if nodo.des is not None:
            dot.edge(str(id(nodo)), str(id(nodo.des)))
            _aggiungi_nodi(nodo.des)

    _aggiungi_nodi(root)
    dot.render(filename, format="png", cleanup=True)
    print(f"Immagine salvata in: {filename}.png")
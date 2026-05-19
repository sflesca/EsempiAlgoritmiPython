"""
Algoritmo di Huffman - Compressione dati senza perdita
=======================================================
Implementazione completa con:
  - Costruzione dell'albero di Huffman
  - Generazione dei codici binari
  - Codifica (encoding) e decodifica (decoding) di una stringa
"""

import heapq
from collections import Counter


# ── Nodo dell'albero ──────────────────────────────────────────────────────────

class Nodo:
    """Rappresenta un nodo dell'albero di Huffman."""

    def __init__(self, carattere, frequenza):
        self.carattere = carattere   # None per i nodi interni
        self.frequenza = frequenza
        self.sinistro  = None
        self.destro    = None

    # Necessario per il min-heap: confronto basato sulla frequenza
    def __lt__(self, altro):
        return self.frequenza < altro.frequenza

    def __repr__(self):
        return f"Nodo({self.carattere!r}, {self.frequenza})"


# ── Costruzione dell'albero ───────────────────────────────────────────────────

def costruisci_albero(testo: str) -> Nodo:
    """
    Costruisce l'albero di Huffman a partire da un testo.

    1. Conta le frequenze di ogni carattere.
    2. Inserisce tutti i nodi foglia in un min-heap.
    3. Unisce iterativamente i due nodi con frequenza minore
       finché non rimane un solo nodo (la radice).
    """
    if not testo:
        raise ValueError("Il testo non può essere vuoto.")

    frequenze = Counter(testo)

    # Min-heap: ogni elemento è un Nodo foglia
    heap = [Nodo(car, freq) for car, freq in frequenze.items()]
    heapq.heapify(heap)

    # Caso speciale: un solo carattere distinto
    if len(heap) == 1:
        unico = heapq.heappop(heap)
        radice = Nodo(None, unico.frequenza)
        radice.sinistro = unico
        heapq.heappush(heap, radice)
        return radice

    while len(heap) > 1:
        minimo1 = heapq.heappop(heap)
        minimo2 = heapq.heappop(heap)

        nodo_interno = Nodo(None, minimo1.frequenza + minimo2.frequenza)
        nodo_interno.sinistro = minimo1
        nodo_interno.destro   = minimo2

        heapq.heappush(heap, nodo_interno)

    return heapq.heappop(heap)  # radice dell'albero


# ── Generazione dei codici ────────────────────────────────────────────────────

def genera_codici(radice: Nodo) -> dict[str, str]:
    """
    Percorre l'albero in profondità (DFS) e assegna a ogni
    carattere il suo codice binario (0 = sinistro, 1 = destro).
    """
    codici = {}

    def dfs(nodo: Nodo, codice_corrente: str):
        if nodo is None:
            return
        # Nodo foglia → salva il codice
        if nodo.carattere is not None:
            codici[nodo.carattere] = codice_corrente or "0"
            return
        dfs(nodo.sinistro, codice_corrente + "0")
        dfs(nodo.destro,   codice_corrente + "1")

    dfs(radice, "")
    return codici


# ── Codifica ──────────────────────────────────────────────────────────────────

def codifica(testo: str, codici: dict[str, str]) -> str:
    """Converte il testo in una stringa di bit usando i codici di Huffman."""
    return "".join(codici[c] for c in testo)


# ── Decodifica ────────────────────────────────────────────────────────────────

def decodifica(bit_string: str, radice: Nodo) -> str:
    """
    Percorre l'albero seguendo i bit (0 = sinistra, 1 = destra)
    e ricostruisce il testo originale.
    """
    risultato = []
    nodo_corrente = radice

    for bit in bit_string:
        nodo_corrente = nodo_corrente.sinistro if bit == "0" else nodo_corrente.destro

        if nodo_corrente is None:
            raise ValueError("Stringa di bit non valida per questo albero.")

        if nodo_corrente.carattere is not None:   # foglia trovata
            risultato.append(nodo_corrente.carattere)
            nodo_corrente = radice                # riparti dalla radice

    return "".join(risultato)


# ── Stampa dell'albero (opzionale) ────────────────────────────────────────────

def stampa_albero(nodo: Nodo, prefisso: str = "", è_sinistro: bool = True):
    """Visualizzazione ASCII dell'albero di Huffman."""
    if nodo is None:
        return
    connettore = "├── " if è_sinistro else "└── "
    etichetta  = repr(nodo.carattere) if nodo.carattere is not None else f"[{nodo.frequenza}]"
    print(prefisso + connettore + f"{etichetta} (freq={nodo.frequenza})")

    estensione = "│   " if è_sinistro else "    "
    stampa_albero(nodo.sinistro, prefisso + estensione, è_sinistro=True)
    stampa_albero(nodo.destro,   prefisso + estensione, è_sinistro=False)


# ── Demo ──────────────────────────────────────────────────────────────────────

def demo(testo: str):
    print("=" * 60)
    print(f"TESTO ORIGINALE : {testo!r}")
    print(f"Lunghezza       : {len(testo)} caratteri")
    print("=" * 60)

    # 1. Frequenze
    frequenze = Counter(testo)
    print("\n📊 Frequenze dei caratteri:")
    for car, freq in sorted(frequenze.items(), key=lambda x: -x[1]):
        print(f"   {car!r:6} → {freq}")

    # 2. Albero
    radice = costruisci_albero(testo)
    print("\n🌲 Albero di Huffman:")
    stampa_albero(radice)

    # 3. Codici
    codici = genera_codici(radice)
    print("\n💡 Codici di Huffman:")
    for car, codice in sorted(codici.items(), key=lambda x: len(x[1])):
        print(f"   {car!r:6} → {codice}")

    # 4. Codifica
    bit_string = codifica(testo, codici)
    print(f"\n🔐 Testo codificato ({len(bit_string)} bit):")
    print(f"   {bit_string}")

    # 5. Statistiche di compressione
    bit_originali   = len(testo) * 8          # 8 bit per carattere (ASCII)
    bit_compressi   = len(bit_string)
    risparmio       = (1 - bit_compressi / bit_originali) * 100
    print(f"\n📦 Statistiche di compressione:")
    print(f"   Bit originali (ASCII 8-bit) : {bit_originali}")
    print(f"   Bit compressi (Huffman)     : {bit_compressi}")
    print(f"   Risparmio                   : {risparmio:.1f}%")

    # 6. Decodifica (verifica)
    testo_decodificato = decodifica(bit_string, radice)
    corretto = testo_decodificato == testo
    print(f"\n✅ Decodifica corretta: {corretto}")
    print(f"   {testo_decodificato!r}")
    print("=" * 60)


if __name__ == "__main__":
    demo("ciao mondo, questo è un testo di esempio per huffman!")
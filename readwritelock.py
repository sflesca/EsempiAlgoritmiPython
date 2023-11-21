from threading import Thread,RLock,Condition, current_thread
from random import random
from time import sleep

#
# Funzione di stampa sincronizzata
#
plock = RLock()
debug = True
def dprint(s):
    if debug:
        plock.acquire()
        print(s)
        plock.release()

class DatoCondiviso():

    def __init__(self,v):
        self.dato = v
        self.numLettori = 0
        self.ceUnoScrittore = False
        self.lock = RLock()
        self.condition = Condition(self.lock)

    def getDato(self):
        return self.dato
    
    def setDato(self, i):
        self.dato = i


    def acquireReadLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} prova a prendere il lock in lettura")
        while self.ceUnoScrittore:
            dprint(f"Il thread {current_thread().name} voleva leggere ma trova che c'è uno scrittore. Dunque aspetta.")
            self.condition.wait()
        self.numLettori += 1
        dprint(f"Il thread {current_thread().name} prende il lock in lettura")
        self.lock.release()

    def releaseReadLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} rilascia il lock in lettura")
        self.numLettori -= 1
        if self.numLettori == 0:
            self.condition.notify()
        self.lock.release()

    def acquireWriteLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} prova a prendere il lock in scrittura")

        while self.numLettori > 0 or self.ceUnoScrittore:
            dprint(f"Il thread {current_thread().name} voleva scrivere, ma trova che ci sono {self.numLettori} lettori e che ceUnoScrittore={self.ceUnoScrittore}. Dunque aspetta.")
            self.condition.wait()
        self.ceUnoScrittore = True
        dprint(f"Il thread {current_thread().name} acquisisce il lock in scrittura")
        self.lock.release()

    def releaseWriteLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} rilascia il lock in scrittura")
        self.ceUnoScrittore = False
        self.condition.notify_all()
        self.lock.release()



class DatoCondivisoSenzaStarvation(DatoCondiviso):
    SOGLIAGIRI = 5

    def __init__(self,v):
        super().__init__(v)
        self.numScrittoriInAttesa = 0
        self.numGiriSenzaScrittori = 0

    def acquireReadLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} prova a prendere il lock in lettura")

        while self.ceUnoScrittore or \
              (self.numScrittoriInAttesa > 0 and self.numGiriSenzaScrittori > self.SOGLIAGIRI):
            dprint(f"Il thread {current_thread().name} trova che {self.numScrittoriInAttesa} scrittori sono in attesa e sono passati {self.numGiriSenzaScrittori} giri senza scrittori. Dunque aspetta")
            self.condition.wait()
        self.numLettori += 1
        # 
        # 		 * Il contatore viene incrementato solo se effettivamente ci sono
        # 		 * scrittori in attesa.
        # 		 
        if self.numScrittoriInAttesa > 0:
            self.numGiriSenzaScrittori += 1
        dprint(f"Il thread {current_thread().name} prende il lock in lettura")
        self.lock.release()

    def releaseReadLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} rilascia il lock in lettura")
        self.numLettori -= 1
        # 
        # 	Nella versione senza starvation, possono esserci anche dei lettori in attesa. 
        #   E' necessario
        #   dunque svegliare tutti.
        # 			 
        if self.numLettori == 0:
            self.condition.notify_all()
        self.lock.release()

    def acquireWriteLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} prova a prendere il lock in scrittura")
 
        self.numScrittoriInAttesa += 1
        while self.numLettori > 0 or self.ceUnoScrittore:
            dprint(f"Il thread {current_thread().name} trova che ci sono {self.numLettori} lettori in attesa e che ceUnoScrittore è {self.ceUnoScrittore}. Dunque aspetta")
            self.condition.wait()
        self.ceUnoScrittore = True
        self.numScrittoriInAttesa -= 1
        self.numGiriSenzaScrittori = 0
        dprint(f"Il thread {current_thread().name} prendere il lock in scrittura")
        self.lock.release()

# Resta uguale a DatoCondiviso
#     def releaseWriteLock(self):
#         lock.acquire()
#         ...
#         lock.release()

class Scrittore(Thread):
    
    maxIterations = 1000

    def __init__(self, i, dc):
        super().__init__()
        self.id = i
        self.dc = dc
        self.iterations = 0

    def run(self):
        while self.iterations < self.maxIterations:
            self.dc.acquireWriteLock()
            sleep(random())
            self.dc.setDato(self.id)
            self.dc.releaseWriteLock()
            sleep(random() * 5)
            self.iterations += 1


class Lettore(Thread):
    maxIterations = 100

    def __init__(self, i, dc):
        super().__init__()
        self.id = i
        self.dc = dc
        self.iterations = 0

    def run(self):
        while self.iterations < self.maxIterations:
            self.dc.acquireReadLock()
            sleep(random())
            self.dc.releaseReadLock()
            sleep(random() * 5)
            self.iterations += 1
  

if __name__ == '__main__':
        #
        #  Per testare il programma, si può usare DatoCondivisoSenzaStarvation oppure DatoCondiviso
        #
        #dc = DatoCondivisoSenzaStarvation(999)
        dc = DatoCondiviso(999)

        NUMS = 5
        NUML = 20

        scrittori = [Scrittore(i,dc) for i in range(NUMS)]
        lettori = [Lettore(i,dc) for i in range(NUML)]
        for s in scrittori:
            s.name = f"Scrittore {s.id}"
            s.start()
        for l in lettori:
            l.name = f"Lettore {l.id}"
            l.start()



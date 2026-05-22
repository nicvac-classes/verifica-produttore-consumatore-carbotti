import threading
import random

DIM_BUFFER = 5
N_PRODUTTORI = 3
N_CONSUMATORI = 2
N_ORDINI = 6

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_ordine():
    return f"ORD-{random.randint(10000, 99999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)


class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)


def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]

    # DA IMPLEMENTARE: start dei thread produttori e consumatori

    # DA IMPLEMENTARE: join di tutti i produttori

    print("Tutti i canali hanno terminato. Chiusura addetti...")

    # Invia un messaggio None per ogni addetto.
    for _ in range(N_CONSUMATORI):
        # DA IMPLEMENTARE: inserire None nel buffer
        pass

    # DA IMPLEMENTARE: join di tutti i consumatori

    print("Magazzino chiuso.")


if __name__ == "__main__":
    main()

import threading
import random

DIM_BUFFER = 7
N_PRODUTTORI = 4
N_CONSUMATORI = 3
N_RICHIESTE = 4

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_drone():
    return f"DRN-{random.randint(100, 999)}"


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

    print("Tutti i sensori hanno terminato. Chiusura piste...")

    # Invia una sentinella None per ogni pista attiva.
    for _ in range(N_CONSUMATORI):
        # DA IMPLEMENTARE: inserire None nel buffer
        pass

    # DA IMPLEMENTARE: join di tutti i consumatori

    print("Torre operativa chiusa.")


if __name__ == "__main__":
    main()

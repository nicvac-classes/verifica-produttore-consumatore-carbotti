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
        self.codice_drone = genera_drone()

    def run(self):
        global metti

        RICHIESTE_ESEGUITE = 0

        while RICHIESTE_ESEGUITE < N_RICHIESTE:

            vuoto.acquire()
            mutexP.acquire()
            i_metti = metti
            metti = (metti + 1) % DIM_BUFFER
            mutexP.release()
            buffer[i_metti] = self.codice_drone
            RICHIESTE_ESEGUITE += 1
            self.codice_drone = genera_drone()
            print(f"[SENSOR-{self.idx}] segnala {self.codice_drone}")
            pieno.release()

class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    def run(self):
        global togli

        termina = False

        while not(termina):

            pieno.acquire()
            mutexC.acquire()
            i_togli = togli
            togli = (togli + 1) % DIM_BUFFER
            mutexC.release
            codice_drone = buffer[i_togli]

            if codice_drone == None:
                termina = True
                print("CODICE DRONE UGUALE A NONE, ERRORE")
            else:
                print(f"[RUNWAY-{self.idx}] autorizza atterraggio {codice_drone}")
                   
            vuoto.release()


def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]

    # DA IMPLEMENTARE: start dei thread produttori e consumatori
    for p in produttori:
        p.start()

    for c in consumatori:
        c.start()

    # DA IMPLEMENTARE: join di tutti i produttori


    for p in produttori:
        p.join()


    print("Tutti i sensori hanno terminato. Chiusura piste...")

    # Invia una sentinella None per ogni pista attiva.
    for _ in range(N_CONSUMATORI):

        vuoto.acquire()
        buffer[metti] = None
        metti = (metti + 1) % DIM_BUFFER
        pieno.release()
        pass

    # DA IMPLEMENTARE: join di tutti i consumatori
    
   
    print("Torre operativa chiusa.")

    for c in consumatori:
        c.join()


if __name__ == "__main__":
    main()

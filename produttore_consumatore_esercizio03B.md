# Esercizio B — Torre di controllo droni

Una torre di controllo riceve richieste di atterraggio da sensori distribuiti nell'area aeroportuale. Ogni richiesta viene inserita in una coda condivisa (buffer circolare); le piste disponibili prelevano le richieste e autorizzano l'atterraggio.

## Parametri

| Parametro | Valore |
|---|---|
| `DIM_BUFFER` | 7 |
| `N_PRODUTTORI` (sensori radar) | 4 |
| `N_CONSUMATORI` (piste attive) | 3 |
| Richieste per sensore | 4 |

Ogni richiesta è una stringa con codice drone generato casualmente, ad esempio `"DRN-773"`. La funzione `genera_drone()` è già fornita nel codice base.

## Cosa devi implementare

Il file di partenza contiene già il `main` e la funzione `genera_drone()`. Devi implementare le due classi thread e completare i blocchi `DA IMPLEMENTARE` nel `main`.

### `ProduttoreThread`

Ogni sensore (produttore) deve:

1. Generare esattamente `N_RICHIESTE` richieste di atterraggio, poi terminare.
2. Per ogni richiesta, usare il protocollo con `vuoto`, `mutexP`, `i_metti`, `pieno`.
3. Stampare `[SENSOR-N] segnala <codice_drone>` dopo aver scritto nel buffer.

### `ConsumatoreThread`

Ogni pista (consumatore) deve:

1. Girare in loop indefinito, prelevando una richiesta alla volta con il protocollo `pieno`, `mutexC`, `i_togli`, `vuoto`.
2. Se la richiesta prelevata è `None`, uscire dal loop (sentinella di terminazione).
3. Stampare `[RUNWAY-N] autorizza atterraggio <codice_drone>`.

### `main`

Nel `main` devi completare i blocchi marcati `DA IMPLEMENTARE` per:

1. Avviare i thread produttori e consumatori.
2. Eseguire la `join` dei produttori.
3. Eseguire la `join` dei consumatori.

## Codice di partenza
- [produttore_consumatore_esercizio03B.py](produttore_consumatore_esercizio03B.py)

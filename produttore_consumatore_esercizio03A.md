# Esercizio A — Magazzino ordini e imballaggio

Un sistema e-commerce riceve ordini da diversi canali di vendita. Ogni ordine viene inserito in una coda condivisa (buffer circolare); gli addetti all'imballaggio prelevano gli ordini e li preparano per la spedizione.

## Parametri

| Parametro | Valore |
|---|---|
| `DIM_BUFFER` | 5 |
| `N_PRODUTTORI` (canali shop) | 3 |
| `N_CONSUMATORI` (addetti packing) | 2 |
| Ordini per canale | 6 |

Ogni ordine è una stringa con ID generato casualmente, ad esempio `"ORD-10573"`. La funzione `genera_ordine()` è già fornita nel codice base.

## Cosa devi implementare

Il file di partenza contiene già il `main` e la funzione `genera_ordine()`. Devi implementare le due classi thread e completare i blocchi `DA IMPLEMENTARE` nel `main`.

### `ProduttoreThread`

Ogni canale (produttore) deve:

1. Generare esattamente `N_ORDINI` ordini, poi terminare.
2. Per ogni ordine, usare il protocollo con `vuoto`, `mutexP`, `i_metti`, `pieno` che hai studiato.
3. Stampare `[SHOP-N] creato ordine <id_ordine>` dopo aver scritto nel buffer.

### `ConsumatoreThread`

Ogni addetto (consumatore) deve:

1. Girare in loop indefinito, prelevando un ordine alla volta con il protocollo `pieno`, `mutexC`, `i_togli`, `vuoto`.
2. Se l'ordine prelevato è `None`, uscire dal loop (segnale di terminazione inviato dal `main`).
3. Stampare `[PACK-N] prepara <id_ordine>`.

### `main`

Nel `main` devi completare i blocchi marcati `DA IMPLEMENTARE` per:

1. Avviare i thread produttori e consumatori.
2. Eseguire la `join` dei produttori.
3. Eseguire la `join` dei consumatori.

## Codice di partenza
- [produttore_consumatore_esercizio03A.py](produttore_consumatore_esercizio03A.py)

import matplotlib.pyplot as plt # Importazione della libreria utile alla visualizzazione esterna al terminale
import numpy as np # Importazione libreria utile al riempimento automatico delle tabelle
import random  # Importazione libreria per riempire le tabelle di 1 in modo casuale
import time # Importazione libreria utile alla creazione di un delay tra le visualizzazioni

plt.figure() # Creazione della forma in cui verra visualizzato l'output


righe = int(input("Inserisci il numero di righe della matrice: "))
colonne = int(input("Inserisci il numero di colonne della matrice: "))


tabella=np.zeros((righe,colonne)) # Creazione di un array di tutti zeri
appoggio=np.zeros((righe,colonne)) # Creazione di un secondo array di appoggio copia del precedente utile a stampare l'output dell'evoluzione senza errori
totale=righe*colonne

random_vive = int(totale*30/100) # Inserimento di un numero di 1 che sia pari a circa il 30% delle celle totali dell'array

i = 0
j = 0
numvive=0 # Inizializzazione della variabile di appoggio che permette a tutte le regole di funzionare

posizioniCasuali = np.random.choice(range(totale), random_vive, replace=False) # Scelta delle posizioni casuali in cui inserire gli 1 ed inserimento

for posizione in posizioniCasuali:
    riga, colonna = divmod(posizione, colonne)
    tabella[riga][colonna] = 1


print(np.array(tabella))

# Funzione per visualizzare la matrice
delay=3

def visualizza_matrice(matrice):
    plt.imshow(matrice, cmap='binary')
    plt.pause(0.1)
    plt.show(block=False)

visualizza_matrice(tabella)

# Sezione delle funzioni

def regoleVive(): # Funzione delle regole applicate alla singola cella qualora il valore contenuto fosse 1 

    if numvive < 2:
        appoggio[i][j] = 0
    
    if numvive == 2 or numvive == 3:
        appoggio[i][j] = 1

    if numvive >= 4 :
        appoggio[i][j] = 0

def regoleMorte():  # Funzione delle regole applicate alla singola cella qualora il valore contenuto fosse 0 

    if numvive == 3:
        appoggio[i][j] = 1
    else: 
        appoggio[i][j] = 0


def angoloNordOvest(): # Confronti necessari al funzionamento della cella [0][0]

    global numvive

    if tabella[0][1] == 1:
        numvive=numvive+1

    if tabella[1][1] == 1:
        numvive=numvive+1 

    if tabella[1][0] == 1:
        numvive=numvive+1  

    if tabella[i][j] == 0:
        regoleMorte()
    else:
        regoleVive()

def angoloNordEst(): # Confronti necessari al funzionamento della cella [0][colonne-1]

    global numvive

    if tabella[0][colonne-2] == 1:
        numvive=numvive+1

    if tabella[1][colonne-2] == 1:
        numvive=numvive+1 

    if tabella[1][colonne-1] == 1:
        numvive=numvive+1  

    if tabella[i][j] == 0:
        regoleMorte()
    else:
        regoleVive()

def angoloSudOvest():   # Confronti necessari al funzionamento della cella [Righe-1][0]

    global numvive

    if tabella[righe-2][0] == 1:
        numvive=numvive+1

    if tabella[righe-2][1] == 1:
        numvive=numvive+1 

    if tabella[righe-1][1] == 1:
        numvive=numvive+1  

    if tabella[i][j] == 0:
        regoleMorte()
    else:
        regoleVive()

def angoloSudEst(): # Confronti necessari al funzionamento della cella [righe-1][colonne-1]

    global numvive

    if tabella[righe-1][colonne-2] == 1:
        numvive=numvive+1

    if tabella[righe-2][colonne-2] == 1:
        numvive=numvive+1 

    if tabella[righe-2][colonne-1] == 1:
        numvive=numvive+1  

    if tabella[i][j] == 0:
        regoleMorte()
    else:
        regoleVive()

def latoNord(): # Confronti necessari al funzionamento delle celle contenute nella riga 0 esclusi gli angoli

    global numvive

    if tabella[i][j-1] == 1:
        numvive=numvive+1  

    if tabella[i+1][j-1] == 1:
        numvive=numvive+1 

    if tabella[i+1][j] == 1:
        numvive=numvive+1  

    if tabella[i+1][j+1] == 1:
        numvive=numvive+1  

    if tabella[i][j+1] == 1:
        numvive=numvive+1  

    if tabella[i][j] == 0:
        regoleMorte()
    else:
        regoleVive()

def latoEst():  # Confronti necessari al funzionamento delle celle contenute nella colonna "colonne-1" esclusi gli angoli

    global numvive

    if tabella[i-1][j] == 1:
        numvive=numvive+1  

    if tabella[i-1][j-1] == 1:
        numvive=numvive+1 

    if tabella[i][j-1] == 1:
        numvive=numvive+1  

    if tabella[i+1][j-1] == 1:
        numvive=numvive+1  

    if tabella[i+1][j] == 1:
        numvive=numvive+1  

    if tabella[i][j] == 0:
        regoleMorte()
    else:
        regoleVive()

def latoSud():  # Confronti necessari al funzionamento delle celle contenute nella riga "righe-1" esclusi gli angoli
    
    global numvive

    if tabella[i][j-1] == 1:
        numvive=numvive+1  

    if tabella[i-1][j-1] == 1:
        numvive=numvive+1 

    if tabella[i-1][j] == 1:
        numvive=numvive+1  

    if tabella[i-1][j+1] == 1:
        numvive=numvive+1  

    if tabella[i][j+1] == 1:
        numvive=numvive+1  

    if tabella[i][j] == 0:
        regoleMorte()
    else:
        regoleVive()

def latoOvest():    # Confronti necessari al funzionamento delle celle contenute nella colonna 0 esclusi gli angoli
    
    global numvive

    if tabella[i-1][j] == 1:
        numvive=numvive+1  

    if tabella[i-1][j+1] == 1:
        numvive=numvive+1 

    if tabella[i][j+1] == 1:
        numvive=numvive+1  

    if tabella[i+1][j+1] == 1:
        numvive=numvive+1  

    if tabella[i+1][j] == 1:
        numvive=numvive+1  

    if tabella[i][j] == 0:
        regoleMorte()
    else:
        regoleVive()

def centrale(): # Confronti necessari al funzionamento di tutte le celle che non rispettino le precedenti "condizioni particolari"

    global numvive

    if tabella[i-1][j-1] == 1:
        numvive=numvive+1  

    if tabella[i-1][j] == 1:
        numvive=numvive+1 

    if tabella[i-1][j+1] == 1:
        numvive=numvive+1  

    if tabella[i][j+1] == 1:
        numvive=numvive+1  
    
    if tabella[i+1][j+1] == 1:
        numvive=numvive+1  

    if tabella[i+1][j] == 1:
        numvive=numvive+1 

    if tabella[i+1][j-1] == 1:
        numvive=numvive+1  

    if tabella[i][j-1] == 1:
        numvive=numvive+1  

    if tabella[i][j] == 0:
        regoleMorte()
    else:
        regoleVive()





print("Benvenuto nel Gioco della Vita!")
print("\n")

evoluzioni = input("Quante evoluzioni vuoi che ci siano in questa partita?")


conta=0


while conta < int(evoluzioni) : # Ciclo che determina il riaggiornamento della griglia in base alle condizioni del gioco e in base al numero di aggiornamenti inseriti in input dall'utente
    for i in range(len(tabella)):
      
        for j in range(len(tabella[0])): # Richiamo delle funzioni specificatamente create in base alle particolari posizioni delle celle
            valore = tabella[i][j]
            if (i == 0 and j == 0):
                angoloNordOvest()
                  
            elif (i == 0 and j == colonne-1) :
                angoloNordEst()

            elif (i == righe-1 and j == 0) :
                angoloSudOvest()

            elif (i == righe-1 and j == colonne-1) :
                angoloSudEst()

            elif i == 0 and (j!=0 and j!=colonne-1):
                latoNord()

            elif i == righe-1 and (j!=0 and j!=colonne-1):
                latoSud()

            elif j == 0 and (i!=0 and i!=righe-1):
                latoOvest()
            
            elif j == colonne-1 and (i!=0 and i!=righe-1):
                latoEst()

            else:
                centrale()
            j=j+1
            numvive=0 # Riporto della variabile numvive a 0 dopo ogni singolo ciclo per prendere in esame le celle vive adiacenti solo alla cella esaminata in quel momento dal ciclo
            
        i=i+1
    
    print(np.array(appoggio))
    visualizza_matrice(appoggio) # Visualizzazione della matrice tramite la libreria matplotlib
    time.sleep(delay) # Delay impostato per permettere alla libreria matplotlib di attendere 3 secondi prima della visualizzazione dell'immagine legata all'evoluzione successiva
    tabella = appoggio 
    conta=conta+1

    print("\n")
   
    print("Questo è il ciclo",(conta))
    
    print("\n")
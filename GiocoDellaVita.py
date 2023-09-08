import matplotlib.pyplot as plt
import numpy as np
import random  
import time

plt.figure()


righe = int(input("Inserisci il numero di righe della matrice: "))
colonne = int(input("Inserisci il numero di colonne della matrice: "))


tabella=np.zeros((righe,colonne))
appoggio=np.zeros((righe,colonne))
totale=righe*colonne

random_vive = int(totale*30/100)

i = 0
j = 0
numvive=0

posizioniCasuali = np.random.choice(range(totale), random_vive, replace=False)

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

#sezione delle funzioni
def regoleVive():

    if numvive < 2:
        appoggio[i][j] = 0
    
    if numvive == 2 or numvive == 3:
        appoggio[i][j] = 1

    if numvive >= 4 :
        appoggio[i][j] = 0

def regoleMorte():

    if numvive == 3:
        appoggio[i][j] = 1
    else: 
        appoggio[i][j] = 0


def angoloNordOvest():

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

def angoloNordEst():

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

def angoloSudOvest():

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

def angoloSudEst():

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

def latoNord():

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

def latoEst():

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

def latoSud():
    
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

def latoOvest():
    
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

def centrale():

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


while conta < int(evoluzioni) :
    for i in range(len(tabella)):
      
        for j in range(len(tabella[0])):
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
            numvive=0
            
        i=i+1
    
    print(np.array(appoggio))
    visualizza_matrice(appoggio)
    time.sleep(delay)
    tabella = appoggio 
    conta=conta+1

    print("\n")
   
    print("Questo è il ciclo",(conta))
    
    print("\n")
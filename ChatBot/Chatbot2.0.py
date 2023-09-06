import sqlite3

# Connessione al database o creazione se non esiste
conn = sqlite3.connect('Dati_Offerte.db')

# Creazione di un cursore
cursor = conn.cursor()

# Creazione di una tabella se non esiste
cursor.execute('''CREATE TABLE IF NOT EXISTS offerte
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Nome_Offerta TEXT,
                   Descrizione TEXT,
                   Stipendio INTEGER,
                   Numero_Recruiter INTEGER)''')



i = 1

while i > 0:

    print("Benvenuto su ChatBOT")
    print("\n")
    print("DatoreLavoro - Utente - Esci")
    scelta = input("Come vuoi interagire? ")
    
    if scelta == "DatoreLavoro":
        print("\n")
        password_inserita = input("Inserisci la password del DatoreLavoro: ")
        
        if password_inserita == "sasso":
            print("Accesso consentito. Esegui azione per il caso DatoreLavoro")
            print("\n")
            print("Operazioni disponibili: Inserisci - Modifica - Elimina")
            scelta1 = input("Come vuoi interagire? ")

            if scelta1 == "Inserisci":
                # Input dei dati dall'utente
                print("\n")
                Nome = input("Per che lavoro vuoi creare un'offerta?: ")
                Descrizione = input("Inserisci una descrizione per il lavoro: ")
                Stipendio = int(input("Inserisci lo stipendio: "))
                Numero_Recruiter = int(input("Inserisci il numero a cui gli interessati ti potranno contattare: "))

                # Inserimento dei dati nella tabella
                cursor.execute("INSERT INTO offerte (Nome_Offerta, Descrizione, Stipendio, Numero_Recruiter) VALUES (?, ?, ?, ?)",
                               (Nome, Descrizione, Stipendio, Numero_Recruiter))

                # Salvataggio dei cambiamenti e chiusura della connessione
                conn.commit()

                print("\n")
                print("Dati inseriti con successo nel database.")
                print("\n")


            elif scelta1 == "Modifica":
                # Visualizza tutte le offerte disponibili per la modifica
                cursor.execute("SELECT * FROM offerte")
                offerte = cursor.fetchall()
                print("Ecco le offerte disponibili per la modifica:")
                for row in offerte:
                    id, Nome, Descrizione, Stipendio, Numero_Recruiter = row
                    print(f"ID: {id} | {Nome} | {Descrizione} | {Stipendio} euro mensili | {Numero_Recruiter}")
                
                print("\n")

                # Chiedi all'utente di selezionare l'ID dell'offerta da modificare
                offerta_da_modificare = input("Inserisci l'ID dell'offerta da modificare: ")

                # Verifica se l'ID inserito è valido
                offerta_esistente = False
                for row in offerte:
                    id, _, _, _, _ = row
                    if str(id) == offerta_da_modificare:
                        offerta_esistente = True
                        break

                if not offerta_esistente:
                    print("ID dell'offerta non valido. La modifica non è possibile.")
                else:
                    # Input dei nuovi dati dall'utente
                    Nome = input("Inserisci il nuovo nome per l'offerta: ")
                    Descrizione = input("Inserisci la nuova descrizione per l'offerta: ")
                    Stipendio = int(input("Inserisci il nuovo stipendio: "))
                    Numero_Recruiter = int(input("Inserisci il nuovo numero a cui gli interessati ti potranno contattare: "))

                    # Esegui l'aggiornamento dei dati dell'offerta selezionata
                    cursor.execute("UPDATE offerte SET Nome_Offerta=?, Descrizione=?, Stipendio=?, Numero_Recruiter=? WHERE id=?",
                                   (Nome, Descrizione, Stipendio, Numero_Recruiter, offerta_da_modificare))

                    # Salvataggio dei cambiamenti e chiusura della connessione
                    conn.commit()

                    print("\n")
                    print("Offerta modificata con successo.")
                    print("\n")

            elif scelta1 == "Elimina":
                # Visualizza tutte le offerte disponibili per l'eliminazione
                cursor.execute("SELECT * FROM offerte")
                offerte = cursor.fetchall()
                print("Ecco le offerte disponibili per l'eliminazione:")
                for row in offerte:
                    id, Nome, Descrizione, Stipendio, Numero_Recruiter = row
                    print(f"ID: {id} | {Nome} | {Descrizione} | {Stipendio} euro mensili | {Numero_Recruiter}")

                print("\n")
                # Chiedi all'utente di selezionare l'ID dell'offerta da eliminare
                offerta_da_eliminare = input("Inserisci l'ID dell'offerta da eliminare: ")
                

                # Verifica se l'ID inserito è valido
                offerta_esistente = False
                for row in offerte:
                    id, _, _, _, _ = row
                    if str(id) == offerta_da_eliminare:
                        offerta_esistente = True
                        break

                if not offerta_esistente:
                    print("ID dell'offerta non valido. L'eliminazione non è possibile.")
                else:
                    # Esegui l'eliminazione dell'offerta selezionata
                    cursor.execute("DELETE FROM offerte WHERE id=?", (offerta_da_eliminare,))
    
                    cursor.execute("SELECT id FROM offerte")
                    rows = cursor.fetchall()
                    new_id = 1

                    for row in rows:
                        old_id = row[0]
                        if old_id != new_id:
                            cursor.execute("UPDATE offerte SET id=? WHERE id=?", (new_id, old_id))
                            new_id += 1

                    # Salvataggio dei cambiamenti e chiusura della connessione
                    conn.commit()
                    
                    print("\n")
                    print("Offerta eliminata con successo.")
                    print("\n")

                    

            else:
                print("Azione non valida.")
        else:
            print("Password errata. Accesso negato.")
    
    elif scelta == "Utente":
        print("\n")
        print("Opzioni disponibili: Visualizza - Cerca - Esci")
        scelta1 = input("Come vuoi interagire? ")
        print("\n")

        if scelta1 == "Visualizza":
            cursor.execute("SELECT id, Nome_Offerta, Stipendio FROM offerte")

            # Recupero di tutti i dati e visualizzazione
            for row in cursor.fetchall():
                id, Nome, Stipendio = row
                print(f"ID: {id} | {Nome} | {Stipendio} euro mensili")
            print("\n")

            while i > 0:

                scelta2 = input("VisualizzaID - Esci? ")

                if scelta2 == "VisualizzaID":
                
                
                    a = input("Qual è l'id dell'offerta a cui sei interessato? ")

                    print("\n")

                    cursor.execute("SELECT * FROM offerte WHERE id = ?", (a,))
                    offerte = cursor.fetchall()
                    for row in offerte:
                        id, Nome, Descrizione, Stipendio, Numero_Recruiter = row
                        print(f"ID: {id} | {Nome} | {Descrizione} | {Stipendio} euro mensili | {Numero_Recruiter}")
                        print("\n")
                
                else:
                    break


        elif scelta1 == "Cerca":

            print("\n")

            parola = input("Inserisci parametro della tua ricerca: ")

            cursor.execute("SELECT * FROM offerte WHERE Nome_Offerta LIKE ? OR Descrizione LIKE ? OR Stipendio LIKE ?", (f"%{parola}%", f"%{parola}%", f"%{parola}%"))
            offerte = cursor.fetchall()
            for row in offerte:
                id, Nome, Descrizione, Stipendio, Numero_Recruiter = row
                print(f"ID: {id} | {Nome} | {Descrizione} | {Stipendio} euro mensili")

            print("\n")

            scelta3 = input("Vuoi visualizzare il recapito telefonico? Si - No : ")
            if scelta3 == "Si":

                cursor.execute("SELECT Numero_Recruiter FROM offerte WHERE Nome_Offerta LIKE ? OR Descrizione LIKE ? OR Stipendio LIKE ?", (f"%{parola}%", f"%{parola}%", f"%{parola}%"))
                recruiter = cursor.fetchall()
                for row in recruiter:
                    Numero_Recruiter = row[0]
                    print(f"Contatto telefonico del Recruiter: {Numero_Recruiter}")

                    print("\n")

        else:
            break
        
    
    elif scelta == "Esci":
        break

conn.close()

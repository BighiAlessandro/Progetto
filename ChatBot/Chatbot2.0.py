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


print("Benvenuto su ChatBOT")
print("\n")
i = 1

while i > 0:

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
                    print(f"ID: {id} | {Nome} | {Descrizione} | {Stipendio} | {Numero_Recruiter}")
                
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
                    print(f"ID: {id} | {Nome} | {Descrizione} | {Stipendio} | {Numero_Recruiter}")

                print("\n")
                # Chiedi all'utente di selezionare l'ID dell'offerta da eliminare
                offerta_da_elimare = input("Inserisci l'ID dell'offerta da eliminare: ")
                

                # Verifica se l'ID inserito è valido
                offerta_esistente = False
                for row in offerte:
                    id, _, _, _, _ = row
                    if str(id) == offerta_da_elimare:
                        offerta_esistente = True
                        break

                if not offerta_esistente:
                    print("ID dell'offerta non valido. L'eliminazione non è possibile.")
                else:
                    # Esegui l'eliminazione dell'offerta selezionata
                    cursor.execute("DELETE FROM offerte WHERE id=?", (offerta_da_elimare,))

                    # Salvataggio dei cambiamenti e chiusura della connessione
                    conn.commit
                    ()
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
            cursor.execute("SELECT * FROM offerte")

            # Recupero di tutti i dati e visualizzazione
            for row in cursor.fetchall():
                id, Nome, Descrizione, Stipendio, Numero_Recruiter = row
                print(f"ID: {id} | {Nome} | {Descrizione} | {Stipendio} | {Numero_Recruiter}")
        print("\n")
        
    elif scelta == "Esci":
        break

conn.close()

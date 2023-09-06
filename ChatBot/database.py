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

# Input dei dati dall'utente
Nome = input("Per che lavoro vuoi creare un'offerta?: ")
Descrizione = input("Inserisci una descrizione per il lavoro: ")
Stipendio = int(input("Inserisci lo stipendio: "))
Numero_Recruiter = int(input("Inserisci il numero a cui gli interessati ti potranno contattare: "))

# Inserimento dei dati nella tabella
cursor.execute("INSERT INTO offerte (Nome_Offerta, Descrizione, Stipendio, Numero_Recruiter) VALUES (?, ?, ?, ?)", (Nome, Descrizione, Stipendio, Numero_Recruiter))

# Salvataggio dei cambiamenti e chiusura della connessione
conn.commit()


print("Dati inseriti con successo nel database.")
print("\n")
print("\n")
print("\n")
print("\n")


cursor.execute("SELECT * FROM offerte")

# Recupero di tutti i dati e visualizzazione
for row in cursor.fetchall():
    id, Nome, Descrizione, Stipendio, Numero_Recruiter = row
    print(f"ID: {id} | {Nome} | {Descrizione} | {Stipendio} | {Numero_Recruiter}")


# first line

import psycopg2
import json

#   create the db - just a bunch of empty tables
def make_db(cur):
    #   apre il file in lettura e copia il contenuto come fosse una stringa
    with open('db.sql') as file:
        db = file.read()
    #   passa la stringa come comando
    cur.execute(db)

    # per stampare i risultati
    rows = cur.fetchall()
    for rw in rows:
        print(rw)

# Connects with the server
def connect():
    # Connessione al server di PostgreSQL
    try:
        # Open the credentials file and load the JSON data
        with open("credentials.json", "r") as nooty:
            pruty = json.load(nooty)  # Load JSON content into a dictionary
        # Use the loaded dictionary for the connection
        conn = psycopg2.connect(**pruty)
        return conn
    except Exception as e:
        print("Failed to establish connection:\n", e)
        return None

#   first interation with the db
def first_connection():

    cnt = connect()
    if cnt is None:
        print ("couldn't connect to db or somme other shit you gotta check.\nfile is connection.py")
        return
    else:
        print ("Connection established correctly, yay!")
        cur = cnt.cursor()
        make_db(cur)

#   chiude cursore e connessione
        cur.commit()
        cur.close()
    cnt.close()

#   fills the db's tables
def second_db(bl):
# bl = miao
    def fill_query(miao, cur):
        if miao == 1:
            # tabella owner
            with open('owner tablefiltìl.sql') as file:
                quack = file.read()
            cur.execute(quack)
        elif miao == 2:
            # tabella illness
            with open("illness tablefill.sql") as file:
                peachy = file.read()
            cur.execute(peachy)
        elif miao == 3:
            # tabella pet
            with open("pets tablefill.sql") as file:
                lemon = file.read()
            cur.execute(lemon)

    cnt = connect()
    if cnt is None:
        print ("Connection-chan has left UwU\n *sniff sniff*...")
    else:
        print ("Connection-cha is here, yay!")
        cur = psycopg2.cursor()
        fill_query(bl, cur)

# flow
first_connection()

# last line
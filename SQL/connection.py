import psycopg2
from credentials import db_config as db

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

#   connects with the server
def connect():
#   connessione al server di PostgreSQL
    try:
        conn = psycopg2.connect(db)
        return conn
    except Exception as e:
        print ("failed to establish connection. " + e)
        return None

#   first interation with the db
def first_connection():

    cnt = connect()
    if cnt is None:
        print ("couldn't conect to db or somme other shit you gotta check.\nfile is connection.py")
        return
    else:
        print ("Connection established correctly, yay!")
        cur = psycopg2.cursor()
        make_db(cur)

#   chiude cursore e connessione
        cur.close()
    cnt.close()

#   fills the db's tables
def second_db():

    def fill_db(cur):
        with open('tablefill.sql') as blblbl:
            quack = file.read(blblbl)
        cur.execute(quack)

    cnt = connect()
    if cnt is None:
        print ("Connection-chan is here UwU\nsomething went wrong *sniff sniff*...")
    else:
        print ("Connection established correctly, yay!")
        cur = psycopg2.cursor()
        fill_db(cur)

# last line
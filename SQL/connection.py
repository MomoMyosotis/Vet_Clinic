# first line

import psycopg2
import json

def close(cur, cnt):
    cur.close()
    cnt.close()

# print table
def tprint (cur):
    # per stampare i risultati
    rows = cur.fetchall()
    for rw in rows:
        print(rw)


#   create the db - just a bunch of empty tables
def make_db(cur):
    #   apre il file in lettura e copia il contenuto come fosse una stringa
    with open('db.sql') as file:
        db = file.read()
    #   passa la stringa come comando
    cur.execute(db)
    print("tables created, now gotta populate 'em")


# Connects with the server
def connect():
    # Connessione al server di PostgreSQL

        # Open the credentials file and load the JSON data
    with open("credentials.json", "r") as nooty:
        pruty = json.load(nooty)
    try:
        # ** -> scompone il dict in parametri
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
        # commit() è un modulo  di connect
        cnt.commit()
    return cnt, cur


#   fills the db's tables
def populate(cnt, cur):
    def fill_query(miao, cur):
        if miao == 0:
            print()
        if miao == 1:
            # tabella owner
            try:
                with open("owner tablefill.sql") as file:
                    quack = file.read()
                    quack = str(quack)
                cur.execute(quack)
            except Exception as e:
                print("error 9.\n " + str(e))
            else:
                print("\nowner table done")
                cnt.commit()

        elif miao == 2:
            # tabella illness
            try:
                with open("illness tablefill.sql") as file:
                    peachy = file.read()
                cur.execute(peachy)
            except Exception as e:
                print("error 10.\n " + str(e))
            else:
                print("\nillness table done")
                cnt.commit()

        elif miao == 3:
            # tabella pet
            try:
                with open("pets tablefill.sql") as file:
                    lemon = file.read()
                cur.execute(lemon)
            except Exception as e:
                print("error 11.\n " + str(e))
            else:
                print("\npets table done")
                cnt.commit()

    print("we're populating")

    bl = 0
    while bl in [0, 1, 2, 3]:
        fill_query(bl, cur)
        bl +=1

    while bl in [0, 1, 2, 3]:
        tprint(bl, cur)
        bl +=1

# flow
def flow():
    connessione, cursore = first_connection()
    populate(connessione, cursore)

flow()
# last line
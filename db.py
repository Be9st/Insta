import sqlite3
from datetime import datetime

def connect_to_db(user):
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    
    try: 
        req = cur.execute('SELECT * FROM Insta WHERE users ="{}"'.format(user)).fetchone()[0]
        result = True
    except: 
        data = [user, datetime.strftime(datetime.now(), "%H:%M:%S")]
        cur.execute('INSERT INTO Insta VALUES(?, ?)', data)
        result = False
    
    con.commit()
    cur.close()
    con.close()
    return result
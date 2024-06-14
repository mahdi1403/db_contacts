import sqlite3

class database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS contacts (id integer primary key,
                         fname text,Lname text, city text, phone text)
                         """)
        self.con.commit()
        
        def insert(self,fname,lname,city,phone):
            self.cur.execute("INSERT INTO contacts (id,fname,lname,city,phone) VALUES (null,?,?,?,?)",
                             (fname,lname,city,phone) )
            self.con.commit()
            print("insert record")
            
import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.c=self.con.cursor()
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS datas(
                pid INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                addresS TEXT NOT NULL,
                contact TEXT NOT NULL,
                mail TEXT NOT NULL
                )
                """)
        self.con.commit()

    def insert(self,name,age,gender,address,contact,mail):
        sql="""
                INSERT INTO datas VALUES(NULL,?,?,?,?,?,?)
            """
        self.c.execute(sql,(name,age,gender,address,contact,mail))
        self.con.commit()

    def fetch_record(self):
        self.c.execute("SELECT * FROM datas")
        data=self.c.fetchall()
        print("\n",data)

    def update_record(self,name,age,address,pid):
        sql="""
                UPDATE datas set name=?,age=?,address=? where pid=?
            """
        self.c.execute(sql,(name,age,address,pid))
        self.con.commit()

    def remove_record(self,pid):
        sql="DELETE FROM datas WHERE pid=?"
        self.c.execute(sql,(pid,))
        self.con.commit()

obj=Database('registration.db')
obj.insert('Sathya',24,'Male','Salem',9085013498,"sathya@gmail.com")
# obj.update_record('V.Raghul',28,'Salem',3)
obj.remove_record(3)
obj.fetch_record()
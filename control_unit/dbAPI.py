import sqlite3 as sql
import os
from collections import OrderedDict





class dbHandler(object):
    """
    DB path: /db/sound.db
    table: file_output
    column: id, url(text)
    """
    def __init__(self):
        self._dir = os.path.dirname(__file__)
        self._db_dir = self._dir + "/db/sound.db"
        self._db_len = len(self.read())

    def read(self):
        conn = sql.connect(self._db_dir)

        c = conn.cursor()

        result = c.execute("SELECT * FROM file_output")

        dist = OrderedDict()
        for row in result:
            dist[row[0]] = row[1]

        conn.close()

        return dist

    def insert(self, path):
        conn = sql.connect(self._db_dir)
        c = conn.cursor()
        url = [(path)]
        try:
            c.execute("INSERT INTO file_output(url) values (?)", url)
            conn.commit()
            print("insert successful")
            conn.close()
            self._db_len += 1
            return True
        except:
            print("insert data failure")
            conn.close()
            return False


    def delete_last_one(self):
        conn = sql.connect(self._db_dir)
        c=conn.cursor()
        last_one_path = c.execute("SELECT url FROM file_output WHERE id =(SELECT MAX(id) FROM file_output)")
        c.execute("DELETE FROM file_output WHERE id= (SELECT MAX(id) FROM file_output)")
        conn.commit()
        for row in last_one_path:
            path = row[0]
            self.remove(path)
        print("delete successful")
        conn.close()
        return True

    def get_len(self):
        return self._db_len

    def remove(self, path):
        os.remove(self._dir + path)
        print(path.split("/")[-1] + " has been removed")

# db=dbHandler()
# db.delete_last_one()
import sqlite3

class Db:
    
    _tableNames = { "statuses": "statuses"}
    _tables = [_tableNames["statuses"]]
    
    def __init__(self):
        conn = sqlite3.connect("impersonator.db")
        self.cursor = conn.cursor()
        self._create_tables()
       
    
    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                        (id int, user_id int, date string, content string)'''.format(Db._tableNames["statuses"]))

    def insert_status(self, values):
        self.cursor.execute("INSERT INTO {} VALUES (?,?,?,?)".format(Db._tableNames["statuses"]), values)
        self.cursor.commit()
    
    def get_status(self, status_id, user_id):
        transaction = self.cursor.execute("SELECT * FROM {} WHERE user_id = ? AND id = ?".format(Db._tableNames["statuses"]), (user_id, status_id))
        return self.cursor.fetchone(transaction)
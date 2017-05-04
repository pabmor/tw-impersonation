import sqlite3

class Db:
    
    self.tableNames = { statuses: "statuses"}
    self.tables = [self._tableNames.statuses]
    
    def __init__(self):
        conn = sqlite3.connect('impersonator.db')
        self.cursor = conn.cursor()
        self._create_tables()
       
    
    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                        (int id, string username, string date, string content)''').format(self._tableNames.statuses)

    def insert_status(self, values):
        self.cursor.execute("INSERT INTO {} VALUES (?,?,?,?)".format(self._tableNames.statuses), values)
        self.cursor.commit()
    
    def get_statuses(self, username):
        return self.cursor.execute("SELECT * FROM {} WHERE username = ?".format(self._tableNames.statuses), username)
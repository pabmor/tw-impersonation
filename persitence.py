import sqlite3

conn = sqlite3.connect('impersonator.db')

cursor = conn.cursor()


c.execute('''CREATE TABLE Twits
		(int id, string content)''')


          


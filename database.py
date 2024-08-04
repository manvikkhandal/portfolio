import sqlite3

from numpy import record
conn = sqlite3.connect("userdata.db")
create_table_query = """
create table userecord (name varchar(25),email varchar(80),message varchar(60))
"""

cur = conn.cursor()
cur.execute(create_table_query)
print("you have successfully created table")

cur.close()
conn.close()
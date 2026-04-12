import sqlite3

def connect_db():
  return sqlite3.connect('task.db')


# ------------> CREATE TABLE
def create_table():
  conn=connect_db()
  c=conn.cursor()
  
  c.execute("""CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    completed INTEGER DEFAULT 0
    )""")
  
  conn.commit()
  conn.close()
  

# ------------> ADD TASK
def add_task(title):
  conn=connect_db()
  c=conn.cursor()
  
  c.execute("INSERT INTO tasks(title) VALUES (?)",(title,))
  
  conn.commit()
  conn.close()
  
  
# ------------> GET DATA (READ)
def get_data():
  conn=connect_db()
  c=conn.cursor()
  
  c.execute("SELECT * FROM tasks")
  data=c.fetchall()
  conn.close()
  return data


# ------------> DELETE TASK
def delete_task(id):
  conn=connect_db()
  c=conn.cursor()
  
  c.execute("DELETE FROM tasks where id = (?)",(id,))
  conn.commit()
  conn.close()
  
  
# ------------> TOGGLE TASK
def toggle_task(id):
  conn=connect_db()
  c=conn.cursor()
  
  c.execute("UPDATE tasks SET completed = not completed where id = (?)",(id,))
  conn.commit()
  conn.close()
  
# ------------> UPDATE TASK
def update_task(id,title):
  conn=connect_db()
  c=conn.cursor()
  
  c.execute("UPDATE tasks SET title = ? where id = ?",(title,id))
  conn.commit()
  conn.close()
  
# ------------> UPDATE TASK
def count_task():
  conn=connect_db()
  c=conn.cursor()
  
  # total
  c.execute("SELECT COUNT(*) FROM tasks")
  total=c.fetchone()[0]
  
  # completed
  c.execute("SELECT COUNT(*) FROM tasks where completed=1")
  completed=c.fetchone()[0]
  
  remaining = total-completed
  
  return total,completed,remaining


# ------------> FILTER TASK
def get_completed_task():
  conn=connect_db()
  c=conn.cursor()
  
  # completed
  c.execute("SELECT * FROM tasks WHERE completed=1")
  data=c.fetchall()
  
  conn.close()
  return data



def get_pending_task():
  conn=connect_db()
  c=conn.cursor()
  
  # completed
  c.execute("SELECT * FROM tasks WHERE completed=0")
  data=c.fetchall()
  
  conn.close()
  return data
  



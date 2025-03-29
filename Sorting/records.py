import sqlite3


class Record():

  def __init__(self, title: str, n: int, dataType: str, time: float, comparisons: int, changes: int = None):
    self.title = title
    self.n = n
    self.dataType = dataType
    self.time = time
    self.comparisons = comparisons
    self.changes = changes

  def __repr__(self):
    return (
      f"Record(name={self.title}, size={self.n}, order={self.dataType}, "
      f"time={self.time:.6f}, comparisons={self.comparisons}, changes={self.changes})"
    )

  def save_to_db(self, conn: sqlite3.Connection, cursor: sqlite3.Cursor):
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS records (
                    title TEXT,
                    n INTEGER,
                    dataType TEXT,
                    time REAL,
                    op INTEGER
                )
            ''')

            conn.commit()

            cursor.execute('''
                INSERT INTO records (title, n, dataType, time, op)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.title, self.n, self.dataType, self.time, self.comparisons + self.changes))

            conn.commit()
           # print(F'[INFO] :: RECORD {self.title}  {self.n} {self.dataType} {self.time} {self.comparisons + self.changes} HAS BEEN SAVED')
        
        except sqlite3.Error as e:
            print(f'[ERROR] :: ERROR WHILE SAVING THE RECORD: {e}')
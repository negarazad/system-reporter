from fastapi import FastAPI, Query
import sqlite3

app = FastAPI()

# اتصال به پایگاه داده SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# ایجاد جدول برای ذخیره رکوردها
cursor.execute('''CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY,
                    data TEXT
                )''')
conn.commit()

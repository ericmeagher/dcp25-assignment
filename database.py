import os
import sqlite3
import pandas as pd

from abc_parser import parse_abc_file   # uses parse_abc_file


BOOKS_DIR = "abc_books"   
DB_NAME = "tunes.db"      # SQLite database file

def get_connection(db_name=DB_NAME):
    return sqlite3.connect(db_name)


def create_tunes_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tunes (
            id INT PRIMARY KEY AUTOINCREMENT,
            book_number INT,
            x INT,
            title TEXT,
            meter TEXT,
            key TEXT,
            rtype TEXT,
            body TEXT
        )
    """)
    conn.commit()
                

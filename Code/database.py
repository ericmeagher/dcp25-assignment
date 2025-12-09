import os
import sqlite3
import pandas as pd

from abc_parser import parse_abc_file


BOOKS_DIR = "abc_books"
DB_NAME = "tunes.db"


def get_connection(db_name=DB_NAME):
    """Open a connection to the SQLite database."""
    return sqlite3.connect(db_name)


def create_tunes_table(conn):
    """Create the tunes table if it does not already exist."""
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tunes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_number INTEGER,
            x INTEGER,
            title TEXT,
            meter TEXT,
            key TEXT,
            rtype TEXT,
            body TEXT
        )
    """)
    conn.commit()


def clear_tunes_table(conn):
    """Delete all rows from tunes."""
    cur = conn.cursor()
    cur.execute("DELETE FROM tunes")
    conn.commit()


def insert_tune(conn, tune, book_number):
    """Insert one tune dictionary into the tunes table."""
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tunes (book_number, x, title, meter, key, rtype, body)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        book_number,
        tune.get("x"),
        tune.get("title"),
        tune.get("meter"),
        tune.get("key"),
        tune.get("rtype"),
        tune.get("body"),
    ))
    conn.commit()


def find_abc_files(base_dir=BOOKS_DIR):
    """Return list of (filepath, book_number) for all .abc files."""
    results = []

    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)

        if not os.path.isdir(folder_path):
            continue
        if not folder_name.isdigit():
            continue

        book_number = int(folder_name)

        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".abc"):
                full_path = os.path.join(folder_path, filename)
                results.append((full_path, book_number))

    return results


def build_database_from_files(clear_existing=False):
    """Parse all .abc files in abc_books and fill the database."""
    conn = get_connection(DB_NAME)
    create_tunes_table(conn)

    if clear_existing:
        clear_tunes_table(conn)

    files = find_abc_files(BOOKS_DIR)
    total_tunes = 0

    for file_info in files:
        path, book_number = file_info
        tunes = parse_abc_file(path)
        for tune in tunes:
            insert_tune(conn, tune, book_number)
        total_tunes += len(tunes)
        print(f"{path} -> {len(tunes)} tune(s)")

    conn.close()
    print(f"Finished. Imported {total_tunes} tunes.")


def load_tunes_dataframe():
    """Load all tunes into a pandas DataFrame."""
    conn = get_connection(DB_NAME)
    df = pd.read_sql("SELECT * FROM tunes", conn)
    conn.close()
    return df


def get_tunes_by_book(df, book_number):
    """All tunes from one book."""
    return df[df["book_number"] == book_number]


def get_tunes_by_type(df, tune_type):
    """All tunes whose rtype contains a string (e.g. 'reel')."""
    matches = df["rtype"].fillna("").str.contains(tune_type, case=False)
    return df[matches]


def search_tunes_by_title(df, term):
    """All tunes whose title contains a string."""
    matches = df["title"].fillna("").str.contains(term, case=False)
    return df[matches]

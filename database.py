import sqlite3
from datetime import datetime

DB_NAME = "documents.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            category TEXT NOT NULL,
            content TEXT,
            filepath TEXT NOT NULL,
            date_added TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_document(filename, category, content, filepath):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO documents (filename, category, content, filepath, date_added)
            VALUES (?, ?, ?, ?, ?)
        """, (filename, category, content, filepath, date_now))

        conn.commit()
        conn.close()
        return True

    except Exception as e:
        print("Erreur DB:", e)
        return False


def get_all_documents():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM documents")
    docs = cursor.fetchall()

    conn.close()
    return docs


def get_documents_by_type(category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM documents WHERE category=?", (category,))
    docs = cursor.fetchall()

    conn.close()
    return docs


def get_document_stats():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, COUNT(*)
        FROM documents
        GROUP BY category
    """)

    stats = cursor.fetchall()
    conn.close()
    return stats
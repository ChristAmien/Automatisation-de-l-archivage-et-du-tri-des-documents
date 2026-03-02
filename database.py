import sqlite3

def init_db():
    conn = sqlite3.connect("archive.db")
    cursor=conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT,
        type_document TEXT,
        contenu TEXT,
        date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
    
    conn.commit()
    conn.close()

def insert_document(titre, type_document, contenu):
    conn=sqlite3.connect("archive.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERY INTO document (titre, type_document, contenu)
    VALUES (?,?,?)
    """,(titre,type_document, contenu))

    conn.commit()
    conn.close()    
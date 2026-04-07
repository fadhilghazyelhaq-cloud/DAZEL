import sqlite3

conn = sqlite3.connect("umkm.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produk (
        nama TEXT PRIMARY KEY,
        harga INTEGER,
        stok INTEGER
    )
    """)
    conn.commit()
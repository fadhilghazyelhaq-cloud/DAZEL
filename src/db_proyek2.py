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

def tambah_produk():
    data = [
        ("Paket Hemat", 95000, 20),
        ("Paket Keluarga", 195000, 15)
    ]

    for d in data:
        cursor.execute(
            "INSERT OR IGNORE INTO produk VALUES (?, ?, ?)", d
)

    conn.commit()

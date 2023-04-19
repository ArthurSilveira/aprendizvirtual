import sqlite3

def banco_connect():
    conn = sqlite3.connect('banco/projetec.db', isolation_level=None)
    conn.row_factory = sqlite3.Row
    return conn

def banco_cursor(conn, execute):
    cur = conn.cursor()
    cur.execute(execute)

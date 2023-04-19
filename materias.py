import banco

def materias():
    conn = banco.banco_connect()
    materias = conn.execute("select * from materias").fetchall()
    conn.close()
    return materias

def buscar_materia(link):
    for x in materias():
        if x['link'] == link:
            return x
    return None

def newmat(novamatlink, novamatnome):
    conn = banco.banco_connect()
    banco.banco_cursor(conn, f"insert into materias (link, nome) values ('{novamatlink}', '{novamatnome}');")
    conn.close()

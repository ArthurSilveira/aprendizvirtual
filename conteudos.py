import banco, materias
from werkzeug.utils import secure_filename

def listaconteudo():
    conn = banco.banco_connect()
    conteudos = conn.execute("select * from conteudos").fetchall()
    conn.close()
    return conteudos

def contpormat(materialink):
    conteudosatuais = []
    for x in listaconteudo():
        if materialink == x['materia']:
            conteudosatuais.append(x)
    return conteudosatuais

def contver(materialink):
    contatual = contpormat(materialink)
    contatualver = []
    for x in contatual:
        if x['userv'] != "0":
            contatualver.append(x)
    return contatualver

def contnver(materialink):
    contatual = contpormat(materialink)
    contatualnver = []
    for x in contatual:
        if x['userv'] == "0":
            contatualnver.append(x)
    return contatualnver

def buscar_cont(link):
    for x in listaconteudo():
        if x['link'] == link:
            return x
    return None

def buscar_cont_user(user):
    conn = banco.banco_connect()
    conteudos = conn.execute(f"select * from conteudos where userc='{user}'").fetchall()
    conn.close()
    return conteudos

def blocosatual(link):
    conn = banco.banco_connect()
    conteudos = conn.execute(f"select * from blocos where link='{link}'").fetchall()
    conn.close()
    return conteudos

def arqvalido(arqnome):
    if arqnome.rsplit(".", 1)[-1] in ['png', 'jpg', 'jpeg', 'gif']:
        return True
    return False


def add_cont(request, materia, user):
    materianome = materias.buscar_materia(materia)['nome']
    titulo = request.form['titulo']
    link = titulo.replace(" ", "").lower()
    email = user['email']
    tag = user['tag']
    
    txtquant = int(request.form['txtquant'])
    imgquant = int(request.form['imgquant'])
    if txtquant > 0:
        txtordem = request.form['txtordem'].split(";")
    if imgquant > 0:
        imgordem = request.form['imgordem'].split(";")

    if txtquant != 0 and imgquant != 0:
        tipo="Texto / Imagens"
    elif txtquant != 0:
        tipo="Texto"
    else:
        tipo="Imagens"

    userv = "0"
    uservtag = "0"
    if user['verificado']:
        userv = email
        uservtag = tag

    conn = banco.banco_connect()
    banco.banco_cursor(conn, f"""insert into conteudos (link, materia, materianome, tipo, titulo, userc, userctag, userv, uservtag) values ('{link}', '{materia}', '{materianome}', '{tipo}', '{titulo}', '{email}', '{tag}', '{userv}','{uservtag}')""")

    arq = []
    arqnome = []
    for x in range(0, txtquant+imgquant):
        if txtquant > 0:
            if str(x) in txtordem:
                conteudo = request.form[f"inputtxt{x}"]
                banco.banco_cursor(conn, f"""insert into blocos (tipo, conteudopag, link) values ('texto', '{conteudo}', '{link}')""")
        if imgquant > 0:
            if str(x) in imgordem:
                arqatual = request.files[f'inputimg{x}']
                if arqatual.filename == '':
                    continue
                if arqvalido(arqatual.filename):
                    arqatualnome = secure_filename(arqatual.filename)
                    arq.append(arqatual)
                    arqnome.append(arqatualnome)
                    banco.banco_cursor(conn, f"""insert into blocos (tipo, conteudopag, link) values ('img', 'imagens/userimgs/{arqatualnome}', '{link}')""")
    conn.close()
    
    return [link, arq, arqnome]


def vercont(contlink, user):
    conn = banco.banco_connect()
    banco.banco_cursor(conn, f"""update conteudos set userv = '{user['email']}', uservtag = '{user['tag']}' where link = '{contlink}' """)
    conn.close()

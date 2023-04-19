import banco

def listausers():
    conn = banco.banco_connect()
    listausers = conn.execute("select * from users").fetchall()
    conn.close()
    return listausers


def novo_user(request):
    tag = request.form['tag']
    email = request.form['email']
    senha = request.form['senha']
    valido = valido_user(tag, email, senha)
    conn = banco.banco_connect()
    banco.banco_cursor(conn, f"""insert into users (email, tag, senha, verificado) values
    ('{email}', '{tag}', '{senha}', 0)""")
    conn.close()
    return [valido, email]


def valido_user(tag, email, senha):
    if tag == "" or email == "" or senha == "":
        return "Um dos campos está vazio"
    
    if tag.count(";") > 0 or email.count(";") > 0 or senha.count(";") > 0:
        return 'Caractere inválid: ;'
    
    if buscar_user(email):
        return "E-mail já cadastrado."
    
    return None


def login_user(request):
    email = request.form['email']
    senha = request.form['senha']

    user = buscar_user(email)
    if user:
        if user['senha'] == senha:
            return email
    return False


def buscar_user(email):
    for x in listausers():
        if x['email'] == email:
            return x
    return None

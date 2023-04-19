import banco

def listaval():
    conn = banco.banco_connect()
    aval = conn.execute("select * from avaliacoes")
    return aval


def listavalatual(conteudoatual):
    list = []
    for x in listaval():
        if x['link'] == conteudoatual:
            list.append(x)
    if len(list) > 0:
        scoretotal = 0
        numaval = 0
        for x in list:
            scoretotal += x['score']
            numaval += 1
        return [list, ("%.2f" % (scoretotal / numaval))]
    return [False, None]

def tem_aval(email, conteudonome):
    if listavalatual(conteudonome)[0]:
        for x in listavalatual(conteudonome)[0]:
            if x['userc'] == email:
                return x
    return None


def media(aval):
        scoretotal = 0
        numaval = 0
        for x in aval:
            scoretotal += int(x.score)
            numaval += 1
        return "%.2f" % (scoretotal / numaval)


def nova_aval(avaluser, g, request, link):
    user = g.user['email']
    tag = g.user['tag']
    score = request.form['score']
    avaltxt = request.form['avaltxt']
    estilo = "cor-estrela-amarela"
    if int(score) < 3:
        estilo = "cor-estrela-vermelha"
    if int(score) > 3:
        estilo = "cor-estrela-verde"

    conn = banco.banco_connect()
    if avaluser:
        banco.banco_cursor(conn, f"""update avaliacoes set score='{score}', estilo = '{estilo}', comentario = '{avaltxt}' where link = '{link}' and userc = '{user}'""")
    else:
        banco.banco_cursor(conn, f"""insert into avaliacoes (link, userc, userctag, score, estilo, comentario) values ('{link}', '{user}', '{tag}', '{score}', '{estilo}', '{avaltxt}')""")

    avaluser = conn.execute(f"""select * from avaliacoes where link = '{link}' and userc = '{user}'""")
    return avaluser

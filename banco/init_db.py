import sqlite3

connection = sqlite3.connect('banco/projetec.db')

with open('banco/projetec.sql') as banco:
    connection.executescript(banco.read())

cur = connection.cursor()
cur.execute("""insert into materias (link, nome) values 
('matematica', 'Matemática'), 
('portugues', 'Português'), 
('ciencias', 'Ciências')""")

cur.execute("""insert into users (email, tag, senha, verificado) values 
('user1email@gmail.com', 'user1', '1234', 1), 
('user2email@gmail.com', 'user2', 'abcd', 0)""")

cur.execute("""insert into conteudos (link, materia, materianome, tipo, titulo, userc, userctag, userv, uservtag) values
('teoremadepitagoras', 'matematica', 'Matemática', 'Texto / Imagens', 'Teorema de Pitágoras',
'user1email@gmail.com', 'user1', 'user1email@gmail.com', 'user1'),
('testemat', 'matematica', 'Matemática', 'Texto', 'Teste Mat', 'user2email@gmail.com', 'user2',
'0', '0'),
('testeport', 'portugues', 'Português', 'Texto', 'Teste Port', 'user2email@gmail.com', 'user2',
'user1email@gmail.com', 'user1')""")

cur.execute("""insert into avaliacoes (link, userc, userctag, score, estilo, comentario) values ('teoremadepitagoras', 'user1email@gmail.com', 'user1', 5, 'cor-estrela-verde', 'Muito Bom.'),
('teoremadepitagoras', 'user2email@gmail.com', 'user2', 1, 'cor-estrela-vermelha', 'Péssimo')""")

cur.execute("""insert into blocos (tipo, conteudopag, link) values
('img', 'imagens/userimgs/exemplo.png', 'teoremadepitagoras'),
('texto', 'O Teorema de Pitágoras define que o quadrado da hipotenusa é igual a soma do quadrado dos catetos: a² = b² + c²', 'teoremadepitagoras'),
('img', 'imagens/userimgs/Prova_pitagoras_animacao.gif', 'teoremadepitagoras')""")

connection.commit()
connection.close()
drop table users;
drop table materias;
drop table conteudos;
drop table blocos;
drop table avaliacoes;

create table if not exists users(
    email varchar(50),
    tag varchar(30),
    senha varchar(12),
    verificado boolean,
    primary key(email)
);

create table if not exists materias(
    link varchar(50),
    nome varchar(50),
    primary key (link)
);

create table if not exists conteudos(
    link varchar(50),
    materia varchar(50),
    materianome varchar(50),
    tipo varchar(20),
    titulo varchar(50),
    userc varchar(50),
    userctag varchar(30),
    userv varchar(50),
    uservtag varchar(30),
    primary key (link),
    foreign key (materia) references materias (link)
);

create table if not exists blocos(
    id int auto_increment,
    tipo varchar(10),
    conteudopag varchar(200),
    link varchar(50),
    primary key (id),
    foreign key (link) references conteudos(link)
);

create table if not exists avaliacoes(
    link varchar(50),
    userc varchar(50),
    userctag varchar(30),
    score int,
    estilo varchar,
    comentario varchar(300),
    primary key (link, userc),
    foreign key (link) references conteudos(link),
    foreign key (userc) references users(email)
);
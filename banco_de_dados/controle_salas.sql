#drop database controlesalas;

create database controlesalas;
use controlesalas;
create table login(
idlogin int auto_increment primary key,
usuario varchar(100) not null,
senha varchar(100) not null
);

create table cliente(
idcliente int auto_increment primary key,
matricula varchar(20) not null,
nome varchar(30) not null,
sobrenome varchar(70) not null
);

create table ambiente(
idambiente int auto_increment primary key,
descricao varchar(255) not null,
tamanho varchar(10) not null
);

create table reserva(
idreserva int auto_increment primary key,
idcliente int,
idambiente int,
data_reserva date not null,
horario_inicio datetime not null,
horario_final datetime not null,
constraint fk_cliente_reserva foreign key (idcliente) references cliente(idcliente),
constraint fk_ambiente_reserva foreign key (idambiente) references ambiente(idambiente)
);
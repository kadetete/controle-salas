# Sistema de Controle e Gestão de Salas

*******
**Sumário**

1. [Integrantes](#integrantes)

2. [Propósito](#proposito)

3. [Ferramentas usadas no projeto](#ferramentas)

4. [Diagramas UML](#diagramas)
    - [Diagrama de caso de uso](#casouso)
    - [Diagrama de classe](#diagclasse)
    
5. [Telas](#telas)
    - [Tela de login](#telalogin)
    - [Tela do calendário](#telacalen)
    - [Tela menu](#telamenu)
    - [Telas de ambientes](#telaambiente)
    - [Tela de cadastro de clientes](#telacliente)
    - [Tela de relatório de salas reservadas](#telarelatorio)    
    
6. [Referências](#ref)

*******
<div id='integrantes'/>

## Integrantes

* Alycson Denis Pereira Moreira
* Layza Cecato Gomes Amaro
* Alessandro Nunes Silva Cruz Filho
* [Guilherme Cadete Matias](https://github/kadetete)
* Rafael Augusto Soares da Silva

<div id='proposito'/>

## Propósito

Este projeto foi proposto como trabalho de conclusão da disciplina de POO (Programação Orientada a objetos), foi sugerido um sistema para a gestão de salas, relacionando pessoas, datas e horários a uma sala para reserva. O projeto foi desenvolvido em python utilizando da biblioteca PySide6 para desenvolvimento de interfaces Qt integrado com o MySQL para o banco de dados.

<div id='ferramentas'/>

## Ferramentas usadas no projeto
Reunimos a equipe para decidir qual aplicativo seria usado para auxiliar no gerenciamento do projeto, indicada pelos integrantes da equipe, 

* [Layza Cecato](https://github.com/layzacecato-dev), adotamos o aplicativo [**TRELLO**](https://trello.com/home) para esta função como sugestão.

* Diagrama UML de caso de uso foi feito na plataforma [**CREATELY**](https://creately.com/) como sugestão de [Alycson Moreira](https://github.com/Alycson-Moreira)

* O Qt Designer foi ultilizado com ferramenta para criação das interfaces 

* O WhatsApp foi utilizado como ferramenta de comunicação rápida entre os integrantes

* Para a implementação do banco de dados foi ultilizado o sgbd MySQL WORKBENCH

<div id='diagramas'/>

## Diagramas UML

<div id='casouso'/>

### Diagrama de caso de uso
Baseado no prototipo de telas foi feito o diagrama UML de caso de uso onde nele apresentamos o fluxo e funcionalidades das telas. 

![diagrama caso de uso](img/diagrama_uml_caso_de_uso.png)

<div id='diagclasse'/>

### Diagrama de classe

<div id='telas'/>

## Telas

<div id='telalogin'/>

### Tela 01 - Login
Nessa tela o usuário do sistema, projetado para ser um funcionário de uma empresa, irá entrar com usuário e senha para acessar a área de agendamento de salas. O programa compara as informações digitadas com as presentes no banco e valida os dados para que o software possa ser utilizado.
![Tela do login](img/janela_login.jpg)

<div id='telacalen'/>

### Tela 02 - Calendário
Após o login o funcionário é redirecionado para a tela de calendário(que segue abaixo), onde é selecionado a data e horário para reserva da sala. O usuário só pode fazer reservas a partir do dia atual.
![Tela do calendário](img/demonstracao_calendario.png)

<div id='telamenu'/>

### Tela 03 - Menu
Nesta tela principal o funcionário/usuário do sistema terá a opção de escolher o ambiente que será reservado.
![Tela Principal](img/tela_principal.png)

<div id='telaambiente'/>

### Tela 04 - Ambientes
A tela apresenta a interface dos ambientes e dispões de funcionalidade de: reserva, edição e exclusão das salas, além de um botão para adicionar uma nova.
![Tela de Ambientes](img/tela_04_v6.png)

<div id='telacliente'/>

### Tela 05 - Cadastro de clientes
Aqui fazemos o cadastro do cliente que deseja reservar alguma das salas da empresa.
![Tela de Ambientes](img/cliente_cadastro.png)

<div id='telarelatorio'/>

### Tela 06 - Relatorio de Salas Reservadas
Na última tela desenvolvida, é mostrada a relação das reservas realizadas no sistema e armazenadas no banco de dados.
![Tela de Ambientes](img/relatoriodesalas.png)

<div id='ref'/>

## Referências
* Fonte utilizada no projeto: [Versa Versa](www.dafont.com/pt/versa-versa.font)
* Ferramenta utilizada para organização: [Trello](https://trello.com/home)
* Ferramenta utilizada para criação das interfaces gráficas: [Qt Creator](https://www.qt.io/product/development-tools)
* A linguagem utilizada para desenvolvimento foi Python com integração ao Qt

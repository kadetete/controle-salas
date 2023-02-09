import mysql.connector
from mysql.connector import Error
import bcrypt

class Conexao_mysql():
    try:
        def __init__(self, host ="localhost", user = "root", pwd = "", db = "controleSalas" ):
            self.host = host
            self.user = user
            self.pwd = pwd
            self.db = db
            
        def conecta(self):
            self.con = mysql.connector.connect( host     = self.host,
                                                user     = self.user,
                                                password = self.pwd,
                                                database = self.db)
            self.cur = self.con.cursor()

        def desconecta(self):
            self.con.close()

        def executa_DQL(self, sql):
            self.conecta()
            self.cur.execute(sql)
            res = self.cur.fetchall()
            self.desconecta()
            return res
        
        def executa_DML(self, sql):
            self.conecta()
            self.cur.execute(sql)
            self.con.commit()
            self.desconecta()

    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
    

class Cliente():
  def __init__(self, matricula, nome, sobrenome = None):
      self.__matricula = matricula
      self.__nome      = nome
      self.__sobrenome = sobrenome

  def incluir(self):
    c = Conexao_mysql()
    achou = False
    sql = 'SELECT * from cliente'
    for linha in c.executa_DQL(sql):
      if(f'{linha[1]}' == f'{self.__matricula}'):
        achou = True
        
    if(achou == False):       
      sql  = f"INSERT INTO cliente (matricula, nome, sobrenome) "
      sql += f"VALUES ({self.__matricula}, '{self.__nome}', '{self.__sobrenome}')"
      c.executa_DML(sql)

  def id(self):
    c = Conexao_mysql()
    sql = 'SELECT * from cliente'
    for linha in c.executa_DQL(sql):
      if(f'{linha[1]}' == f'{self.__matricula}'):
        return linha[0]
  def alterar(self, matricula, va2, va1):
        c = Conexao_mysql()
        sql  = f"UPDATE cliente "
        sql += f"SET {va1} = '{va2}' "
        sql += f"WHERE matricula = '{matricula}'"
        c.executa_DML(sql)

  def excluir(self, matricula):
    c = Conexao_mysql()
    sql  = f"DELETE FROM cliente "
    sql += f"WHERE matricula = {matricula}"
    c.executa_DML(sql)



class Login():
    def __init__(self, username, passorwd):
      self.__username = username
      self.__passorwd = passorwd.encode('utf-8')

    def incluir(self):
      achou = False
      c = Conexao_mysql()
      sql = 'SELECT * from login'
      for linha in c.executa_DQL(sql):
        if(f'{linha[1]}' == f'{self.__username}'):
          if bcrypt.checkpw(self.__passorwd , linha[2].encode('utf-8')):
            achou = True
            return True
      if(achou == False):       
        salt = bcrypt.gensalt()  
        self.__pwd_encrypt = bcrypt.hashpw(self.__passorwd, salt)
        self.__pwd_encrypt = f'{self.__pwd_encrypt}'[2:-1]
        sql  = f"INSERT INTO login (usuario, senha) "
        sql += f"VALUES ('{self.__username}', '{self.__pwd_encrypt}')"
        c.executa_DML(sql)

    def authenticate(self):
      achou = False
      c = Conexao_mysql()
      sql = 'SELECT * from login'
      for linha in c.executa_DQL(sql):
        if(f'{linha[1]}' == f'{self.__username}'):
          if bcrypt.checkpw(self.__passorwd , linha[2].encode('utf-8')):
            achou = True
            print('Login e senha validos')
            return True
          else:
            print('Senha invalida')
            return False 
      if(achou == False):
        print('Login e senha invalidos')
        return False
     
class BD_Ambientes():
  def __init__(self, id_ambiente) -> None:
    self.id_ambiente = id_ambiente
    
  def visualizar(self):
    c = Conexao_mysql()
    sql = 'SELECT * from ambiente'
    for linha in c.executa_DQL(sql):
      if(f'{linha[0]}' == f'{self.id_ambiente}'):
        descricao_sala = f'Tamanho: {linha[1]}\n'
        descricao_sala += f'Descrição:\n  {linha[2]}'
    else: 
      descricao_sala = 'Descrição'
    return descricao_sala
      
  def incluir(self, descricao, tamanho):
    c = Conexao_mysql()
    achou = False
    sql = 'SELECT * from ambiente'
    print(self.id_ambiente, descricao, tamanho)
    for linha in c.executa_DQL(sql):
      if(f'{linha[0]}' == f'{self.id_ambiente}'):
        self.alterar(descricao, tamanho)
        achou = True
        
    if(achou == False):     
      print(sql)  
      sql  = f"INSERT INTO ambiente (idambiente, descricao, tamanho) "
      sql += f"VALUES ({self.id_ambiente}, '{descricao}', '{tamanho}')"
      print(sql) 
      c.executa_DML(sql)

  def alterar(self, descricao, tamanho):
      c = Conexao_mysql()
      sql  = f"UPDATE ambiente "
      sql += f"SET descricao = '{descricao}', tamanho = '{tamanho}' "
      sql += f"WHERE idambiente = {self.id_ambiente}"
      c.executa_DML(sql)

class Reseva():
  def __init__(self, idcliente, idambiente, data_reserva, horario_inicio, horario_final):
    self.__idcliente      = idcliente
    self.__idambiente     = idambiente
    data_reserva   = f"{data_reserva[2]}-{self.formatarData(data_reserva[1], data_reserva[0], '-')}"
    self.__data_reserva = data_reserva 
    horario_inicio = f"{self.formatarData(horario_inicio[0], horario_inicio[1], ':')}:00"
    self.__horario_inicio = horario_inicio
    horario_final  = f"{self.formatarData(horario_final[0], horario_final[1], ':')}:00"
    self.__horario_final = horario_final

  def verificar_resevas(self):
      c = Conexao_mysql()
      sql  = f"INSERT INTO reserva (idcliente, idambiente, data_reserva, horario_inicio, horario_final) "
      sql += f"VALUES ({self.__idcliente}, {self.__idambiente}, '{self.__data_reserva}', '{self.__horario_inicio}', '{self.__horario_final}')"
      c.executa_DML(sql)
      
  def formatarData(self, hora, min, sinal):
    self.hora = hora
    self.min = min
    if self.hora < 10:
      self.hora = f'0{self.hora}'
    if self.min < 10:
      self.min = f'0{self.min}'
    return f'{self.hora}{sinal}{self.min}'
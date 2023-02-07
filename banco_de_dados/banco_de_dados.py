import mysql.connector
from mysql.connector import Error
import bcrypt

class Conexao_mysql():
    try:
        def __init__(self, host ="localhost", user = "root", pwd = "", db = "controlesalas" ):
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
      
class CadastroAmbientes():
  def __init__(self, idambiente, descricao, tamanho):
    self.__idambiente = idambiente
    self.__descricao  = descricao
    self.__tamanho    = tamanho

  def incluir(self):
    c = Conexao_mysql()
    achou = False
    sql = 'SELECT * from ambiente'
    for linha in c.executa_DQL(sql):
      if(f'{linha[0]}' == f'{self.__idambiente}'):
        achou = True
        
    if(achou == False):       
      sql  = f"INSERT INTO ambiente (idambiente, descricao, tamanho) "
      sql += f"VALUES ({self.__idambiente}, '{self.__descricao}', '{self.__tamanho}')"
      c.executa_DML(sql)

  def alterar(self, idambiente, va2, va1):
        c = Conexao_mysql()
        sql  = f"UPDATE ambiente "
        sql += f"SET {va1} = '{va2}' "
        sql += f"WHERE idambiente = '{idambiente}'"
        c.executa_DML(sql)
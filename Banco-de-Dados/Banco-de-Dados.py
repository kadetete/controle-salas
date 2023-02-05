from ConexaoBD import *
import bcrypt

class cadastro_user():
    def __init__(self, matricula, nome, sobrenome = None):
        self.__matricula = matricula
        self.__nome      = nome
        self.__sobrenome = sobrenome

    def incluir(self):
        c = ConexaoBD()
        sql  = f"INSERT INTO cliente (matricula, nome, sobrenome) "
        sql += f"VALUES ({self.__matricula}, '{self.__nome}', '{self.__sobrenome}')"
        c.executa_DML(sql)

    def alterar(self, matricula, va2, va1):
        c = ConexaoBD()
        sql  = f"UPDATE cliente "
        sql += f"SET {va1} = '{va2}' "
        sql += f"WHERE matricula = {matricula}"
        c.executa_DML(sql)

    def excluir(self, matricula):
        c = ConexaoBD()
        sql  = f"DELETE FROM cliente "
        sql += f"WHERE matricula = {matricula}"
        c.executa_DML(sql)

S = cadastro_user(1234, 'Beto', '')        
S.incluir()
S.alterar(2022114, 'Soares', 'Sobrenome')
#S.excluir(1234)

class Login():
    def __init__(self, username, passorwd):
      self.__username = username
      self.__passorwd = passorwd.encode('utf-8')

    def incluir(self):
      achou = False
      c = ConexaoBD()
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
        c = ConexaoBD()
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
            
            
login = Login('Admin', '12345')
login.incluir()
login.authenticate()
login2 = Login('Fulano', '67890')
login2.incluir()
login2.authenticate()

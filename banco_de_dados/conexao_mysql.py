import mysql.connector
from mysql.connector import Error
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
    

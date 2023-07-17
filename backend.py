import sqlite3
def cadastrar (self):
    pass

def entrar(self):
    pass

class backend():
    def conecta_banco(self):
        self.conexao = sqlite3.connect('snac_banco.db')
        self.sql = self.conexao.cursor()
        print('Bando de dados ativado!')

    def desconecta_banco(self):
        self.conexao.close()
        print('Banco de dados desconectado')

    def criar_banco(self):
        self.conecta_banco()
        self.sql.execute(
            '''
            CREATE TABLE IF NOT EXISTS usuarios
            (id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            confirmarSenha TEXT NOT NULL)
            ''')
        
        self.conexao.commit()
        print('Tabela de dados criada!')
        self.desconecta_banco()
        pass
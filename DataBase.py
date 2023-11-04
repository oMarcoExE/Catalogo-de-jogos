import sqlite3

class DataBase:
    def __init__(self, banco_dados):
        self.concetarBanco(banco_dados)

    def concetarBanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)
        self.cursor = self.banco.cursor()

        self.criarTabelaFilmes()
        
    def criarTabelaFilmes(self):
       self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jogos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                desenvolvedora TEXT NULL,
                distribuidora TEXT NULL,
                ano TEXT NULL
                           
            )
        """)
       

    def inserir(self, tabela, valores):
        colunas = ', '.join(valores.keys())
        placeholders = ', '.join(['? '] * len(valores))

        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"

        self.cursor.execute(sql, tuple(valores.values()))
        self.banco.commit()
        if self.cursor.lastrowid:
            print(f"{tabela} salvo com sucesso!")
            return True
        else:
            print("Erro ao cadastrar dados!")
            return False       

    def buscarDados(self, tabela, campos = '*'):
        sql = f"SELECT {campos} from {tabela}"
        self.cursor.execute(sql)
        
        dados = self.cursor.fetchall()
        return dados
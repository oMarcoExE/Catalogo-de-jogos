import os
from DataBase import DataBase

class UI:
    def __init__(self):
        self.banco = DataBase("catalogoJogos.db")

    def logo(self):
        print("- - - - - - - - - - - - - - -")
        print("- -  - Steam em python- - - -")
        print("- - - - - - - - - - - - - - -")
        print()

    def mostrarMenu(self):
        print("1- Adiconar gamee a biblioteca")
        print("2- Ver biblioteca")
        print("0- Sair")
        print()

    def limparTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def selecionaOpcao(self, opcoes = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoes)

        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção não encontrada!")
            return self.selecionaOpcao(opcoes)

        if opcaoSelecionada not in opcoes:
            print("Opção não encontrada!")
            return self.selecionaOpcao(opcoes)
        
        return opcaoSelecionada
        
    def Bibliotecajogos(self):
        self.logo()

        print("Insira os dados do seu jogo:")
        print("campos com * são obrigatórios")
        
        titulo = self.solicitaValor("Digite o titulo* ", 'texto', False)
        genero = self.solicitaValor("Digite o gênero ", 'texto', True)
        desenvolvedora = self.solicitaValor("Digite a desenvolvedora ", 'numero', True)
        distribuidora = self.solicitaValor("Digite o distribuidora ", 'texto', True)
        ano = self.solicitaValor("Digite o ano* ", 'numero', False)

        valores = {
            "titulo": titulo,
            "genero": genero,
            "desenvolvedora": desenvolvedora,
            "distribuidora": distribuidora,
            "ano": ano,
        }

        self.banco.inserir('jogos', valores)


    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.solicitaValor(legenda, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
           return valor
       
        if tipo == 'numero':
            try:
               valor = float(valor)
            except ValueError:
               print("Valor invalida!")
               return self.solicitaValor(legenda, tipo, permiteNulo)
        return valor


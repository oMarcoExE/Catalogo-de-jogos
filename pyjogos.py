from ui import UI
from DataBase import DataBase

dUi = UI()

opcao = ""
while opcao != 0:
    dUi.logo()
    dUi.mostrarMenu()
    opcao = dUi.selecionaOpcao([1, 2, 0])
    dUi.limparTela()

    if opcao == 1:
        dUi.Bibliotecajogos()
        opcao = ""

    if opcao == 2:
        dUi.Biblioteca()
        opcao = ""
        dUi.limparTela
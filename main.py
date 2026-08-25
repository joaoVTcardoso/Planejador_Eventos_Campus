import os
import funcoes_aluno_A
import funcoes_aluno_B

# funcao de dar espaço entre resultados    
def espaco_vazio():
    print("")

# funcao para confirmar no enter
def enter_confirm():
    verificar_enter = input("digite ENTER para continuar...")
    if verificar_enter == ' ':
        return 0
    else:
        print("Voce nao apertou enter")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def displayMenu():
    print("=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Sair ")

def menu_principal():

    while True:
        espaco_vazio()
        displayMenu()   
        espaco_vazio()

        opcoes = input("Digite o numero da opção que deseja: ")

        if opcoes == '1':
            limpar_tela()

            nome , data, local , genero = funcoes_aluno_A.lerValoresEvento()
            funcoes_aluno_A.adicionarEvento(funcoes_aluno_A.listaEventos, nome, data , local , genero)

            espaco_vazio()
            enter_confirm()
            espaco_vazio()

        elif opcoes == '2':
            limpar_tela()
            print("Lista atual de eventos: ")
            espaco_vazio()
            funcoes_aluno_A.mostrar_eventos(funcoes_aluno_A.lista_eventos)
            espaco_vazio()
            enter_confirm()
            espaco_vazio()

        elif opcoes == '3':
            limpar_tela()
            categoria = funcoes_aluno_A.lerValoresEvento
            funcoes_aluno_B.filtrarEventosPorCategoria(funcoes_aluno_A.listaEventos, categoria)
            print("teste03")
            
        elif opcoes == '4':
            limpar_tela()
            print("teste04")

        elif opcoes == '5':
            limpar_tela()
            print("teste05")

        elif opcoes == '6':
            limpar_tela()
            print("teste06")
        
        else:
            limpar_tela()
            print("opcao digitada nao é valida")

if __name__ == "__main__":
    menu_principal()
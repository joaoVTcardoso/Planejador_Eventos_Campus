import os
import funcoes_aluno_A
import funcoes_aluno_B

# funcao de dar espaço entre resultados    
def espaco_vazio():
    print("")

# funcao para confirmar no enter
def enter_confirm():
    verificar_enter = input("digite ENTER para continuar...")
    if verificar_enter == '':
        return 0
    else:
        print("Voce nao apertou enter")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def displayMenu():
    print("=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Pesquisar Eventos por Nome")
    print("4. Filtrar por Categoria")
    print("5. Marcar Evento como Participado")
    print("6. Deletar Evento")
    print("7. Gerar Relatório")
    print("8. Sair ")

def menu_principal():

    while True:
        displayMenu()   
        espaco_vazio()

        opcoes = input("Digite o numero da opção que deseja: ")

        if opcoes == '1':
            limpar_tela()

            nome, data, local, genero = funcoes_aluno_A.lerValoresEvento()
            funcoes_aluno_A.adicionarEvento(funcoes_aluno_A.lista_eventos, nome, data, local, genero)

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
            espaco_vazio()
            funcoes_aluno_A.pesquisaPorNomeEventos(funcoes_aluno_A.lista_eventos)
            espaco_vazio()

        elif opcoes == '4':
            limpar_tela()
            espaco_vazio()
            cat = input("Digite a categoria desejada: ")
            resultado = funcoes_aluno_B.filtrarEventosPorCategoria(funcoes_aluno_A.lista_eventos, cat)
            for evento in resultado:
                print("-", evento["nome"])
            espaco_vazio()
            enter_confirm()
            espaco_vazio()

        elif opcoes == '5':
            limpar_tela()
            espaco_vazio()
            id_ev = int(input("Digite o ID do evento que participou: "))
            funcoes_aluno_B.marcarEventoAtendido(funcoes_aluno_A.lista_eventos, id_ev)
            espaco_vazio()
            enter_confirm()
            espaco_vazio()

        elif opcoes == '6':
            limpar_tela()
            funcoes_aluno_A.deletarEvento(funcoes_aluno_A.lista_eventos)

        elif opcoes == '7':
            limpar_tela()
            espaco_vazio()
            funcoes_aluno_B.gerarRelatorio(funcoes_aluno_A.lista_eventos)
            espaco_vazio()
            enter_confirm()
            espaco_vazio()

        elif opcoes == '8':
            limpar_tela()
            print("teste08")
        
        else:
            limpar_tela()
            print("opcao digitada nao é valida")

if __name__ == "__main__":
    menu_principal()
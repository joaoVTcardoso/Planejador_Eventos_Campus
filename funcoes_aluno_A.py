import main
import funcoes_aluno_B

lista_eventos = []
lista_eventos_geral = []

def mostraEventoDetalhado (evento):
    print("Nome do evento:", evento["nome"])
    print("Data do evento:", evento["data"])
    print("Local do evento:", evento["local"])
    print("Categoria do evento:", evento["categoria"])
    print("\n")



def mostrar_eventos(lista_eventos):
    for indice, evento in enumerate(lista_eventos):
        print(indice+1,") Nome: ", evento["nome"])



def lerValoresEvento ():
    adicionar_evento_nome  = input("\ndigite o nome evento que voce deseja adicionar: ")
    adicionar_evento_data  = input("\ndigite a data de realização dele: ")
    adicionar_evento_local  = input("\ndigite o local onde acontecera o evento: ")
    adicionar_evento_genero  = input("\ndigite qual o tipo de evento: ")
    return adicionar_evento_nome, adicionar_evento_data, adicionar_evento_local, adicionar_evento_genero

# função para adicionar listas
def adicionarEvento(listaEventos, nome, data, local, categoria):            
    
    if (len(lista_eventos) == 0):
        id = 1
    else:
        id = lista_eventos[-1]["id"] + 1

    evento = {
        "id": id,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria
    }
 
    listaEventos.append(evento)
        
        
#funcao de mostra a lista de eventos


def menu_adicionar_evento():
    while True:
        print("1. Mostrar os eventos atuais")
        print("2. Adicionar um evento a sua lista de eventos")
        print("3. sair\n")

        opcao =  input("digite a opção desejada: ")
        if opcao == '1':
            main.espaco_vazio()
            mostrar_eventos()
            main.espaco_vazio()
            main.enter_confirm()
            main.espaco_vazio()

        elif opcao == '2':
            adicionarEvento()

        elif opcao == '3':
            print("\ntchau :)\n")
            break
        
        else:
            main.espaco_vazio()
            print("voce nao digitou nenhum carctere disponivel, tente novamente")
            main.espaco_vazio()
    
def pesquisaPorNomeEventos(eventos):
    nome_buscado = str(input("Digite o nome do evento que deseja pesquisar: "))
    main.espaco_vazio()
    flag = False

    if nome_buscado == "":
        main.espaco_vazio()
        print("Voce nao digitou nada")
        main.espaco_vazio()
    else:  
        for evento in eventos:
            if evento["nome"] == nome_buscado:
                flag = True
                mostraEventoDetalhado(evento) 

                main.enter_confirm()
                main.espaco_vazio()
        
        if (flag == False):
            print("Não foi possível encontrar o")

def deletarEvento(listaparaDeletar):
    evento_a_deletar = int(input("digite um numero do evento que deseja deletar(ordem crecente): "))
    achei = None
    main.espaco_vazio()    
    for evento in listaparaDeletar:
        if evento_a_deletar == evento["id"]:            
            achei = evento
            break

    if (achei != None):
        confirmar_delet = input("Digite ENTER para confirmar que quer deletar o evento...")
        if confirmar_delet == '':
            listaparaDeletar.remove(achei)
            main.espaco_vazio()
            print("O evento foi deletado!")
            main.espaco_vazio()
        else:
            print("Voce nao digitou ENTER")
    else:
        print("Nao foi possivel deletar o evento")

import main
import funcoes_aluno_A


def filtrarEventosPorCategoria(listaEventos, categoria):
    eventos_filtrados = []
    for evento in listaEventos:
        if evento["categoria"].lower() == categoria.lower():
            eventos_filtrados.append(evento)
            print("Eventos disponiveis de acordo com a categoria: ", evento["categoria"])
    return eventos_filtrados


def marcarEventoAtendido(listaEventos, id_evento):
    encontrou = False
    for evento in listaEventos:
        if str(evento["id"]) == str(id_evento):
            evento["participado"] = True
            encontrou = True
            print("\nEvento marcado como participado com sucesso!")
            break
            
    if encontrou == False:
        print("\nNenhum evento foi encontrado com esse ID.")


def gerarRelatorio(listaEventos):
    total_eventos = len(listaEventos)
    
    if total_eventos == 0:
        print("\nNao existem eventos cadastrados para mostrar o relatorio.")
    else:
        participados = 0
        
        for evento in listaEventos:
            if evento.get("participado") == True:
                participados = participados + 1
        
        porcentagem = (participados / total_eventos) * 100
        
        print("\n--- RELATORIO DE EVENTOS ---")
        print("Total de eventos:", total_eventos)
        print("Eventos participados:", participados)
        print("Porcentagem de participacao:", porcentagem, "%")
        print("\nEventos por categoria:")
        
        
        categorias_vistas = []
        for evento in listaEventos:
            cat = evento["categoria"]
            if cat not in categorias_vistas:
                categorias_vistas.append(cat)
                
                
                contador = 0
                for e in listaEventos:
                    if e["categoria"] == cat:
                        contador = contador + 1
                print("-", cat, ":", contador)
        print("----------------------------\n")
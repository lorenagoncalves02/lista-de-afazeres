lista = []

loop = True

while loop == True:
    print("""
    ----------------------------
    |    LISTA DE AFAZERES     |
    ----------------------------
    |1 - Inserir tarefa        |
    |2 - Listar tarefas        |
    |3 - Marcar como concluído |
    |4 - Remover tarefa        |
    |0 - Sair                  | 
    ---------------------------- """)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        tarefa = input("Qual é a sua tarefa? ")
        lista.append(tarefa)
    
    elif opcao == 2:
        for tarefa in lista:
            print(tarefa)

    elif opcao == 3:
        contador = 0
        


    elif opcao == 4:
        remover = input("Qual item você quer remover? ")
        lista.remove(remover)
        

    elif opcao == 0:
        loop = False





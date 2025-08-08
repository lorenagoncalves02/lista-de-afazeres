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
        with open("arquivo.txt", "w") as arquivo:
            for tarefa in lista:
                arquivo.write(tarefa + "\n")

        add = input("Você deseja adicionar mais alguma tarefa?")
        if add == "sim":
            tarefa = input("Qual é a sua tarefa? ")
            lista.append(tarefa)
            with open("arquivo.txt", "w") as arquivo:
                for tarefa in lista:
                    arquivo.write(tarefa + "\n")
            
    
    elif opcao == 2:
        for tarefa in lista:
            print(tarefa)


    elif opcao == 3:
        contador = 0

        for x in lista:
            print(f"""{contador}-{x}""")
            contador = contador + 1

        marcar = int(input("Qual item você deseja marcar como concluído?"))
        lista[marcar] = lista[marcar] + " ✓"
        print(lista)



    elif opcao == 4:
        remover = int(input("Qual item você deseja remover? (digite o número do item)"))
        lista.pop(remover)
        print(lista)
        
        

    elif opcao == 0:
        loop = False

















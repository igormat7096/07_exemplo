import os

nomes = []

#loop
while True:
    #menu
    print("1 - Cadastrar novo nome.")
    print("2 - Exebir a lista.")
    print("3 - Ordernar lista.")
    print("4 - Alterar nome da lista.")
    print("5 - Excluir nome da lista.")
    print("6 - Sair do programa.")
    
    #usuário informa a opção escolhida 
    opcao = input("Opção desejada: ")

    #limpa console
    os.system("cls")

    #programa verifica a opção escolhida pelo usuário
    match opcao:
        case "1":
            novo_nome = input("Informe o nome a ser cadstrado: ")
            nomes.append(novo_nome)
            print(f"{novo_nome} Cadastrado com sucesso.")
            continue
        
        case "2":
            print("LISTA:\n")
            for i in range(len(nomes)):
                print(f"Índice {i}: {nomes[i]}.")
            print("\n")
            continue
        
        case "3":
            nomes.sort()
            print("Lista ordenada com sucesso.")
            continue
        
        case "4":
            try:
              indice = int(input("Informe o índice do nome a ser alterados: "))
              confirmar = input(f"Deseja alterar {nomes[indice]}? Digite 'sim' para confirmar:  ") 

              if confirmar == "sim":
                  nomes[indice] = input("Informe o novo nome: ")
              else:
                  print("Nome não foi alterado.")        
            except Exception as e:
                print(f"Não foi possivel alterara. {e}.")
            finally:
                continue
        
        case "5":
            try:
             indice = int(input("Informe o índice do nome qie deseja excluir: "))
             confirmar = input(f"Deseja excluir o nome {nomes[indice]}? Digite 'sim' para confirmar: ")

             if confirmar == "sim":
                    del(nomes[indice])
                    print("Nome excluido com sucesso.")
             else:
                    print("Nome não foi excluido.") 
            except Exception as e:
                print(f"Não foi possivel excluir o nome. {e}.")
            finally:
                continue
       
        case "6":
             print("Programa encerrado!")
             break
        case _:
            print("Opção inválida.")
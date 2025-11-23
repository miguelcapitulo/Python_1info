while True:
    print("O que você deseja fazer? \n [1] Inserir um projeto \n [2] Listar \n [3] Buscar projeto \n [4]Atualizar projeto \n [5] Remover um projeto \n [6] Remover TODOS os Dados \n [0] Sair")
    opPro=input("digite qual opção deseja: ")
    if opPro=="1":
        from datetime import datetime

        while True:
            nome = input("Digite o nome do projeto: ").strip()

            if len(nome) < 3:
                print("O nome deve ter pelo menos 3 caracteres!")
                
            else:
                break
        descricao=input("Digite a descrição do projeto:")


        def ler_data(mensagem):
            while True:
                data_str = input(mensagem)
                try:
                    data = datetime.strptime(data_str, "%d/%m/%Y")
                    return data
                except ValueError:
                    print("Data inválida! Use o formato DD/MM/AAAA.\n")
        data_inicio = ler_data("Digite a data de início (DD/MM/AAAA): ")
        data_fim = ler_data("Digite a data de fim (DD/MM/AAAA): ")

        while data_fim < data_inicio:
            print("A data de fim não pode ser ANTES da data de início!\n")
            data_fim = ler_data("Digite novamente a data de fim (DD/MM/AAAA): ")

        print("Datas válidas!")
        
        IdPRO={
        "Nome:":nome,
        "Descrição:":descricao,
        "Dada de início":data_inicio.strftime("%d/%m/%Y"),
        "Dada de fim":data_fim.strftime("%d/%m/%Y")
        }
        print(IdPRO)
    opPro=input("Digite qual opção deseja: ")
    if opPro=="4":
        print("Qual dado você deseja atualizar? digite [1] para nome , [2] para descrição , [3] para datas")
        attPro=input("O que você deseja?")
        if attPro=="1":
            while True:
                nome = input("Digite o nome do projeto: ").strip()

                if len(nome) < 3:
                    print("O nome deve ter pelo menos 3 caracteres!")
                
                else:
                    break
        if attPro=="2":
            descricao=input("Digite a descrição do projeto:")
        if attPro=="3":
            def ler_data(mensagem):
                while True:
                    data_str = input(mensagem)
                    try:
                        data = datetime.strptime(data_str, "%d/%m/%Y")
                        return data
                    except ValueError:
                        print("Data inválida! Use o formato DD/MM/AAAA.\n")
            data_inicio = ler_data("Digite a data de início (DD/MM/AAAA): ")
            data_fim = ler_data("Digite a data de fim (DD/MM/AAAA): ")

            while data_fim < data_inicio:
                print("A data de fim não pode ser ANTES da data de início!\n")
                data_fim = ler_data("Digite novamente a data de fim (DD/MM/AAAA): ")
                print("Datas válidas!")
                IdPRO={
            "Nome:":nome,
            "Descrição:":descricao,
            "Dada de início":data_inicio.strftime("%d/%m/%Y"),
            "Dada de fim":data_fim.strftime("%d/%m/%Y")
            }
            print(IdPRO)
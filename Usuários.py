while True:
    print("[1] Inserir usuários \n[2] Listar  \n[3] Buscar nome ou email \n[4]Atualizar Dados \n[5] Remover Dados\n[6] Remover TODOS os Dados\n[0] Sair")
    opUS=input("digite qual opção deseja: ")
    if opUS=="1":
        while True:
            nome = input("Digite o seu nome: ")

            if len(nome) < 3:
                print("O nome deve ter pelo menos 3 caracteres!")
            else:
                break
        
        while True:
            email = input("Insira o seu email: ")

            if email.count("@")!=1:
                print("Invalido,Tente Novamente")
                continue
            
            usuario,dominio=email.split("@")

            if not usuario:
                print("Email inválido! Deve haver algo antes do '@'.")
                continue
            if not dominio:
                print("Email inválido! Deve haver algo após o '@'.")
                continue
            if "." not in dominio or dominio.startswith(".") or dominio.endswith("."):
                print("Email inválido! O domínio deve conter um ponto válido.")
                continue
            print("Email válido!")
            break

        while True:
            perfil=input("Insira o seu perfil: ")
            if perfil=="":
                print("invalido,tente novamente")
            else:
                break
        IdUS={
        "Nome:":nome,
        "Email:":email,
        "Perfil":perfil
        }
        print(IdUS)

    if opUS=="4":
        print("qual dado você deseja atualizar? digite [1] para nome , [2] para email , [3] para perfil")
        att=input("digite a opção que deseja: ")

        if att=="1":

            while True:
                nome = input("Digite o seu nome: ")

                if len(nome) < 3:
                    print("O nome deve ter pelo menos 3 caracteres!")
                else:
                    break
        elif att=="2":

            while True:
                email = input("Insira o seu email: ")

                if email.count("@")!=1:
                    print("Invalido,Tente Novamente")
                    continue
                
                usuario,dominio=email.split("@")

                if not usuario:
                    print("Email inválido! Deve haver algo antes do '@'.")
                    continue
                if not dominio:
                    print("Email inválido! Deve haver algo após o '@'.")
                    continue
                if "." not in dominio or dominio.startswith(".") or dominio.endswith("."):
                    print("Email inválido! O domínio deve conter um ponto válido.")
                    continue
                print("Email válido!")
                break
        elif att=="3":

            while True:
                perfil=input("Insira o seu perfil: ")
                if perfil=="":
                    print("invalido,tente novamente")
                else:
                    break
        IdUS={
        "Nome:":nome,
        "Email:":email,
        "Perfil":perfil
        }
        print(IdUS)

        if opUS=="0":
            break

        

        
        








        
    



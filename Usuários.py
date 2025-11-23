import json

# ---------- FUNÇÕES PARA VALIDAÇÃO ----------

def validar_nome():
    while True:
        nome = input("Digite o seu nome: ")
        if len(nome) < 3:
            print("Nome deve ter pelo menos 3 caracteres.")
        else:
            return nome

def validar_email():
    while True:
        email = input("Insira o seu email: ")
        if email.count("@") != 1:
            print("Email inválido.")
            continue

        usuario, dominio = email.split("@")
        if not usuario or not dominio or "." not in dominio:
            print("Email inválido.")
        else:
            return email

def validar_perfil():
    while True:
        perfil = input("Insira o seu perfil: ")
        if perfil.strip() == "":
            print("Perfil inválido.")
        else:
            return perfil

# ---------- FUNÇÕES PARA JSON ----------

def salvar_json(usuarios):
    with open("data/usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump({"usuarios": usuarios}, arquivo, indent=4, ensure_ascii=False)

def carregar_json():
    try:
        with open("data/usuarios.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)["usuarios"]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Carregar dados ao iniciar
usuarios = carregar_json()

# ---------- MENU PRINCIPAL ----------

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("[1] Inserir usuário")
    print("[2] Listar usuários")
    print("[3] Buscar por nome ou email")
    print("[4] Atualizar dados")
    print("[5] Remover usuário")
    print("[6] Remover TODOS os usuários")
    print("[0] Sair")
    
    opUS = input("Digite a opção desejada: ")

    if opUS == "1":  # Inserir
        nome = validar_nome()
        email = validar_email()
        perfil = validar_perfil()
        usuarios.append({"Nome": nome, "Email": email, "Perfil": perfil})
        salvar_json(usuarios)

    elif opUS == "2":  # Listar
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for u in usuarios:
                print(u)

    elif opUS == "3":  # Buscar
        termo = input("Digite nome ou email para busca: ").lower()
        encontrados = [u for u in usuarios if termo in u["Nome"].lower() or termo in u["Email"].lower()]
        print(encontrados if encontrados else "Nenhum usuário encontrado.")

    elif opUS == "4":  # Atualizar
        email_ref = input("Digite o email do usuário para atualização: ")
        for u in usuarios:
            if u["Email"] == email_ref:
                print("[1] Nome  [2] Email  [3] Perfil")
                att = input("Escolha a opção: ")
                if att == "1":
                    u["Nome"] = validar_nome()
                elif att == "2":
                    u["Email"] = validar_email()
                elif att == "3":
                    u["Perfil"] = validar_perfil()
                salvar_json(usuarios)
                break
        else:
            print("Usuário não encontrado.")

    elif opUS == "5":  # Remover
        email_ref = input("Digite o email do usuário que deseja remover: ")
        usuarios = [u for u in usuarios if u["Email"] != email_ref]
        salvar_json(usuarios)

    elif opUS == "6":  # Remover TODOS
        usuarios.clear()
        salvar_json(usuarios)

    elif opUS == "0":  # Sair
        break

    else:
        print("Opção inválida.")

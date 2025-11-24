import json
from datetime import datetime

# Carregar dados existentes
def carregar_projetos():
    try:
        with open("data/projeto.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
            if isinstance(dados, list):  # Corrige JSON errado
                return {}
            return dados
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# Salvar dados
def salvar_projetos(projetos):
    with open("data/projeto.json", "w", encoding="utf-8") as f:
        json.dump(projetos, f, indent=4, ensure_ascii=False)

# Ler datas
def ler_data(mensagem):
    while True:
        data_str = input(mensagem)
        try:
            return datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            print("Data inválida! Use o formato DD/MM/AAAA.\n")

# ------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------

projetos = carregar_projetos()

while True:
    print("\nO que você deseja fazer?")
    print("[1] Inserir projeto")
    print("[2] Listar projetos")
    print("[3] Buscar projeto")
    print("[4] Atualizar projeto")
    print("[5] Remover projeto")
    print("[6] Remover TODOS os projetos")
    print("[0] Sair")

    op = input("Escolha: ")

    # 1 - Inserir
    if op == "1":
        nome = input("Digite o nome do projeto: ").strip()

        if nome in projetos:
            print("Já existe um projeto com esse nome!")
            continue

        descricao = input("Digite a descrição: ")

        data_inicio = ler_data("Data início (DD/MM/AAAA): ")
        data_fim = ler_data("Data fim (DD/MM/AAAA): ")

        while data_fim < data_inicio:
            print("Data de fim não pode ser antes da de início!")
            data_fim = ler_data("Data fim (DD/MM/AAAA): ")

        projetos[nome] = {
            "nome": nome,
            "descricao": descricao,
            "data_inicio": data_inicio.strftime("%d/%m/%Y"),
            "data_fim": data_fim.strftime("%d/%m/%Y")
        }

        salvar_projetos(projetos)
        print("Projeto salvo com sucesso!")

    # 2 - Listar
    elif op == "2":
        if not projetos:
            print("Nenhum projeto cadastrado.")
        else:
            for p in projetos.values():
                print("\n------------------------")
                print("Nome:", p["nome"])
                print("Descrição:", p["descricao"])
                print("Início:", p["data_inicio"])
                print("Fim:", p["data_fim"])

    # 3 - Buscar
    elif op == "3":
        nome = input("Nome do projeto: ")
        if nome in projetos:
            p = projetos[nome]
            print("\nProjeto encontrado:")
            print("Nome:", p["nome"])
            print("Descrição:", p["descricao"])
            print("Início:", p["data_inicio"])
            print("Fim:", p["data_fim"])
        else:
            print("Projeto não encontrado.")

    # 4 - Atualizar
    elif op == "4":
        nome = input("Nome do projeto para atualizar: ")

        if nome not in projetos:
            print("Projeto não encontrado.")
            continue

        print("[1] Atualizar nome")
        print("[2] Atualizar descrição")
        print("[3] Atualizar datas")

        att = input("Escolha: ")

        if att == "1":
            novo_nome = input("Novo nome: ").strip()

            if novo_nome in projetos:
                print("Já existe projeto com esse nome!")
                continue

            projetos[novo_nome] = projetos.pop(nome)
            projetos[novo_nome]["nome"] = novo_nome

        elif att == "2":
            projetos[nome]["descricao"] = input("Nova descrição: ")

        elif att == "3":
            data_inicio = ler_data("Nova data início: ")
            data_fim = ler_data("Nova data fim: ")

            while data_fim < data_inicio:
                print("Data de fim não pode ser antes da de início!")
                data_fim = ler_data("Nova data fim: ")

            projetos[nome]["data_inicio"] = data_inicio.strftime("%d/%m/%Y")
            projetos[nome]["data_fim"] = data_fim.strftime("%d/%m/%Y")

        else:
            print("Opção inválida.")
            continue

        salvar_projetos(projetos)
        print("Projeto atualizado!")

    # 5 - Remover
    elif op == "5":
        nome = input("Nome do projeto para remover: ")
        if nome in projetos:
            projetos.pop(nome)
            salvar_projetos(projetos)
            print("Projeto removido!")
        else:
            print("Projeto não encontrado.")

    # 6 - Remover tudo
    elif op == "6":
        confirmar = input("Tem certeza? (s/n): ").lower()
        if confirmar == "s":
            projetos = {}
            salvar_projetos(projetos)
            print("Todos os projetos foram apagados!")

    # 0 - Sair
    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
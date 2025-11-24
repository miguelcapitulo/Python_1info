import json
from datetime import datetime

# ---------- FUNÇÕES AUXILIARES ----------

def carregar_json(caminho, tipo="lista"):
    """Carrega um JSON e garante o tipo correto (lista ou dict)"""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
            if tipo == "lista":
                return dados if isinstance(dados, list) else []
            return dados if isinstance(dados, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return [] if tipo == "lista" else {}

def salvar_json(caminho, dados):
    """Salva dados em um JSON"""
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def ler_data(mensagem):
    """Valida e lê data no formato DD/MM/YYYY"""
    while True:
        data_str = input(mensagem).strip()
        try:
            datetime.strptime(data_str, "%d/%m/%Y")
            return data_str
        except ValueError:
            print("Data inválida! Use o formato DD/MM/YYYY.")

def listar_tarefas(filtro=None, valor=None):
    """Lista tarefas, opcionalmente filtradas"""
    tarefas = carregar_json("data/tarefas.json", tipo="lista")
    if filtro and valor:
        tarefas = [t for t in tarefas if t.get(filtro) == valor]

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, t in enumerate(tarefas):
            print(f"{i} - Título: {t['titulo']} | Projeto: {t['projeto']} | "
                  f"Responsável: {t['responsavel']} | Status: {t['status']} | Prazo: {t['prazo']}")

# ---------- FUNÇÕES DE TAREFA ----------

def cadastrar_tarefa():
    titulo = input("Título da tarefa: ").strip()
    projeto = input("Projeto relacionado: ").strip()
    responsavel = input("Responsável pela tarefa: ").strip()
    prazo = ler_data("Prazo (DD/MM/YYYY): ")
    status = "pendente"

    # Verifica se o projeto existe
    projetos = carregar_json("data/projeto.json", tipo="dict")
    if projeto not in projetos:
        print(f"Projeto '{projeto}' não encontrado em projeto.json.")
        return

    # Verifica se o responsável existe
    usuarios_data = carregar_json("data/usuarios.json", tipo="dict")
    usuarios = usuarios_data.get("usuarios", [])
    if not any(u["Nome"] == responsavel for u in usuarios):
        print(f"Usuário '{responsavel}' não encontrado em usuarios.json.")
        return

    tarefas = carregar_json("data/tarefas.json", tipo="lista")
    tarefas.append({
        "titulo": titulo,
        "projeto": projeto,
        "responsavel": responsavel,
        "status": status,
        "prazo": prazo
    })
    salvar_json("data/tarefas.json", tarefas)
    print("Tarefa cadastrada com sucesso!")

def atualizar_tarefa():
    listar_tarefas()
    tarefas = carregar_json("data/tarefas.json", tipo="lista")
    try:
        idx = int(input("Índice da tarefa a atualizar: "))
        tarefa = tarefas[idx]
    except (ValueError, IndexError):
        print("Índice inválido.")
        return

    campo = input("Campo a atualizar (titulo/projeto/responsavel/status/prazo): ").strip().lower()
    if campo not in ["titulo", "projeto", "responsavel", "status", "prazo"]:
        print("Campo inválido.")
        return

    if campo == "projeto":
        valor = input("Novo projeto: ").strip()
        projetos = carregar_json("data/projeto.json", tipo="dict")
        if valor not in projetos:
            print(f"Projeto '{valor}' não encontrado.")
            return
    elif campo == "responsavel":
        valor = input("Novo responsável: ").strip()
        usuarios_data = carregar_json("data/usuarios.json", tipo="dict")
        usuarios = usuarios_data.get("usuarios", [])
        if not any(u["Nome"] == valor for u in usuarios):
            print(f"Usuário '{valor}' não encontrado.")
            return
    elif campo == "prazo":
        valor = ler_data("Novo prazo (DD/MM/YYYY): ")
    else:
        valor = input(f"Novo valor para {campo}: ").strip()

    tarefa[campo] = valor
    salvar_json("data/tarefas.json", tarefas)
    print("Tarefa atualizada com sucesso!")

def concluir_tarefa():
    listar_tarefas()
    tarefas = carregar_json("data/tarefas.json", tipo="lista")
    try:
        idx = int(input("Índice da tarefa para concluir: "))
        tarefas[idx]["status"] = "concluída"
    except (ValueError, IndexError):
        print("Índice inválido.")
        return
    salvar_json("data/tarefas.json", tarefas)
    print("Tarefa concluída.")

def remover_tarefa():
    listar_tarefas()
    tarefas = carregar_json("data/tarefas.json", tipo="lista")
    try:
        idx = int(input("Índice da tarefa para remover: "))
        tarefas.pop(idx)
    except (ValueError, IndexError):
        print("Índice inválido.")
        return
    salvar_json("data/tarefas.json", tarefas)
    print("Tarefa removida.")

# ---------- MENU PRINCIPAL ----------

while True:
    print("\n===== MENU DE TAREFAS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Concluir tarefa")
    print("5 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        cadastrar_tarefa()
    elif opcao == "2":
        filtro = input("Filtrar por (todas/projeto/responsavel/status): ").strip().lower()
        if filtro == "todas":
            listar_tarefas()
        elif filtro in ["projeto", "responsavel", "status"]:
            valor = input(f"Digite o nome de {filtro}: ").strip()
            listar_tarefas(filtro, valor)
        else:
            print("Filtro inválido.")
    elif opcao == "3":
        atualizar_tarefa()
    elif opcao == "4":
        concluir_tarefa()
    elif opcao == "5":
        remover_tarefa()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
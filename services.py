# services.py
from storage import load_list, save_list
from models import novo_usuario, novo_projeto, nova_tarefa
from utils import validar_status, parse_date_str
from typing import List, Dict

USERS = "usuarios.json"
PROJ = "projeto.json"
TASKS = "tarefas.json"

# ---------- Usuários ----------
def listar_usuarios() -> List[Dict]:
    return load_list(USERS)

def cadastrar_usuario(nome: str, email: str, perfil: str) -> None:
    usuarios = load_list(USERS)
    if any(u.get("Email","").lower() == email.lower() for u in usuarios):
        raise ValueError("E-mail já cadastrado.")
    u = novo_usuario(nome, email, perfil)
    usuarios.append(u)
    save_list(USERS, usuarios)

def buscar_usuarios(termo: str) -> List[Dict]:
    t = termo.strip().lower()
    return [u for u in load_list(USERS) if t in u.get("Nome","").lower() or t in u.get("Email","").lower()]

def atualizar_usuario(email_ref: str, campo: str, valor: str) -> bool:
    usuarios = load_list(USERS)
    updated = False
    for u in usuarios:
        if u.get("Email","").lower() == email_ref.lower():
            if campo == "Email" and any(x.get("Email","").lower() == valor.lower() for x in usuarios):
                raise ValueError("Novo e-mail já cadastrado.")
            u[campo] = valor
            updated = True
            break
    if updated:
        save_list(USERS, usuarios)
    return updated

def remover_usuario(email: str) -> bool:
    usuarios = load_list(USERS)
    novas = [u for u in usuarios if u.get("Email","").lower() != email.lower()]
    if len(novas) == len(usuarios):
        return False
    save_list(USERS, novas)
    return True

def remover_todos_usuarios() -> None:
    save_list(USERS, [])

# ---------- Projetos ----------
def listar_projetos() -> List[Dict]:
    return load_list(PROJ)

def cadastrar_projeto(nome: str, descricao: str, data_inicio: str, data_fim: str) -> None:
    projetos = load_list(PROJ)
    if any(p.get("nome","").lower() == nome.lower() for p in projetos):
        raise ValueError("Projeto com esse nome já existe.")
    p = novo_projeto(nome, descricao, data_inicio, data_fim)
    projetos.append(p)
    save_list(PROJ, projetos)

def buscar_projeto(nome: str) -> List[Dict]:
    n = nome.strip().lower()
    return [p for p in load_list(PROJ) if n == p.get("nome","").lower()]

def atualizar_projeto(nome_ref: str, campo: str, valor: str) -> bool:
    projetos = load_list(PROJ)
    updated = False
    for p in projetos:
        if p.get("nome","").lower() == nome_ref.lower():
            if campo == "nome" and any(x.get("nome","").lower() == valor.lower() for x in projetos):
                raise ValueError("Nome de projeto já existe.")
            # if updating dates, validate
            if campo in ("data_inicio","data_fim"):
                if not parse_date_str(valor):
                    raise ValueError("Data inválida. Use DD/MM/AAAA.")
            p[campo] = valor
            updated = True
            break
    if updated:
        save_list(PROJ, projetos)
    return updated

def remover_projeto(nome: str) -> bool:
    projetos = load_list(PROJ)
    novas = [p for p in projetos if p.get("nome","").lower() != nome.lower()]
    if len(novas) == len(projetos):
        return False
    save_list(PROJ, novas)
    return True

def remover_todos_projetos() -> None:
    save_list(PROJ, [])

# ---------- Tarefas ----------
def listar_tarefas() -> List[Dict]:
    return load_list(TASKS)

def cadastrar_tarefa(titulo: str, projeto: str, responsavel: str, status: str, prazo: str) -> None:
    projetos = load_list(PROJ)
    usuarios = load_list(USERS)
    if not any(p.get("nome","").lower() == projeto.lower() for p in projetos):
        raise ValueError("Projeto não encontrado.")
    if not any(u.get("Nome","").lower() == responsavel.lower() for u in usuarios):
        raise ValueError("Responsável não encontrado.")
    if validar_status(status) is None:
        raise ValueError("Status inválido.")
    if parse_date_str(prazo) is None:
        raise ValueError("Prazo inválido.")
    tarefas = load_list(TASKS)
    tarefas.append(nova_tarefa(titulo, projeto, responsavel, status, prazo))
    save_list(TASKS, tarefas)

def buscar_tarefas_por_projeto(projeto: str):
    return [t for t in load_list(TASKS) if t.get("projeto","").lower() == projeto.lower()]

def buscar_tarefas_por_responsavel(resp: str):
    return [t for t in load_list(TASKS) if t.get("responsavel","").lower() == resp.lower()]

def buscar_tarefas_por_status(status: str):
    st = validar_status(status)
    if st is None:
        return []
    return [t for t in load_list(TASKS) if t.get("status","").lower() == st]

def atualizar_tarefa(titulo_ref: str, campo: str, valor: str) -> bool:
    tarefas = load_list(TASKS)
    updated = False
    for t in tarefas:
        if t.get("titulo","").lower() == titulo_ref.lower():
            if campo == "status" and validar_status(valor) is None:
                raise ValueError("Status inválido.")
            if campo == "projeto":
                if not any(p.get("nome","").lower() == valor.lower() for p in load_list(PROJ)):
                    raise ValueError("Projeto inválido.")
            if campo == "responsavel":
                if not any(u.get("Nome","").lower() == valor.lower() for u in load_list(USERS)):
                    raise ValueError("Responsável inválido.")
            if campo == "prazo" and parse_date_str(valor) is None:
                raise ValueError("Prazo inválido.")
            t[campo] = valor
            updated = True
            break
    if updated:
        save_list(TASKS, tarefas)
    return updated

def concluir_tarefa(titulo_ref: str) -> bool:
    return atualizar_tarefa(titulo_ref, "status", "concluída")

def reabrir_tarefa(titulo_ref: str) -> bool:
    return atualizar_tarefa(titulo_ref, "status", "pendente")

def remover_tarefa(titulo_ref: str) -> bool:
    tarefas = load_list(TASKS)
    novas = [t for t in tarefas if t.get("titulo","").lower() != titulo_ref.lower()]
    if len(novas) == len(tarefas):
        return False
    save_list(TASKS, novas)
    return True

def remover_todas_tarefas() -> None:
    save_list(TASKS, [])

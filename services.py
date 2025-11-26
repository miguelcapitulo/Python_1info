from storage import load_list, save_list
from models import criar_usuario, criar_projeto, criar_tarefa
from datetime import datetime

USERS_FILE = "usuarios.json"
PROJECTS_FILE = "projeto.json"
TASKS_FILE = "tarefas.json"

VALID_STATUS = ("pendente", "andamento", "concluída")

#USUÁRIOS
def listar_usuarios():
    return load_list(USERS_FILE)

def cadastrar_usuario(nome, email, perfil):
    usuarios = listar_usuarios()
    if any(u.get("Email", "").lower() == email.lower() for u in usuarios):
        raise ValueError("O email informado já está cadastrado.")
    u = criar_usuario(nome, email, perfil)
    usuarios.append(u)
    save_list(USERS_FILE, usuarios)
    return u

def buscar_usuarios(term):
    term = (term or "").strip().lower()
    if not term:
        return listar_usuarios()
    return [
        u for u in listar_usuarios()
        if term in u.get("Nome", "").lower() or term in u.get("Email", "").lower()
    ]

def atualizar_usuario(email, campo, valor):
    usuarios = listar_usuarios()
    for u in usuarios:
        if u.get("Email", "").lower() == email.lower():
            u[campo] = valor
            save_list(USERS_FILE, usuarios)
            return True
    return False

def remover_usuario(email):
    usuarios = listar_usuarios()
    nova = [u for u in usuarios if u.get("Email", "").lower() != email.lower()]
    if len(nova) < len(usuarios):
        save_list(USERS_FILE, nova)
        return True
    return False

def remover_todos_usuarios():
    save_list(USERS_FILE, [])


#PROJETOS
def listar_projetos():
    return load_list(PROJECTS_FILE)

def cadastrar_projeto(nome, descricao, ini, fim):
    projetos = listar_projetos()
    if any(p.get("nome", "").lower() == nome.lower() for p in projetos):
        raise ValueError("Já existe um projeto com esse nome.")
    try:
        d_ini = datetime.strptime(ini, "%d/%m/%Y").date()
        d_fim = datetime.strptime(fim, "%d/%m/%Y").date()
    except Exception:
        raise ValueError("Datas inválidas. Use DD/MM/AAAA.")
    if d_fim < d_ini:
        raise ValueError("Data final não pode ser anterior à data de início.")
    p = criar_projeto(nome, descricao, ini, fim)
    projetos.append(p)
    save_list(PROJECTS_FILE, projetos)
    return p

def buscar_projeto(term):
    term = (term or "").strip().lower()
    if not term:
        return listar_projetos()
    return [p for p in listar_projetos() if term in p.get("nome", "").lower()]

def atualizar_projeto(nome, campo, valor):
    projetos = listar_projetos()
    for p in projetos:
        if p.get("nome", "").lower() == nome.lower():
            p[campo] = valor
            save_list(PROJECTS_FILE, projetos)
            return True
    return False

def remover_projeto(nome):
    projetos = listar_projetos()
    nova = [p for p in projetos if p.get("nome", "").lower() != nome.lower()]
    if len(nova) < len(projetos):
        save_list(PROJECTS_FILE, nova)
        return True
    return False

def remover_todos_projetos():
    save_list(PROJECTS_FILE, [])


#TAREFAS
def listar_tarefas():
    return load_list(TASKS_FILE)

def _normalize_status(status):
    if not status:
        return None
    s = status.strip().lower()
    if s in VALID_STATUS:
        return s
    return None

def cadastrar_tarefa(titulo, projeto, responsavel, status, prazo):
    if not any(p.get("nome", "").lower() == projeto.lower() for p in listar_projetos()):
        raise ValueError("O projeto informado não existe.")
    if not any(u.get("Nome", "").lower() == responsavel.lower() for u in listar_usuarios()):
        raise ValueError("O responsável informado não existe.")
    status_norm = _normalize_status(status)
    if not status_norm:
        raise ValueError("Status inválido. Use: pendente, andamento ou concluída.")
    try:
        datetime.strptime(prazo, "%d/%m/%Y")
    except Exception:
        raise ValueError("Prazo com formato inválido. Use DD/MM/AAAA.")
    t = criar_tarefa(titulo, projeto, responsavel, status_norm, prazo)
    tarefas = listar_tarefas()
    tarefas.append(t)
    save_list(TASKS_FILE, tarefas)
    return t

def buscar_tarefas_por_projeto(term):
    term = (term or "").strip().lower()
    if not term:
        return listar_tarefas()
    return [t for t in listar_tarefas() if term in t.get("projeto", "").lower()]

def buscar_tarefas_por_responsavel(term):
    term = (term or "").strip().lower()
    if not term:
        return listar_tarefas()
    return [t for t in listar_tarefas() if term in t.get("responsavel", "").lower()]

def buscar_tarefas_por_status(term):
    term = (term or "").strip().lower()
    if not term:
        return listar_tarefas()
    return [t for t in listar_tarefas() if term == t.get("status", "").lower()]

def atualizar_tarefa(titulo, campo, valor):
    tarefas = listar_tarefas()
    for t in tarefas:
        if t.get("titulo", "").lower() == titulo.lower():
            if campo.lower() == "status":
                status_norm = _normalize_status(valor)
                if not status_norm:
                    raise ValueError("Status inválido. Use: pendente, andamento ou concluída.")
                t["status"] = status_norm
            elif campo.lower() == "prazo":
                try:
                    datetime.strptime(valor, "%d/%m/%Y")
                except Exception:
                    raise ValueError("Prazo com formato inválido. Use DD/MM/AAAA.")
                t["prazo"] = valor
            else:
                t[campo] = valor
            save_list(TASKS_FILE, tarefas)
            return True
    return False

def concluir_tarefa(titulo):
    return atualizar_tarefa(titulo, "status", "concluída")

def reabrir_tarefa(titulo):
    return atualizar_tarefa(titulo, "status", "pendente")

def remover_tarefa(titulo):
    tarefas = listar_tarefas()
    nova = [t for t in tarefas if t.get("titulo", "").lower() != titulo.lower()]
    if len(nova) < len(tarefas):
        save_list(TASKS_FILE, nova)
        return True
    return False

def remover_todas_tarefas():
    save_list(TASKS_FILE, [])


#RELATÓRIOS
def tarefas_atrasadas():
    hoje = datetime.now().date()
    atrasadas = []
    for t in listar_tarefas():
        prazo_str = t.get("prazo", "")
        status = t.get("status", "").strip().lower()
        try:
            prazo = datetime.strptime(prazo_str, "%d/%m/%Y").date()
        except Exception:
            continue
        if prazo < hoje and status in ("pendente", "andamento"):
            atrasadas.append(t)
    return atrasadas

def report_summary_by_project():
    projetos = listar_projetos()
    tarefas = listar_tarefas()
    relatorio = []
    for p in projetos:
        nome = p.get("nome")
        tarefas_proj = [t for t in tarefas if (t.get("projeto") or "").lower() == (nome or "").lower()]
        total = len(tarefas_proj)
        por_status = {}
        for t in tarefas_proj:
            s = t.get("status", "N/A")
            por_status[s] = por_status.get(s, 0) + 1
        pct_concluidas = (por_status.get("concluída", 0) / total * 100) if total > 0 else 0
        relatorio.append({
            "projeto": nome,
            "total": total,
            "por_status": por_status,
            "pct_concluidas": pct_concluidas
        })
    return relatorio

def productivity_by_user(inicio, fim):
    try:
        d_ini = datetime.strptime(inicio, "%d/%m/%Y").date()
        d_fim = datetime.strptime(fim, "%d/%m/%Y").date()
    except Exception:
        raise ValueError("Datas inválidas. Use DD/MM/AAAA.")
    produtividades = {}
    for t in listar_tarefas():
        if (t.get("status", "").lower() == "concluída"):
            try:
                prazo = datetime.strptime(t.get("prazo", ""), "%d/%m/%Y").date()
            except Exception:
                continue
            if d_ini <= prazo <= d_fim:
                resp = t.get("responsavel")
                produtividades[resp] = produtividades.get(resp, 0) + 1
    return produtividades

def overdue_tasks():
    return tarefas_atrasadas()
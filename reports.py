from services import listar_projetos, listar_tarefas
from datetime import datetime

def resumo_por_projeto():
    projetos = listar_projetos()
    tarefas = listar_tarefas()
    if not projetos:
        return {}
    resumo = {}
    for p in projetos:
        nome = p.get("nome")
        tproj = [t for t in tarefas if t.get("projeto","").lower() == nome.lower()]
        total = len(tproj)
        pend = sum(1 for t in tproj if t.get("status") == "pendente")
        andam = sum(1 for t in tproj if t.get("status") == "andamento")
        conc = sum(1 for t in tproj if t.get("status") == "concluída")
        pct = round((conc / total * 100), 1) if total else 0.0
        resumo[nome] = {"total_tarefas": total, "pendente": pend, "andamento": andam, "concluída": conc, "percentual_conclusão": pct}
    return resumo

def produtividade_por_usuario(data_ini=None, data_fim=None):
    tarefas = listar_tarefas()
    res = {}
    fmt = "%d/%m/%Y"
    if data_ini:
        di = datetime.strptime(data_ini, fmt)
    else:
        di = None
    if data_fim:
        df = datetime.strptime(data_fim, fmt)
    else:
        df = None
    for t in tarefas:
        if t.get("status") != "concluída":
            continue
        prazo = datetime.strptime(t.get("prazo"), fmt)
        if di and prazo < di: continue
        if df and prazo > df: continue
        nome = t.get("responsavel")
        res[nome] = res.get(nome, 0) + 1
    return res

def tarefas_atrasadas():
    hoje = datetime.today()
    tarefas = listar_tarefas()
    atrasadas = []
    for t in tarefas:
        if t.get("status") == "concluída":
            continue
        try:
            prazo = datetime.strptime(t.get("prazo"), "%d/%m/%Y")
            if prazo < hoje:
                atrasadas.append(t)
        except Exception:
            continue
    return atrasadas
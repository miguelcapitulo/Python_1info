# reports.py
from services import listar_tarefas, listar_projetos, listar_usuarios
from datetime import datetime
from typing import Dict

def resumo_geral() -> Dict[str,int]:
    return {
        "usuarios": len(listar_usuarios()),
        "projetos": len(listar_projetos()),
        "tarefas": len(listar_tarefas())
    }

def tarefas_por_status() -> Dict[str,int]:
    from services import buscar_tarefas_por_status
    d = {}
    for s in ("pendente","andamento","concluída"):
        d[s] = len(buscar_tarefas_por_status(s))
    return d

def tarefas_vencidas_ate(data_str: str):
    """Retorna tarefas com prazo <= data_str (DD/MM/YYYY)."""
    try:
        limite = datetime.strptime(data_str, "%d/%m/%Y")
    except Exception:
        return []
    out = []
    for t in listar_tarefas():
        try:
            p = datetime.strptime(t.get("prazo","01/01/1900"), "%d/%m/%Y")
            if p <= limite:
                out.append(t)
        except Exception:
            continue
    return out

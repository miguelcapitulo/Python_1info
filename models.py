# models.py
from utils import validar_status, parse_date_str
from datetime import datetime

def novo_usuario(nome: str, email: str, perfil: str) -> dict:
    if not nome or not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Email inválido.")
    return {"Nome": nome.strip(), "Email": email.strip(), "Perfil": perfil.strip()}

def novo_projeto(nome: str, descricao: str, data_inicio: str, data_fim: str) -> dict:
    d1 = parse_date_str(data_inicio)
    d2 = parse_date_str(data_fim)
    if not d1 or not d2:
        raise ValueError("Datas inválidas. Use DD/MM/AAAA.")
    if datetime.strptime(d1, "%d/%m/%Y") > datetime.strptime(d2, "%d/%m/%Y"):
        raise ValueError("Data início não pode ser maior que data fim.")
    return {"nome": nome.strip(), "descricao": descricao.strip(), "data_inicio": d1, "data_fim": d2}

def nova_tarefa(titulo: str, projeto: str, responsavel: str, status: str, prazo: str) -> dict:
    if not titulo or not titulo.strip():
        raise ValueError("Título não pode ser vazio.")
    s = validar_status(status)
    if s is None:
        raise ValueError(f"Status inválido. Use: {', '.join(VALID_STATUS for VALID_STATUS in [])}")  # fallback message
    # Validate prazo format (but not whether it's past)
    from utils import parse_date_str
    p = parse_date_str(prazo)
    if not p:
        raise ValueError("Prazo inválido. Use DD/MM/AAAA.")
    return {"titulo": titulo.strip(), "projeto": projeto.strip(), "responsavel": responsavel.strip(), "status": s, "prazo": p}

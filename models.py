from datetime import datetime
from utils import VALID_STATUS

def criar_usuario(nome, email, perfil):
    if not nome or len(nome.strip()) < 1:
        raise ValueError("Nome inválido")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Email inválido")
    return {"Nome": nome.strip(), "Email": email.strip(), "Perfil": perfil.strip()}

def criar_projeto(nome, descricao, data_inicio, data_fim):
    d1 = datetime.strptime(data_inicio, "%d/%m/%Y")
    d2 = datetime.strptime(data_fim, "%d/%m/%Y")
    if d2 < d1:
        raise ValueError("Data fim menor que início")
    return {"nome": nome.strip(), "descricao": descricao.strip(),
            "data_inicio": data_inicio, "data_fim": data_fim}

def criar_tarefa(titulo, projeto, responsavel, status, prazo):
    if status.lower() not in VALID_STATUS:
        raise ValueError("Status inválido")
    try:
        from datetime import datetime as _dt
        _dt.strptime(prazo, "%d/%m/%Y")
    except Exception:
        raise ValueError("Prazo inválido")
    return {"titulo": titulo.strip(), "projeto": projeto.strip(),
            "responsavel": responsavel.strip(), "status": status.lower(), "prazo": prazo}
# utils.py
from datetime import datetime
from typing import Optional

VALID_STATUS = ("pendente", "andamento", "concluída")

def validar_status(s: str) -> Optional[str]:
    if not isinstance(s, str):
        return None
    s = s.strip().lower()
    return s if s in VALID_STATUS else None

def parse_date_str(s: str) -> Optional[str]:
    """Recebe 'DD/MM/YYYY' e retorna a mesma string validada (ou None)."""
    try:
        dt = datetime.strptime(s.strip(), "%d/%m/%Y")
        return dt.strftime("%d/%m/%Y")
    except Exception:
        return None

def pedir_data(msg: str) -> str:
    while True:
        s = input(msg).strip()
        v = parse_date_str(s)
        if v:
            return v
        print("Formato inválido. Use DD/MM/AAAA.")

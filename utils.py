from datetime import datetime

VALID_STATUS = ("pendente", "andamento", "concluída")

def pedir_data(msg):
    while True:
        s = input(f"{msg} ").strip()
        try:
            datetime.strptime(s, "%d/%m/%Y")
            return s
        except ValueError:
            print("Formato inválido! Use exatamente DD/MM/AAAA.")

def validar_status(s):
    if not s:
        return None
    status_corrigido = s.lower().strip()
    return status_corrigido if status_corrigido in VALID_STATUS else None
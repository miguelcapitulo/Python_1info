from datetime import datetime

VALID_STATUS = ("pendente", "andamento", "concluída")

def pedir_data(msg):
    while True:
        s = input(f"{msg} ").strip()
        try:
            datetime.strptime(s, "%d/%m/%Y")
            return s
        except ValueError:
            print("Formato inválido! Digite no formato DD/MM/AAAA.")


def validar_status(s):
    return s.lower().strip() in VALID_STATUS if s else False

from datetime import datetime

VALID_STATUS = ("pendente", "andamento", "concluída")

def pedir_data(msg):
    while True:
        s = input(msg).strip()
        if s == "":
            return ""
        try:
            datetime.strptime(s, "%d/%m/%Y")
            return s
        except ValueError:
            print("Formato inválido. Use DD/MM/AAAA")

def validar_status(s):
    return s and s.lower() in VALID_STATUS

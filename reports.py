
while True:
    nome = input("Digite o nome do projeto: ").strip()

    if len(nome) < 3:
        print("O nome deve ter pelo menos 3 caracteres!")
    
    else:
        break
    descriçao=input("Digite a descrição do projeto (deixe vazio para finalizar):")
linhas = []
while True:
    linha = input()
    if linha.strip() == "":
        break
    linhas.append(linha)

descricao = "\n".join(linhas)

from datetime import datetime

def ler_data(mensagem):
    while True:
        data_str = input(mensagem)
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida! Use o formato DD/MM/AAAA.\n")

data_inicio = ler_data("Digite a data de início (DD/MM/AAAA): ")
data_fim = ler_data("Digite a data de fim (DD/MM/AAAA): ")

print("Data de início:", data_inicio)
print("Data de fim:   ", data_fim)
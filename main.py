
while True:
    try:
        nome=input("insira o seu nome: ")
        break
    except ValueError:
        print("Entrada inválida! Por favor, insira o seu nome.")
while True:
    email = input("Insira o seu email: ")

    if email.count("@")!=1:
        print("Invalido,Tente Novamente")
        continue
        
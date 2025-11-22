
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
    
    usuario,dominio=email.split("@")

    if not usuario:
        print("Email inválido! Deve haver algo antes do '@'.")
        continue
    if not dominio:
        print("Email inválido! Deve haver algo após o '@'.")
        continue
    if "." not in dominio or dominio.startswith(".") or dominio.endswith("."):
        print("Email inválido! O domínio deve conter um ponto válido.")
        continue

    break

print("Email válido!")
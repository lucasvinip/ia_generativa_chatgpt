tentativa = 3
senha = input("Digite sua senha: ")

while tentativa != 0:
    if senha == "123456":
        print("Seja bem-vindo")
        break
    else:
        print("Tente novamente")
    tentativa -= 1
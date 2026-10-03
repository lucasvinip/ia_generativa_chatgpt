# Concatenação simples de variáveis de texto
nome = "Maria"
sobrenome = " da Silva"
nome_completo = nome + sobrenome

print("Nome completo: ", nome_completo)

# Concatenação combinando texto com números
idade = 22
mensagem = "Olá meu nome é " + nome_completo + " e eu tenho " + str(idade) + " anos"
print(mensagem)

# Numeros inseridos pelo usúario 
inputUser = input
nota_1 = float(inputUser("Digite a primeira nota: "))
nota_2 = float(inputUser("Digite a segunda nota: "))
nota_3 = float(inputUser("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3
print("A média das notas é: ", media)

# arredondamento de casas decimais
print(f"A média das notas é: {media:.2f}")
print(f"A média das notas é: {round(media, 2)}")
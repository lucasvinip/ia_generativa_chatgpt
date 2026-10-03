# Operador AND (E) -  Retorna True apenas se TODAS as condições forem verdadeiras
tem_sol = True
tem_dinheiro = True
vai_praia = tem_sol and tem_dinheiro

print("Vai a praia (AND):", vai_praia)

# Retorna OR (OU) - Retorna True se pelo menos uma condição for verdadeira
tem_carro = True
tem_bicecleta = True
pode_viajar = tem_carro or tem_dinheiro
print("Pode viajar (OR):", pode_viajar)

# Retorna NOT (NÃO) - Inverte o valor lógico
chovendo = False
fazer_caminhada = not chovendo
print("Fazer caminhada (NOT): ", fazer_caminhada)

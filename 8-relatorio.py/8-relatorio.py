# O modo W cria o arquivo "relatorio.txt" na pasta raíz do projeto

# with open ("8-relatorio.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.write("Primeira linha: atenção a primeira linha foi escrita\n")
#     arquivo.write("Segunda linha: atenção a segunda linha foi escrita")

with open ("8-relatorio.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\nPrimeira linha: atenção a primeira linha foi escrita\n")
    arquivo.write("\nSegunda linha: atenção a segunda linha foi escrita")
import csv

dados_tabela = [
    ["Nome", "Cargo", "Idade"],
    ["Carlos", "Desenvolvedor", 28],
    ["Ana", "Recrutadora", 26],
    ["Lucas Oliveira", "Estágiario", 22],
]

with open("8.2-funcionarios.csv", "w", encoding="utf-8", newline="") as arquivo_csv:
    escrever = csv.writer(arquivo_csv)
    escrever.writerows(dados_tabela)
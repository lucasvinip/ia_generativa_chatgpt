# Lista de arquivos encontrados no diretório
arquivos_enviados = ["manual.pdf", "foto.png", "contrato.PDF", "virus.exe", "relatorio.pdf", "anotacoes.txt"]

pdfs_validos = []

for arquivo_enviado in arquivos_enviados:
    if arquivo_enviado.lower().endswith(".pdf"):
        pdfs_validos.append(arquivo_enviado)

print("Lista completa...")
print("Arquivos de pdf: ", pdfs_validos)

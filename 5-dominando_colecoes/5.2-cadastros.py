cadastros = [
        {
            "id": 1024,
            "perfil":{
                "nome": "Beatriz Souza",
                "email": "beatrizsouza@gmail.com"
            }
        },
        {
                "id": 1060,
                "perfil": {
                    "nome": "Carlos Silva",
                    "email": "carlosilva@gmail.com"
                }
        }
]

for item in cadastros:
    id_formulario = item.get("id")
    perfil_extraido = item.get("perfil")
    nome_extraido = perfil_extraido.get("nome")
    telefone_usuario = perfil_extraido.get("telefone")

    print(f"ID: {id_formulario} | Usuário: {nome_extraido} | Telefone: {telefone_usuario}")


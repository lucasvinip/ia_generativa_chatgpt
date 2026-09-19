employers = {
    101: {
        "nome": "Carlos",
        "cargo": "desenvolvedor",
        "habilidades": ["Python", "Java", "C##"]
    },
    102: {
            "nome": "Mario",
            "cargo": "Gerente de Projetos",
            "habilidades": ["Scrum", "Kanban", "Gestão"]
    },
}

# print(employers[102]["habilidades"][0])
print(employers.get(103,{}).get("nome"))
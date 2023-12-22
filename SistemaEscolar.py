import random

alunos = {}
professores = {}

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    senha = input("Digite a senha: ")
    aluno_id = len(alunos) + 1
    notas_aleatorias = {'1º Bimestre': round(random.uniform(0, 10), 2),
                        '2º Bimestre': round(random.uniform(0, 10), 2),
                        '3º Bimestre': round(random.uniform(0, 10), 2)}
    alunos[aluno_id] = {'nome': nome, 'senha': senha, 'notas': notas_aleatorias}
    print(f"Aluno(a) {nome} cadastrado com ID {aluno_id} *GUARDE ESTE ID* e notas:")
    for bimestre, nota in notas_aleatorias.items():
        print(f"{bimestre}: {nota:.2f}")

def cadastrar_prof():
    nome = input("Digite o nome do professor(a): ")
    senha = input("Digite a senha: ")
    professor_id = len(professores) + 1
    professores[professor_id] = {'nome': nome, 'senha': senha}
    print(f"Professor {nome} cadastrado com ID {professor_id} *GUARDE ESTE ID* ")

def login():
    tipo_de_usuario = input("Digite 'A' para aluno ou 'P' para professor: ")

    if tipo_de_usuario.upper() == 'A':
        aluno_id = int(input("Digite o ID do aluno: "))
        senha = input("Digite a senha: ")

        if aluno_id in alunos and alunos[aluno_id]['senha'] == senha:
            print(f"Bem-vindo, {alunos[aluno_id]['nome']}!")
            return aluno_id, 'aluno'
        else:
            print("Login inválido.")
            return None, None

    elif tipo_de_usuario.upper() == 'P':
        try:
            professor_id = int(input("Digite o ID do professor: "))
        except ValueError:
            print("ID do professor deve ser um número inteiro.")
            return None, None

        senha = input("Digite a senha: ")

        if professor_id in professores and professores[professor_id]['senha'] == senha:
            print(f"Bem-vindo, Professor {professores[professor_id]['nome']}!")
            return professor_id, 'professor'
        else:
            print("Login inválido.")
            return None, None

    else:
        print("Opção inválida.")
        return None, None

def painel_prof():
    while True:
        print("\n--- Painel do Professor ---")
        print("1. Visualizar Notas dos Alunos")
        print("2. Alterar Notas dos Alunos")
        print("3. Sair")

        options = input("Escolha uma opção (1/2/3): ")

        if options == '1':
            visualizar_notas()
        elif options == '2':
            alterar_notas_alunos()
        elif options == '3':
            print("Saindo do painel do professor...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def visualizar_notas():
    print("\n--- Notas dos Alunos ---")
    for aluno_id, aluno_info in alunos.items():
        print(f"\nAluno ID {aluno_id}: {aluno_info['nome']}")
        if isinstance(aluno_info['notas'], list):
            print("Notas: N/A (Formato antigo)")
        else:
            for bimestre, nota in aluno_info['notas'].items():
                print(f"{bimestre}: {nota:.2f}")
            media = calcular_media(aluno_info['notas'])
            print(f"Média: {media:.2f}")
        print("-" * 20)

def alterar_notas_alunos():
    aluno_id = int(input("Digite o ID do aluno: "))
    
    if aluno_id in alunos:
        novas_notas = input("Digite as novas notas (separadas por vírgula): ").split(',')
        alunos[aluno_id]['notas'] = {'1º Bimestre': float(novas_notas[0]),
                                      '2º Bimestre': float(novas_notas[1]),
                                      '3º Bimestre': float(novas_notas[2])}
        print(f"Notas do Aluno ID {aluno_id} alteradas para: {alunos[aluno_id]['notas']}")
    else:
        print("Não foi possível encontrar o aluno.")

def calcular_media(notas):
    return sum(notas.values()) / len(notas)

def visualizar_notas_aluno(aluno_id): 
    print("\n--- Suas Notas ---")
    aluno_info = alunos.get(aluno_id)
    if aluno_info:
        for bimestre, nota in aluno_info['notas'].items():
            print(f"{bimestre}: {nota:.2f}")
        media = calcular_media(aluno_info['notas'])
        print(f"Média: {media:.2f}")
    else:
        print("Não foi possível encontrar o aluno.")


def painel_principal():
    while True:
        print("\n--- Painel Escolar ---")
        print("1. Cadastrar Aluno(a)")
        print("2. Cadastrar Professor(a)")
        print("3. Fazer Login")
        print("4. Sair")

        options = input("Escolha uma opção (1/2/3/4): ")

        if options == '1':
            cadastrar_aluno()
        elif options == '2':
            cadastrar_prof()
        elif options == '3':
            usuario_id, tipo_de_usuario = login()
            if usuario_id is not None:
                if tipo_de_usuario == 'professor':
                    painel_prof()
                elif tipo_de_usuario == 'aluno':
                    visualizar_notas_aluno(usuario_id)
        elif options == '4':
            print("Saindo do painel...")
            break
        else:
            print("Opção inválida. Tente novamente.")

painel_principal()

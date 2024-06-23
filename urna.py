import random

# Função para gerar nomes aleatórios
def gerar_nome(tipo):
    primeiro_nome = ("João", "Maria", "José", "Ana", "Carlos", "Paula", "Pedro", "Mariana", "Lucas", "Fernanda")
    sobrenome = ("Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues", "Almeida", "Nascimento", "Lima", "Souza")
    return f"{random.choice(primeiro_nome)} {random.choice(sobrenome)} - {tipo}"

# Gerar candidatos a prefeito e vereador
prefeito_1 = gerar_nome("Prefeito")
prefeito_2 = gerar_nome("Prefeito")
prefeito_3 = gerar_nome("Prefeito")
prefeito_4 = gerar_nome("Prefeito")

vereador_1 = gerar_nome("Vereador")
vereador_2 = gerar_nome("Vereador")
vereador_3 = gerar_nome("Vereador")
vereador_4 = gerar_nome("Vereador")
vereador_5 = gerar_nome("Vereador")
vereador_6 = gerar_nome("Vereador")
vereador_7 = gerar_nome("Vereador")
vereador_8 = gerar_nome("Vereador")
vereador_9 = gerar_nome("Vereador")
vereador_10 = gerar_nome("Vereador")

# Inicializar contadores de votos para prefeitos e vereadores
votos_prefeito_1 = 0
votos_prefeito_2 = 0
votos_prefeito_3 = 0
votos_prefeito_4 = 0

votos_vereador_1 = 0
votos_vereador_2 = 0
votos_vereador_3 = 0
votos_vereador_4 = 0
votos_vereador_5 = 0
votos_vereador_6 = 0
votos_vereador_7 = 0
votos_vereador_8 = 0
votos_vereador_9 = 0
votos_vereador_10 = 0

votos_nulo = 0
votos_branco = 0

# Mesário abre a urna
urna_aberta = True
print("\nUrna aberta para votação.\n")

# Número de eleitores
num_eleitores = 40
eleitor_atual = 1

while urna_aberta and eleitor_atual <= num_eleitores:
    print(f"\n===== Eleitor {eleitor_atual} =====\n")
    
    # Eleitor vota para prefeito
    voto_valido = False
    while not voto_valido:
        print("Candidatos a Prefeito:")
        print(f"1. {prefeito_1}")
        print(f"2. {prefeito_2}")
        print(f"3. {prefeito_3}")
        print(f"4. {prefeito_4}")
        
        voto_prefeito = input("\nVote para Prefeito (1-4, N para Nulo, B para Branco): ")
        if voto_prefeito == '1':
            votos_prefeito_1 += 1
            voto_valido = True
        elif voto_prefeito == '2':
            votos_prefeito_2 += 1
            voto_valido = True
        elif voto_prefeito == '3':
            votos_prefeito_3 += 1
            voto_valido = True
        elif voto_prefeito == '4':
            votos_prefeito_4 += 1
            voto_valido = True
        elif voto_prefeito.upper() == 'N':
            votos_nulo += 1
            voto_valido = True
        elif voto_prefeito.upper() == 'B':
            votos_branco += 1
            voto_valido = True
        else:
            print("\nVoto inválido para Prefeito. Tente novamente.\n")
    
    # Eleitor vota para vereador
    voto_valido = False
    while not voto_valido:
        print("\nCandidatos a Vereador:")
        print(f"1. {vereador_1}")
        print(f"2. {vereador_2}")
        print(f"3. {vereador_3}")
        print(f"4. {vereador_4}")
        print(f"5. {vereador_5}")
        print(f"6. {vereador_6}")
        print(f"7. {vereador_7}")
        print(f"8. {vereador_8}")
        print(f"9. {vereador_9}")
        print(f"10. {vereador_10}")
        
        voto_vereador = input("\nVote para Vereador (1-10, N para Nulo, B para Branco): ")
        if voto_vereador == '1':
            votos_vereador_1 += 1
            voto_valido = True
        elif voto_vereador == '2':
            votos_vereador_2 += 1
            voto_valido = True
        elif voto_vereador == '3':
            votos_vereador_3 += 1
            voto_valido = True
        elif voto_vereador == '4':
            votos_vereador_4 += 1
            voto_valido = True
        elif voto_vereador == '5':
            votos_vereador_5 += 1
            voto_valido = True
        elif voto_vereador == '6':
            votos_vereador_6 += 1
            voto_valido = True
        elif voto_vereador == '7':
            votos_vereador_7 += 1
            voto_valido = True
        elif voto_vereador == '8':
            votos_vereador_8 += 1
            voto_valido = True
        elif voto_vereador == '9':
            votos_vereador_9 += 1
            voto_valido = True
        elif voto_vereador == '10':
            votos_vereador_10 += 1
            voto_valido = True
        elif voto_vereador.upper() == 'N':
            votos_nulo += 1
            voto_valido = True
        elif voto_vereador.upper() == 'B':
            votos_branco += 1
            voto_valido = True
        else:
            print("\nVoto inválido para Vereador. Tente novamente.\n")

    # Passar para o próximo eleitor
    eleitor_atual += 1

# Mesário encerra a urna
print("\nUrna encerrada.\n")

# Exibição dos resultados
print("\n===== Resultado da Eleição para Prefeito =====")
print(f"{prefeito_1}: {votos_prefeito_1} votos")
print(f"{prefeito_2}: {votos_prefeito_2} votos")
print(f"{prefeito_3}: {votos_prefeito_3} votos")
print(f"{prefeito_4}: {votos_prefeito_4} votos")

print("\n===== Resultado da Eleição para Vereador =====")
print(f"{vereador_1}: {votos_vereador_1} votos")
print(f"{vereador_2}: {votos_vereador_2} votos")
print(f"{vereador_3}: {votos_vereador_3} votos")
print(f"{vereador_4}: {votos_vereador_4} votos")
print(f"{vereador_5}: {votos_vereador_5} votos")
print(f"{vereador_6}: {votos_vereador_6} votos")
print(f"{vereador_7}: {votos_vereador_7} votos")
print(f"{vereador_8}: {votos_vereador_8} votos")
print(f"{vereador_9}: {votos_vereador_9} votos")
print(f"{vereador_10}: {votos_vereador_10} votos")

print(f"\nVotos Nulos: {votos_nulo}")
print(f"Votos em Branco: {votos_branco}\n")

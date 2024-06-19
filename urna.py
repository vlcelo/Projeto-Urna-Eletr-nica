# Inicialização da urna eletrônica
print("Bem-vindo à urna eletrônica da eleição municipal!")

# Variáveis de controle
eleitores_totais = 40
eleitores_votaram = 0
votos_prefeito = [0, 0, 0, 0]  # Índices representam os candidatos 1, 2, 3 e 4
votos_vereador = [0] * 10  # Índices representam os candidatos 1 a 10

# Mesário abre a urna
print("\nUrna aberta. Eleitores começarão a votar.\n")

# Simulação da votação
while eleitores_votaram < eleitores_totais:
    num_eleitor = eleitores_votaram + 1
    zona_secao_corretas = False
    
    # Simulação de verificação de zona e seção (simplificado para fins didáticos)
    if num_eleitor % 2 == 0:  # Exemplo de verificação fictícia
        zona_secao_corretas = True
    
    if zona_secao_corretas:
        print(f"Eleitor {num_eleitor}: Autorizado a votar.")
        
        # Simulação de escolha do voto (candidato ou nulo/branco)
        tipo_voto = input("Digite P para prefeito, V para vereador, N para nulo, B para branco: ").upper()
        
        if tipo_voto == 'P':
            voto_prefeito = int(input("Digite o número do candidato a prefeito (1 a 4): "))
            if 1 <= voto_prefeito <= 4:
                votos_prefeito[voto_prefeito - 1] += 1
            else:
                print("Voto inválido para prefeito.")
        elif tipo_voto == 'V':
            voto_vereador = int(input("Digite o número do candidato a vereador (1 a 10): "))
            if 1 <= voto_vereador <= 10:
                votos_vereador[voto_vereador - 1] += 1
            else:
                print("Voto inválido para vereador.")
        elif tipo_voto == 'N':
            print("Voto nulo registrado.")
        elif tipo_voto == 'B':
            print("Voto em branco registrado.")
        else:
            print("Opção de voto inválida.")
        
        eleitores_votaram += 1
    else:
        print(f"Eleitor {num_eleitor}: Não autorizado a votar nesta urna.")

# Mesário encerra a votação
print("\nVotação encerrada. Apurando os resultados...\n")

# Exibição dos resultados
print("Resultados da eleição:")
print("Votos para Prefeito:")
for i in range(4):
    print(f"Candidato {i+1}: {votos_prefeito[i]} voto(s)")
    
print("\nVotos para Vereador:")
for i in range(10):
    print(f"Candidato {i+1}: {votos_vereador[i]} voto(s)")
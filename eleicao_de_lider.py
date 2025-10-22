# Lista de processos simulados com seus identificadores (IDs)
processos = [1, 2, 3, 4]  # Quanto maior o ID, mais "poderoso" o processo

# O processo com o maior ID é inicialmente considerado o coordenador
coordenador = 4  

# Função que simula a falha do processo coordenador
def falha_do_coordenador():
    global coordenador
    print(f"O coordenador {coordenador} falhou!")  # Mensagem informativa
    coordenador = None  # Remove o coordenador atual (simula falha)

# Função responsável por iniciar o processo de eleição de líder
def eleicao(iniciador):
    global coordenador
    print(f"Processo {iniciador} inicia eleição...")  # Indica quem iniciou
    # Cria uma lista com os processos de ID maior que o iniciador
    maiores = [p for p in processos if p > iniciador]
    
    # Se não há processos com ID maior, o iniciador torna-se o novo líder
    if not maiores:
        coordenador = iniciador
        print(f"Processo {iniciador} é o novo coordenador.")
    else:
        # Envia mensagens para os processos de maior ID
        for p in maiores:
            print(f"Processo {iniciador} envia mensagem para {p}.")
        # O processo com o maior ID assume a liderança
        coordenador = max(maiores)
        print(f"Processo {coordenador} foi eleito como novo coordenador.")

# EXECUTANDO A SIMULAÇÂO

print("\n--- Estado Inicial ---")
print("Processos ativos:", processos)
print("Coordenador atual:", coordenador)

# 1. Simulação da falha do líder (processo 4)
falha_do_coordenador() 
processos.remove(4) # Remove o 4 da lista de processos "vivos"
print("\nProcessos ativos (após falha):", processos)
print("Coordenador atual:", coordenador)

# O processo 1 detecta a falha e inicia a eleição
eleicao(iniciador=1)

print("\n--- Estado Final (Eleição 1) ---")
print("Novo Coordenador:", coordenador)

# 2. Simular a falha do novo líder (processo 3)
coordenador_anterior = coordenador
coordenador = coordenador_anterior
falha_do_coordenador() 
processos.remove(coordenador_anterior) # Remove o 3 da lista de processos "vivos"
print("\nProcessos ativos (após nova falha):", processos)
print("Coordenador atual:", coordenador)

# O processo 2 detecta a falha e inicia a eleição
eleicao(iniciador=2)

print("\n--- Estado Final (Eleição 2) ---")
print("Novo Coordenador:", coordenador)
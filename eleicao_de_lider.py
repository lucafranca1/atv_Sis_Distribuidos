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
    print(f"Processo {iniciador} inicia eleição...")
    maiores = [p for p in processos if p > iniciador]
    
    if not maiores:
        coordenador = iniciador
        print(f"Processo {iniciador} é o novo coordenador.")
    else:
        for p in maiores:
            print(f"Processo {iniciador} envia mensagem para {p}.")
        coordenador = max(maiores)
        print(f"Processo {coordenador} foi eleito como novo coordenador.")

# --- SIMULAÇÃO ---

print("\n--- Estado Inicial ---")
print("Processos ativos:", processos)
print("Coordenador atual:", coordenador)

# 1. Falha do líder
falha_do_coordenador()
processos.remove(4)
print("\nProcessos ativos (após falha):", processos)
print("Coordenador atual:", coordenador)

# Eleição 1
eleicao(1)
print("\n--- Estado Final (Eleição 1) ---")
print("Novo Coordenador:", coordenador)

# 2. Falha do novo líder
coordenador_anterior = coordenador
falha_do_coordenador()
if coordenador_anterior in processos:
    processos.remove(coordenador_anterior)
print("\nProcessos ativos (após nova falha):", processos)
print("Coordenador atual:", coordenador)

# Eleição 2
eleicao(2)
print("\n--- Estado Final (Eleição 2) ---")
print("Novo Coordenador:", coordenador)

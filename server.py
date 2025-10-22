# Importa o servidor XML-RPC que permite chamadas remotas
from xmlrpc.server import SimpleXMLRPCServer

# Define uma função simples que soma dois números
def soma(a, b):
    return a + b



# Cria o servidor na porta 8000 (localhost)
server = SimpleXMLRPCServer(("localhost", 8000))

# Registra a função 'soma' para ser acessível remotamente
server.register_function(soma, "subtracao")

# Exibe mensagem informando que o servidor está ativo
print("Servidor RPC em execução...")

# Mantém o servidor escutando indefinidamente
server.serve_forever()

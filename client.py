# Importa o cliente XML-RPC
import xmlrpc.client

# Cria o proxy de comunicação com o servidor RPC
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Chama a função remota 'soma' passando dois parâmetros
resultado = proxy.soma(10, 9)

# Exibe o resultado retornado pelo servidor
print("Resultado da soma remota:", resultado)

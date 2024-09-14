import socket

#import socket

# Configurações do servidor
HOST = "0.0.0.0" # Endereço para aceitar todos os servidores disponíveis
PORT = PORT # Porta que o servidor usará (destino)

# Criação do socket IPv4 (AF_INET), UDP (SOCK_DGRAM):
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind() # Associa o socket ao endereço e porta especificados
    print(f"Servidor (UDP) escutando em {HOST}:{PORT}")

    while True:
        dados, endereco = s.recvfrom(1024) # Recebe os dados passados pelo cliente
        print(f"Recebido: {dados.decode()} de {endereco}")
        mensagem = dados.decode()
        if mensagem == "PING":
            resposta = "PONG"
            s.sendto(resposta.encode(), endereco)

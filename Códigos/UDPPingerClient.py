import time
import socket

# Configurações do cliente
HOST = "HOSTIP" # Endereço do servidor
PORT = PORT # Porta que o servidor está usando

# Criação do socket IPv4 (AF_INET), UDP (SOCK_DGRAM):
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as c:
    mensagem = "PING"
    for i in range(10): # Para enviar 10 mensagens
        inicio = time.time() # Registra o tempo de início do envio da mensagem
        c.sendto(mensagem.encode(), (HOST, PORT)) # Envia a mensagem ao servidor
        
        try:
            dados, endereco = c.recvfrom(1024) # Recebe os dados passados pelo servidor
            fim = time.time() # Registra o tempo de chagada da resposta

            rtt = (fim - inicio) * 1000 # Calcula o tempo de ida e volta (RTT) em milissegundos

            print(f"Ping {i + 1} - Recebido do servidor: {dados.decode()}")
            print(f"RTT: {rtt:.2f} ms")
        except socket.timeout:
            print(f"Ping {i + 1}: Timeout")
        
        time.sleep(1) # Aguarda 1 segundo entre as mensagens

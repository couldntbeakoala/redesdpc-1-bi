# Passo a Passo (Redes de Computadores - Atividade do 1º Bimestre)

Este `Markdown` tem como objetivo guiar o usuário através de uma apresentação passo a passo para completar a atividade passada pelo professor Matheus. Serão usados os códigos que o mesmo disponibilizou via aplicativo **Multivix**.

---

## 1. Instalação e Configuração do Ambiente

Abaixo, estão as instruções para a instalação e configuração das ferramentas necessárias, organizadas por ordem de tamanho do arquivo de instalação, do mais pesado para o mais leve.

**Na máquina local...**

## 1.1. Instalação do VirtualBox (VM):

1. Acesse [https://www.virtualbox.org](https://www.virtualbox.org).
2. Baixe e instale a versão mais recente do VirtualBox.

### 1.2. Instalação do Kali Linux (VirtualBox)

Há duas formas de fazer isto, a manual (instala e configura) e a automática (uma VirtualBox já configurada).

- Manual:

Será preciso seguir todos os passos para configurar o Kali Linux do zero.
1. Baixe a imagem ISO do Kali Linux em [https://www.kali.org/get-kali/#kali-installer-images](https://www.kali.org/get-kali/#kali-installer-images).
2. Ao abrir o VirtualBox, vá em **Ferramentas** e selecione **Novo** no menu de opções na parte superior do gerenciador para criar uma nova máquina virtual:
    - Tipo: **Linux**.
    - Versão: **Debian (64-bit)**.
    - Atribua memória e armazenamento conforme necessário.
3. Na aba _Storage_, monte a ISO do Kali Linux.
4. Inicie a máquina virtual e siga o processo de instalação do sistema.

- Automática:

Todo o processo de instalação do sistema é evitado, pois utiliza-se uma máquina virtual pronta no formato `.vbox` (configuração da VM) e o respectivo arquivo de disco virtual `.vdi`.
1. Baixe a máquina virtual pré-configurada (versão `VirtualBox`) do Kali Linux em [https://www.kali.org/get-kali/#kali-virtual-machines](https://www.kali.org/get-kali/#kali-virtual-machines).
2. Ao abrir o VirtualBox, vá em **Ferramentas** e selecione **Acrescentar** no menu de opções na parte superior do gerenciador para adicionar uma máquina virtual:
    - Selecione o arquivo `.vbox` baixado.
4. Verifique as configurações da VM:
    - Selecione a máquina virtual, clique em **Configurações**, em seguida na aba **Rede**, ajuste `Conectado a:` para **Placa em modo Bridge**, para que a rede da máquina virtual seja a mesma que a do computador.
5. Clique em **Iniciar** para ligar a máquina virtual. A máquina já está pronta para o uso.
    - Porque a máquina já está configurada, ela possui um usuário pronto, cujos _username_ e _password_ estão apresentados em sua descrição:
    - Selecione a máquina virtual, clique em **Configurações**, na aba **Geral**, clique em **Descrição** OU Selecione a máquina virtual e role com o _scroll_ do mouse até encontrar a seção de **Descrição**.
    - Caso, ao iniciar a máquina virtual, a tela permaneça em _boot_, encerre a máquina virtual e a inicie novamente. Porém, se isto persistir, acesse este [site](https://medium.com/@joemcfarland/tricks-and-tips-fixing-virtualbox-kali-linux-black-screen-5adefeb25ed) e verifique se as dicas resolvem o problema.

### 1.2. Instalação do Visual Studio Code (VSCode):

1. Baixe e instale o aplicativo por meio do site oficial: [https://code.visualstudio.com](https://code.visualstudio.com)
2. Ao abrir o `Visual Studio Code`, há a seguinte apresentação:
3. Vá à aba de `Extensões` e busque por `Python`, em seguida, instale as seguintes opções:


### 1.3. Instalação do Compilador Python:

Passo a passo - [(Linux)](https://python.org.br/instalacao-linux/) | [(Windows)](https://python.org.br/instalacao-windows/):

1. Baixe e instale o aplicativo por meio do site oficial: [https://python.org](https://python.org)
2. Durante a instalação, marque a opção `Add Python to PATH`, para que o sistema reconheça o Python diretamente pelo terminal.
> Isto é necessário porque o Windows usará a variável `PATH` do ambiente para obter uma lista de diretórios para procurar o arquivo `python.exe`

- Em seguida, verifique a instalação no terminal com:

```bash
python --version
```

> A versão do _Python_ instalado em seu computador deverá aparecer, do contrário, será necessário configurar o caminho do _Python_ manualmente nas variáveis de ambiente do sistema:
>
> <details>
>
> <summary>(Windows)</summary>
>
> 1. No menu iniciar, busque por `Python` e clique com o botão direito no executável, em seguida, selecione "Abrir local de arquivo" e _somente copie_ o caminho ("URL" do local), adicionando > `\python.exe` no final.
> 2. Em seguida, aproveite a pasta aberta (se fechou, abra uma qualquer) e, na coluna de atalhos procure por **Este Computador** (normalmente acima de "Rede"; do contrário, clique com o botão direito em um espaço vazio da coluna e ative "Mostrar Este PC").
> 3. Clique com o botão direito e depois selecione **Propriedades**. Na seção de "Links relacionados", selecione **Configurações avançadas do sistema** e depois, lá embaixo **Variáveis de Ambiente...**.
>   - Se já houver uma variável `Path`, selecione-a e clique em **Editar**, aperte em **Novo** e cole o caminho do executável _Python_ que copiou anteriormente.
>   - Do contrário, clique em **Novo**, em **Nome da variável:**, digite "Path". Em seguida, em **Valor da variável:**, cole o caminho do executável _Python_ que copiou anteriormente.
>
> </details>

### 1.4. Instalação do Wireshark

Porque não será utilizado o **Wireshark** pela máquina local, devido a problemas de análise de tráfego em rede no sistema _Windows_, **não há necessidade de instalá-lo**, uma vez que já consta integrado na máquina virtual _Kali Linux_. Porém, **se quiser** instalá-lo:

1. Acesse [https://www.wireshark.org](https://www.wireshark.org).
2. Baixe e instale a versão mais recente do Wireshark.

---

## 2. Configuração e Criação dos Scripts TCP/UDP

### 2.1. Scripts de Servidor e Cliente (TCP)

Neste caso, o servidor será a máquina local e o cliente, a máquina virtual anteriormente configurada.

Para editar os arquivos, abra o **VSCode** e selecione uma pasta onde os arquivos estão localizados, em seguida, substitua:
- `PORT`:
- `HOSTPORT`:
    - Ou defina-o antes por `HOSTPORT = 127.0.0.1`
        - Troque `127.0.0.1` pela porta desejada.
- `HOST`:
- `HOSTIP`: 
    - Ou defina-o antes por `HOSTIP = 192.168.0.0`
        - Troque `192.168.0.0` pelo endereço de IP do servidor, no caso, a máquina local.

#### TCPServer.py (Máquina Local)

```python
from socket import *

serverPort = HOSTPORT
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
```

<details>

<summary>Importação de biblioteca</summary>

```python
from socket import *
```

Importa todas as funcionalidades do módulo `socket`, uma biblioteca padrão do Python usada para trabalhar com conexões de rede.


</details>

<details>

<summary>Configuração, associação e conexão</summary>

```python
serverPort = HOSTPORT
serverSocket = socket(AF_INET, SOCK_STREAM)
```

- `serverPort = HOSTPORT`: define a porta em que o servidor escutará conexões de clientes; `HOSTPORT` tendo que ser substituído por um número ou previamente definido (exemplo: `HOSTPORT = 12345`).
- `serverSocket = socket(AF_INET, SOCK_STREAM)`: cria-se um socket em que `AF_INET` indica que este _socket_ utilizará o protocolo IPv4; *SOCK_STREAM* indica que utilizará o protocolo de transporte _TCP_.

```python
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
```

- `serverSocket.bind(('', serverPort))`: associa o _socket_ a um endereço de IP e uma porta específicados, sendo o primeiro parâmetro referindo-se ao IP e o segundo referindo-se à porta.
- `serverSocket.listen(1)`: coloca o _socket_ em modo de escuta, em que espera por conexões de clientes. `1` como parâmetro define o tamanho da fila de conexões pendentes (no caso, máximo de 1 cliente aguardando para conectar-se simultaneamente ao servidor).
- `print ('The server is ready to receive')`: imprime uma mensagem indicando que o servidor está pronto para receber conexões.

</details>

<details>

<summary>Comunicação, processamento e fechamento</summary>

```python
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
```

- `while 1:` Cria um _loop_ infinito para que o servidor continue aguardando por novas conexões até que seja encerrado manualmente.
- `serverSocket.accept()`: entra em espera até que um cliente se conecte e retorna:
    - `connectionSocket`: um novo _socket_, específico para tal conexão; utilizado para comunicação com o cliente conectado.
    - `addr`: o endereço IP e a porta do cliente que se conectou.
- `sentence = connectionSocket.recv(1024)`: `sentence` armazena o retorno da função `connectionSocket.recv(1024)` que recebe os dados enviados pelo cliente, cujo parâmetro `1024` define o tamanho máximo do _buffer_ de recepção (no caso, até 1024 _bytes_).
- `capitalizedSentence = sentence.upper()`: `capitalizedSentence` armazena a conversão da _string_ recebida para letras maiúsculas.
- `connectionSocket.send(capitalizedSentence)`: envia a mensagem modificada de volta ao cliente através do _socket_ previamente criado.
- `connectionSocket.close()`: encerra a comunicação com o cliente.
    - O servidor continua ativo para aceitar novas conexões devido ao _loop_ `while 1`.


</details>

#### TCPClient.py (Máquina Virtual - Kali Linux)

```python
from socket import *
serverName = "HOSTIP"
serverPort = HOSTPORT
addr = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(addr)
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence)
clientSocket.close()
```

<details>

<summary>Importação de biblioteca</summary>

```python
from socket import *
```

Importa todas as funcionalidades do módulo `socket`, uma biblioteca padrão do Python usada para trabalhar com conexões de rede.


</details>

<details>

<summary>Configuração de conexão</summary>

```python
serverName = "HOSTIP"
serverPort = HOSTPORT
addr = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(addr)
```

- `serverName`: armazena o endereço IP ou nome do _host_ do servidor.
- `serverPort`: armazena a porta do servidor.
- `addr`: armazena o conjunto do endereço de IP e porta, usada posteriormente para conectar-se ao servidor.
- `clientSocket = socket(AF_INET, SOCK_STREAM)`: cria-se um socket em que `AF_INET` indica que este _socket_ utilizará o protocolo IPv4; *SOCK_STREAM* indica que utilizará o protocolo de transporte _TCP_.
- `clientSocket.connect(addr)`: conecta o cliente ao servidor por meio do endereço e porta previamente definidos.


</details>

</details>

<details>

<summary>Comunicação, processamento e fechamento</summary>

```python
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence)
clientSocket.close()
```

- `sentence = input('Input lowercase sentence:')`: solicita ao usuário que insira uma frase em letras minúsculas e armazena na variável `sentence`.
- `clientSocket.send(sentence.encode('utf-8'))`: modifica a mensagem, convertendo a frase do formato de _string_ para _bytes_ por meio da codificação `UTF-8`.
- `modifiedSentence = clientSocket.recv(1024)`: recebe até 1024 _bytes_ (definidos como parâmetro para tamanho do _buffer_) e armazena os dados recebidos na variável `modifiedSentence`.
- `print ('From Server:', modifiedSentence)`: imprime a mensagem modificada.
- `clientSocket.close()`: encerra a comunicação com o servidor.


</details>

### 2.1. Scripts de Servidor e Cliente (UDP)

#### UDPServer.py (Máquina Local)

```python
from socket import *
serverPort = HOSTPORT
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
```

<details>

<summary>Importação de biblioteca</summary>

```python
from socket import *
```

Importa todas as funcionalidades do módulo `socket`, uma biblioteca padrão do Python usada para trabalhar com conexões de rede.

</details>

<details>

<summary>Configuração, associação e conexão</summary>

```python
serverPort = HOSTPORT
serverSocket = socket(AF_INET, SOCK_DGRAM)
```

- `serverPort = HOSTPORT`: define a porta em que o servidor escutará conexões de clientes; `HOSTPORT` tendo que ser substituído por um número ou previamente definido (exemplo: `HOSTPORT = 12345`).
- `serverSocket = socket(AF_INET, SOCK_DGRAM)`: cria-se um socket em que `AF_INET` indica que este _socket_ utilizará o protocolo IPv4; *SOCK_DGRAM* indica que utilizará o protocolo de transporte _UDP_.

```python
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
```

- `serverSocket.bind(('', serverPort))`: associa o _socket_ a um endereço de IP e uma porta específicados, sendo o primeiro parâmetro referindo-se ao IP e o segundo referindo-se à porta.
- `print ('The server is ready to receive')`: imprime uma mensagem indicando que o servidor está pronto para receber conexões.

</details>

<details>

<summary>Comunicação e processamento</summary>

```python
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
```

- `while 1:` Cria um _loop_ infinito para que o servidor continue aguardando por novas conexões até que seja encerrado manualmente.
- `serverSocket.recvfrom(2048)`: recebe até 1024 _bytes_ (definidos como parâmetro para tamanho do _buffer_) e retorna:
    - `message`: uma variável que armazena os dados recebidos.
    - `clientAddress`: o endereço IP e a porta do cliente.
- `modifiedMessage = message.upper()`: `modifiedMessage` armazena a conversão da _string_ recebida para letras maiúsculas.
- `serverSocket.sendto(modifiedMessage, clientAddress)`: envia a mensagem modificada de volta ao cliente através do _socket_ previamente criado.

</details>

#### UDPClient.py (Máquina Virtual - Kali Linux)

```python
from socket import *
serverName = "HOSTIP"
serverPort = HOSTPORT
addr = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode('utf-8'), addr)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()
```

<details>

<summary>Importação de biblioteca</summary>

```python
from socket import *
```

Importa todas as funcionalidades do módulo `socket`, uma biblioteca padrão do Python usada para trabalhar com conexões de rede.


</details>

<details>

<summary>Configuração de conexão</summary>

```python
serverName = "HOSTIP"
serverPort = HOSTPORT
addr = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)
```

- `serverName`: armazena o endereço IP ou nome do _host_ do servidor.
- `serverPort`: armazena a porta do servidor.
- `addr`: armazena o conjunto do endereço de IP e porta, usada posteriormente para conectar-se ao servidor.
- `clientSocket = socket(AF_INET, SOCK_DGRAM)`: cria-se um socket em que `AF_INET` indica que este _socket_ utilizará o protocolo IPv4; *SOCK_DGRAM* indica que utilizará o protocolo de transporte _UDP_.


</details>

<details>

<summary>Comunicação, processamento e fechamento</summary>

```python
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode('utf-8'), addr)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()
```

- `message = input('Input lowercase sentence:')`: solicita ao usuário que insira uma frase em letras minúsculas e armazena na variável `message`.
- `clientSocket.sendto(message.encode('utf-8'), addr)`: modifica a mensagem, convertendo a frase do formato de _string_ para _bytes_ por meio da codificação `UTF-8` e a envia para o endereço especificado por `addr` (conjunto de endereço IP e porta).
- `clientSocket.recvfrom(2048)`: recebe até 2048 _bytes_ (definidos como parâmetro para tamanho do _buffer_) e retorna:
    - `modifiedMessage`: uma variável que armazena os dados recebidos.
    - `serverAddress`: o endereço IP e a porta do servidor.
- `print (modifiedSentence)`: imprime a mensagem modificada.
- `clientSocket.close()`: encerra a comunicação com o servidor.

</details>

#### UDPPingerClient.py (Máquina Virtual - Kali Linux)

```python
import sys, time
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
timeout = 1 # in second
 
# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
clientsocket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout as 1 second
clientsocket.settimeout(timeout)
# Command line argument is a string, change the port into integer
port = int(port)  
# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent
    data = "Ping " + str(ptime) + " " + time.asctime()

    try:
        # Sent time
        RTTb = time.time()
        # Send the UDP packet with the ping message
        clientsocket.sendto(data,(host, port))
        # Receive the server response
        message, address = clientsocket.recvfrom(1024)  
        # Received time
        RTTa = time.time()
        # Display the server response as an output
        print "Reply from " + address[0] + ": " + message       
        # Round trip time is the difference between sent and received time
        print "RTT: " + str(RTTa - RTTb)
    except:
        # Server does not response
        # Assume the packet is lost
        print "Request timed out."
        continue

# Close the client socket
clientsocket.close()
```

<details>

<summary>Importação de biblioteca</summary>

```python
import sys, time
from socket import *
```

- `import sys, time`:
    - `sys` é um módulo que fornece acesso a algumas variáveis e funções específicas do sistema, como argumentos da linha de comando.
    - `time` é um módulo que fornece funções relacionadas ao tempo, como medir intervalos de tempo e obter o tempo atual.
- `from socket import *`: importa todas as funcionalidades do módulo `socket`, que é usado para criar e manipular conexões de rede.

</details>

<details>

<summary>Configuração, tempo e conexão</summary>

```python
argv = sys.argv                      
host = argv[1]
port = argv[2]
timeout = 1
clientsocket = socket(AF_INET, SOCK_DGRAM)
clientsocket.settimeout(timeout)
port = int(port)
ptime = 0
```

- `argv = sys.argv`:
    - Obtém a lista de argumentos passados para o _script_ na linha de comando.
    - `sys.argv[0]` é o nome do _script_, e os argumentos seguintes são os fornecidos pelo usuário.
- `host = argv[1]`: a variável `host` recebe o primeiro argumento da linha de comando, que representa o nome ou IP do servidor.
- `port = argv[2]`: a variável `port` recebe o segundo argumento da linha de comando, que representa a porta do servidor.
- `timeout = 1`: define o tempo limite (_timeout_) para o _socket_ como `1` segundo, no caso.
- `clientsocket = socket(AF_INET, SOCK_DGRAM)`: cria-se um socket em que `AF_INET` indica que este _socket_ utilizará o protocolo IPv4; *SOCK_DGRAM* indica que utilizará o protocolo de transporte _UDP_.
- `clientsocket.settimeout(timeout)`: define o tempo limite de 1 segundo para operações de leitura no socket.
- `port = int(port)`: porque o argumento da linha de comando é uma _string_, converte o valor da porta de _string_ para inteiro (_integer_).
- `ptime = 0`: inicializa a variável `ptime`, que será usada para contar o número de pacotes de _ping_ enviados.

</details>

<details>

<summary>Comunicação, tempo e encerramento</summary>

```python
while ptime < 10: 
    ptime += 1
    data = "Ping " + str(ptime) + " " + time.asctime()
    
    try:
        RTTb = time.time()
        clientsocket.sendto(data, (host, port))
        message, address = clientsocket.recvfrom(1024)  
        RTTa = time.time()
        print "Reply from " + address[0] + ": " + message       
        print "RTT: " + str(RTTa - RTTb)
    except:
        print "Request timed out."
        continue
```

- `while ptime < 10:`: inicia um _loop_ que executa enquanto `ptime` for menor que 10, enviando 10 pacotes de ping.
- `ptime += 1`: incrementa o contador `ptime` a cada iteração do _loop_.
- `data = "Ping " + str(ptime) + " " + time.asctime()`: cria a mensagem de _ping_ com o número da sequência `ptime` e o horário atual.
- `RTTb = time.time()`: registra o tempo atual antes do envio do pacote (tempo de envio).
- `clientsocket.sendto(data, (host, port))`: envia o pacote de _ping_ para o servidor no endereço e porta especificados.
- `clientsocket.recvfrom(1024)`: recebe até 1024 _bytes_ (definidos como parâmetro para tamanho do _buffer_) e retorna:
    - `message`: uma variável que armazena os dados recebidos.
    - `address`: o endereço IP e a porta do servidor.
- `RTTa = time.time()`: registra o tempo atual após o recebimento da resposta (tempo de recebimento).
- `print "Reply from " + address[0] + ": " + message`: imprime a resposta recebida e o endereço do servidor.
    - Usa-se operador `+` para concatenar _strings_.
- `print "RTT: " + str(RTTa - RTTb)`: calcula e imprime o tempo de ida e volta (_RTT_) como a diferença entre o tempo de recebimento e o tempo de envio.
    - Usa-se operador `+` e função `str()` para que seja possível concatenar o valor em _strings_, deixando tudo no mesmo formato.
- `except`: captura exceções se ocorrer um erro, como o _timeout_ de leitura.
- `print "Request timed out."`: imprime uma mensagem se a resposta do servidor não for recebida dentro do tempo limite definido.
- `continue`: continua o _loop_ para enviar o próximo pacote de _ping_.
- `clientsocket.close()`: encerra a comunicação com o cliente.

</details>

### 2.2. Compartilhamento de Arquivos

Para facilitar o processo, adicione um diretório compartilhado (em que ambas as máquinas local e virtual possa trocar arquivos):

1. Crie uma pasta qualquer e copie seu caminho ("URL" do local).
2. Em seguida, abra o VirtualBox, selecione a máquina virtual, clique em **Configurações**.
3. Vá para a aba **Pastas Compartilhadas**, clique no ícone de pasta com um operador `+` esverdeado para adicionar uma pasta compartilhada e cole seu caminho.
    - Certifique-se de que `Montar Automaticamente` esteja marcado.
4. Mova/copie os _scripts_ para a pasta compartilhada; agora ambas as máquinas (local e virtual) têm acesso aos arquivos dentro de tal pasta.

---

## 3. Análise de Pacotes com Wireshark

### 3.1. Captura de Tráfego

**Na máquina local:**

1. Abra o **Wireshark** e selecione a interface de rede correspondente à sua conexão.
2. Inicie a captura clicando no ícone de _iniciar captura_.
3. Execute os _scripts_ de cliente e servidor (primeiro inicie o servidor, depois o cliente).
4. Pare a captura após a comunicação finalizar.

### 3.2. Análise dos Pacotes

- Para filtrar a captura a fim de visualizar somente o que interessa, vá para o campo de filtro e digite:
    - Para filtrar somente protocolos _DNS_: `dns`
          - Consulta e resposta: vá ao campo **Domain Name System (query)** (consulta) / **Domain Name System (response)** (resposta), no campo `Queries`, em seguida `Name`: haverá a "URL" do site.
    - Para filtrar somente protocolos _TCP_ e _UDP_ na porta especificda: `tcp.port == PORT || udp.port == PORT` (sendo `PORT` a porta do servidor)
    - Para filtrar somente os endereços _IP_: `ip.addr == IP || ip.addr == IP` (sendo `IP`s, respectivamente, os IPs do cliente e servidor ou vice-versa)

### 3.3. Informações dos Pacotes

#### 3.3.1. IP de Origem e Destino

- Em detalhes do pacote, expanda o cabeçalho IP: **Internet Protocol Version 4**.
    - No campo `Source Address` (endereço de origem) está o IP de origem em relação ao tráfego.
        - Ou na mesma linha logo após de `Src:`
    - No campo `Destination Address` (endereço de destino) está o IP de destino em relação ao tráfego.
        - Ou na mesma linha logo após de `Dst:`

#### 3.3.2. Protocolo Utilizado

- Em detalhes de cada pacote há uma lista com cabeçalhos. Logo após o cabeçalho IP está o cabeçalho da camada de transporte referente ao pacote:
    - `Transmission Control Protocol` (TCP).
    - `User Datagram Protocol` (UDP).

#### 3.3.3. Porta de Origem e Destino

- Em detalhes do pacote, expanda o cabeçalho da camada de transporte (TCP/UDP): **Transmission Control Protocol**/**User Datagram Protocol**.
    - No campo `Source Port` (porta de origem) está a porta de origem em relação ao tráfego.
        - Ou na mesma linha logo após de `Src Port:`
    - No campo `Destination Port` (porta de destino) está a porta de destino em relação ao tráfego.
        - Ou na mesma linha logo após de `Dst Port:`

#### 3.3.4. Tamanho do Pacote

- Há duas formas de visualizar o tamanho do pacote:
    - Pode ser calculado pela _soma_ do tamanho do cabeçalho do protocolo (`Header length` (acima de `Flags`, no caso do TCP) / `Length` (acima de `Checksum`, no caso do UDP)) com a carga útil (`payload`), em _bytes_:
        - Vá ao cabeçalho **Transmission Control Protocol**/**User Datagram Protocol**, campo `Header length` (TCP) / `Length` (UDP)  para o tamanho do cabeçalho do protocolo.
        - A carga útil está localizada no cabeçalho **Data** no campo `payload`.
    - Pode ser calculado pela _subtração_ do tamanho do cabeçalho do IP (`Total length`) com o tamanho do cabeçalho do protocolo `Header length` (TCP) / `Length` (UDP), em _bytes_:
        - Vá ao cabeçalho **Internet Protocol Version 4**, campo `Total length` para o tamanho total.
        - No mesmo cabeçalho, subtraia o valor de `Total length` com o campo `Header length` (TCP) / `Length` (UDP) no cabeçalho respectivo do protocolo.
      Isto porque é em segmento, dos dados (`payload`) ao fim do pacote completo (`Frame`), o comprimento de cada camada é a soma do comprimento da anterior com o seu próprio.

## Referências
- [Instalação do VSCode](https://code.visualstudio.com/docs/setup/setup-overview)
- [Instalação do Python](https://www.python.org/downloads/)
    - [Programação de Soquetes (Python)](https://docs.python.org/pt-br/3/howto/sockets.html) & [Biblioteca Socket (Python)](https://docs.python.org/3/library/socket.html)
- [Instalação do VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Wireshark: Como usar e filtrar pacotes](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html)

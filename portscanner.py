import socket
host = input("Qual o ip para o portscannig? ")
portas = [21,22,23,80,443]
print("Portas abertas: ")
for porta in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        codigoRetorno = sock.connect_ex((host,porta))
        sock.close()
        if codigoRetorno == 0:
                print("A porta", porta, "esta aberta") 

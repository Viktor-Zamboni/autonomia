import socket

#si mette 0.0.0.0 perchè si mette in ascolto su tutte le interfacce di rete
ipAddress = "0.0.0.0"
udpPort = 5555

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#binding tra porta e ip per avviare il server
udpSocket.bind((ipAddress, udpPort))
print("server UDP avviato...")
#attesa bloccante di un messaggio udp quindi ricevo al massimo 1024 byte alla volta
(data, clientAddress) = udpSocket.recvfrom(1024)
#se arrivo a questo punto, ho un pacchetto udp da spacchettare
receivedData = data.decode("utf-8")
print(f"ricevuto udp zio pera pkt da{clientAddress}")
print(f"Contenuto: {receivedData}")
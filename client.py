#udp(livello 4 come tcp e si basano sugli ip e quindi non è sicuro) è un protocollo non orientato alla connessione, ossia non crea un canale tra host e server, 
#gli svantaggi di questo che in caso di intasamento non viene autoinviato i messaggi però un vantaggio è che veloce(tcp è lento ma ti manda i messaggi per recuperare
#in caso di intasamento e un server non chiederà mai se ti vuoi agganciare a lui ma è sempre il client)
#la three way handshake(tcp) è chiedere se mi posso agganciare e se dice di si si aggancia(richiesta, risposta del server, risposta del client)
#con tcp non ci sono broadcast
#un processo al livello 4 è caratterizzato da una tupla di valori ip-porta(socket), 
#le prime 1024(in totale sono circa 65000 e le prime 20000 sono conosciute e possono essere modificate)
#sono le wellknown port ed è meglio non usarla per non sporcarla e quindi è un identicativo di un processo


import socket

#(ip della macchine e porta a scelta)
udpServerIp = "192.168.6.113"
udpServerPort = 5555
#socket del server udp(un datagram è messaggio udp ed è un messaggio a sè e non un flow
#e af_inet è per dire che uso ipv4)
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "hello"
udpSocket.sendto(message.encode("utf-8"), (udpServerIp, udpServerPort))
#!/usr/bin/env python3

import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        print(f"\n[+] Nuevo cliente conectado: {client_addr}")


    def run(self):

        message = ''

        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            if message.strip() == 'bye':
                break

            print(f"\n[+] Mensaje enviado por el cliente: {message.strip()}")
            # Podríamos poner sendall(data) pero eso es para mensajes muy largos que nos interese que llegue al destino
            self.client_sock.send(data)

        print(f"\n[!] Cliente {self.client_addr} desconectado")
        self.client_sock.close()

host = 'localhost'
port = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Esto es para manipular la propiedad de un nivel (donde se manejan los diferentes protocolos de red)
    # Algunas propiedades: socket.IPPROTO_IP, socket.IPPROTO_TCP, socket.IPPROTO_UDP
    # En este caso vamos a reutilizar la espera que no dejaba ejecutar el server al cerrar la conexión

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #TIME_WAIT
    server_socket.bind((host,port))

    print("\n[+] En espera de conexiones entrantes...")

    while True:
        
        server_socket.listen() # Hay que ponerla para que el cliente se pueda conectar, aunque no usemos argumentos
        client_sock, client_addr = server_socket.accept()

        # Uso de hilos
        #new_thread = threading.Thread(target=mi_funcion, args=(client_sock, client_addr))
        # Como threading.Thread instancia una clase que existe, es mejor crear la nuestra propia que herede de esa
        new_thread = ClientThread(client_sock, client_addr)
        new_thread.start() # método run()

    

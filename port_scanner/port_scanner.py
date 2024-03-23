#!/usr/bin/env python3

import socket
import argparse
import sys
from termcolor import colored


def get_arguments():

    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", help="Victim target to scan (Ex: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", help="Port range to scan (Ex: -p 1-100)")
    options = parser.parse_args()

    if not options.target or options.port is None:
        parser.print_help()
        sys.exit(1)
    
    return options.target, options.port

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Timpo para ver si está abierto o cerrao
    return s

def port_scanner(port, host, s):

    try:
        s.connect((host, port)) 
        print(colored(f"\n[+] El puerto {port} está abierto", 'green'))
        s.close()

    except (socket.timeout, ConnectionRefusedError):
        s.close()

def scan_ports(ports, target):

    for port in ports:
        s = create_socket()
        port_scanner(port, target, s)


def parse_ports(ports_str):

    if '-' in ports_str:
        start, end = map(int, ports_str.split('-')) # En start se almacena el primer elemento antes del guion y en end el resto
        return range(start, end+1)

    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)  # Solo hay un elemento

def main():

    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host / IP Range to scan")

    args = parser.parse_args()

    return args.target


def scan(ip):
    scapy.arping(ip)


def main():
    target = get_arguments()
    scan(target)

if __name__ == "__main__":
    main()


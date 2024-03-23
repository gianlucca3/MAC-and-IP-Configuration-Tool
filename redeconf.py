#!/usr/bin/env python3
import subprocess
import random

def print_titulo():
    cor = "\033[1;{}m".format(random.randint(31, 37))
    print(cor + """
  _                                               __  __   _   ___                _   ___ ___ 
   /_\  _ _  ___ _ _ _  _ _ __  ___ _  _ ___  ___  |  \/  | /_\ / __|  __ _ _ _  __| | |_ _| _  |
  / _ \| ' \/ _ \ ' \ || | '  \/ _ \ || (_-< |___| | |\/| |/ _ \ (__  / _` | ' \/ _` |  | ||  _/
 /_/ \_\_||_\___/_||_\_, |_|_|_\___/\_,_/__/       |_|  |_/_/ \_\___| \__,_|_||_\__,_| |___|_|  
                     |__/      
  Tool created for information security study purposes
                                                                        Created for Gian Viana
  """ + "\033[0m")


if __name__ == "__main__":
    print_titulo()

def mudar_mac():
    print ("[+] Mudando MAC Address... ")
    interface = input("Digite a interface: ")
    novo_mac = input("Digite seu novo MAC: ")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", novo_mac])
    subprocess.call(["ifconfig", interface, "up"])

def mudar_ip():
    print("[+] Mudando IP Address... ")
    interface = input("Digite a interface: ")
    novo_ip = input("Digite seu novo IP: ")
    mascara = input("Digite a máscara de rede (ex. 255.255.255.0): ")

    subprocess.call(["ifconfig", interface, novo_ip, "netmask", mascara])

if __name__=="__main__":
    subprocess.call("ifconfig")
    mudar_mac()
    mudar_ip()

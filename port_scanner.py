from scapy.all import ARP, Ether, srp
import socket

target = "192.168.0.111/24"

arp = ARP(pdst=target)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

result = srp(packet, timeout=2, verbose=0)[0]


arr_of_ip = []
for sent, received in result:
    arr_of_ip.append(received.psrc)


find_flag = True

for ip in arr_of_ip:
    find_flag = True
    for port in range(1, 1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        code = s.connect_ex((ip, port))
        if code == 0:
            print("open", port)
            find_flag = False
        s.close()
    if find_flag:
        print(f'По IP адрессу: {ip} ничего не удалось найти')
        


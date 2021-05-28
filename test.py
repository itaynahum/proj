import struct

from scapy.all import *

sc = r'C:\Users\user\Desktop\test\test.pcap'

"""if packet.haslayer('ARP'):
    print(packet.show())"""
t = open(sc, 'rb').read()[0:8]
print(struct.unpack('hhl', t))

"""with open(sc, 'rb') as file_opened:
    for bit in file_opened.read():
        print(chr(bit))"""


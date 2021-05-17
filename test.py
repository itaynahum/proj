from scapy.all import *

sc = rdpcap(r'C:\Users\user\Desktop\test\test.pcap')
for p in sc:
    print(hexdump(p))


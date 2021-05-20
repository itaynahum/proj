from scapy.all import *

sc = rdpcap(r'C:\Users\user\Desktop\test\test.pcap')
for p in sc:
    if re.search(b'P', p.show()):
        print(p.show())
        time.sleep(3)


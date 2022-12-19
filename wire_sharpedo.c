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
#include <arpa/inet.h>

// used to get source and destination IP address.
struct sockaddr_in src_addr;
struct sockaddr_in dest_addr;

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

void print_IPv6_header(unsigned char* buffer){
    struct ip6_hdr *ip6_hdr_ptr = (struct ip6_hdr*) (buffer + sizeof(struct ethhdr));
    printf("\n IPv6 Header\n");
    // first 4 bits of vfc is version as per 
    int vfc = ip6_hdr_ptr->ip6_ctlun.ip6_un2_vfc;
    int version = (vfc >> 4) & 0b00001111;
    printf("\t| Version               : %d\n", version);
    printf("\t| Flow                  : %d\n", ip6_hdr_ptr->ip6_ctlun.ip6_un1.ip6_un1_flow);
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
}

void print_packet(unsigned char* buffer){
    struct ethhdr *eth = (struct ethhdr*)buffer;
    printf("\n Ethernet Header \n");
    printf("\t| Source address        : %.2X:%.2X:%.2X:%.2X:%.2X:%.2X\n", eth->h_source[0],eth->h_source[1],eth->h_source[2],eth->h_source[3],eth->h_source[4],eth->h_source[5]);
    printf("\t| Destination address   : %.2X:%.2X:%.2X:%.2X:%.2X:%.2X\n", eth->h_dest[0],eth->h_dest[1],eth->h_dest[2],eth->h_dest[3],eth->h_dest[4],eth->h_dest[5]);
    printf("\t| Protocol              : %s\n", get_ether_type(ntohs(eth->h_proto)));
    // if(ntohs(eth->h_proto) == 2054){
    //     printf("\n ARP fields\n");
        
    // } 
    if(ntohs(eth->h_proto) == 2048){
        print_IP_header(buffer);
    } else if(ntohs(eth->h_proto) == 34525){
        print_IPv6_header(buffer);
    }
    // switch(ntohs(eth->h_proto)){
    //     case 2048:
    //         // struct iphdr *ip_hdr_ptr = (struct iphdr*)(buffer + sizeof(struct ethhdr));
    //         print_IP_header(buffer);
    //         break;
    // }
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
        print_packet(buffer);
        printf("\n=================================================\n");
        
    }
    return 0;
}
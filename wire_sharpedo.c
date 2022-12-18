#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <net/ethernet.h>
#include <netinet/ether.h>

void print_hex_protocol(int dec_protocol){
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
    printf("Protocol not present in switch case:  ");
    for(int i = index; i >= 0; i--){
        printf("%c", hex[i]);
    }    
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
            print_hex_protocol(dec_protocol); 
    }
}

int main(){
    // htons(ETH_P_ALL) => all protocols
    int sock_raw = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
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
        } else{
            printf("able to receive data\n");
            
        }
    
        struct ethhdr *eth = (struct ethhdr*)buffer;
        printf("\n Ethernet Header \n");
        printf("\t| Source address: %.2X:%.2X:%.2X:%.2X:%.2X:%.2X\n", eth->h_source[0],eth->h_source[1],eth->h_source[2],eth->h_source[3],eth->h_source[4],eth->h_source[5]);
        printf("\t| Destination address: %.2X:%.2X:%.2X:%.2X:%.2X:%.2X\n", eth->h_dest[0],eth->h_dest[1],eth->h_dest[2],eth->h_dest[3],eth->h_dest[4],eth->h_dest[5]);
        printf("\t| Protocol: %s\n", get_ether_type(ntohs(eth->h_proto)));
        // printf("|-Source Address : %.2X-%.2X-%.2X-%.2X-%.2X-%.2X\n", eth->h_source[0],eth->h_source[1],eth->h_source[2],eth->h_source[3],eth->h_source[4],eth->h_source[5]);
    }
    


    return 0;
}
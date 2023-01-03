#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <net/ethernet.h>
#include <netinet/ether.h>
#include <arpa/inet.h>
#include <net/if.h>
#include <ifaddrs.h>

void find_devices(){

    struct ifaddrs *addr;
    char ip_addr[INET_ADDRSTRLEN];
    char ip_netmask[INET_ADDRSTRLEN];
    char ip_broadcast[INET_ADDRSTRLEN];
    char ip6_addr[INET6_ADDRSTRLEN];
    char ip6_netmask[INET6_ADDRSTRLEN];
    char ip6_broadcast[INET6_ADDRSTRLEN];


    printf("============================================All network Interface============================================\n");
    getifaddrs(&addr);
    while(addr){
        if(addr->ifa_addr){
            if(addr->ifa_addr->sa_family == AF_PACKET){
                printf("Interface: %s\n", addr->ifa_name);
            }
        }
        addr = addr->ifa_next;
    }
    printf("\n");
    freeifaddrs(addr); 
    printf("============================================ IPv6 Version ============================================ \n");
    getifaddrs(&addr);
    while(addr){
        if(addr->ifa_addr){
            if(addr->ifa_addr->sa_family == AF_INET){
                printf("Name: %s\n", addr->ifa_name);
                inet_ntop(AF_INET, &((struct sockaddr_in *)addr->ifa_addr)->sin_addr, ip_addr, INET_ADDRSTRLEN );
                printf("IPv4 Address: %s", ip_addr);
                inet_ntop(AF_INET, &((struct sockaddr_in *)addr->ifa_netmask)->sin_addr, ip_netmask, INET_ADDRSTRLEN);
                printf("\tIPv4 Netmask: %s\n\n", ip_netmask);
            }
        }
        addr = addr->ifa_next;
    }
    freeifaddrs(addr); 
    getifaddrs(&addr);
    printf("============================================ IPv6 Version ============================================ \n");
    while(addr){
        if(addr->ifa_addr){
            if(addr->ifa_addr->sa_family == AF_INET6){
                printf("Name: %s\n", addr->ifa_name);
                inet_ntop(AF_INET6, &((struct sockaddr_in6 *)addr->ifa_addr)->sin6_addr, ip6_addr, INET6_ADDRSTRLEN);
                printf("IPv6 Address: %s", ip6_addr);
                inet_ntop(AF_INET6, &((struct sockaddr_in6 *)addr->ifa_netmask)->sin6_addr, ip6_netmask, INET6_ADDRSTRLEN);
                printf("\tIPv6 Netmask: %s\n\n", ip6_netmask);
            }
        }
        addr = addr->ifa_next;
    }
    freeifaddrs(addr); 
}

int main(){
    find_devices();
    return 1;
}

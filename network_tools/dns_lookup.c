#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <netinet/in.h>

/* 
This program works like a simple DNS lookup 
*/

int main(int argc, char *argv[]){
    struct addrinfo addrs;
    struct addrinfo *res;
    int status;
    char ipstr[INET6_ADDRSTRLEN];

    memset(&addrs, 0, sizeof(addrs)); // making sure the addrinfo struct is empty
    addrs.ai_family = AF_UNSPEC; // we accept both IPv4 and IPv6
    addrs.ai_socktype = SOCK_STREAM;

    // getaddrinfo translates host name into address
    status = getaddrinfo(argv[1], NULL, &addrs, &res);

    if(status != 0){
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(status));
        return 2;
    }
    // printf("getaddrinfo return code: %d\n", status);
    printf("IP adress for %s:\n\n", argv[1]);
    
    // Iterate through the returned linked-list and get address out of it
    while(res){
        void *addr;
        char *ipver;

        // get the pointer to the address itself
        // different fields in IPv4 and IPv6
        if(res->ai_family == AF_INET){
            struct sockaddr_in *ipv4 = (struct sockaddr_in *)res->ai_addr;
            addr = &(ipv4->sin_addr);
            ipver = "IPv4";
        } else{
            struct sockaddr_in6 *ipv6 = (struct sockaddr_in6 *)res->ai_addr;
            addr = &(ipv6->sin6_addr);
            ipver = "IPv6";
        }
        printf("IP address");
        // convert the IP to a string and print it
        inet_ntop(res->ai_family, addr, ipstr, sizeof(ipstr));
        printf("%s: %s\n", ipver, ipstr);
        res = res->ai_next;
    }

    freeaddrinfo(res);
    return 0;

}
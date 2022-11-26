#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>



int main(){
    int sock_raw = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);
    int test_sock = socket(AF_INET, SOCK_STREAM, 0);
    printf("%d\n", test_sock);
    printf("%d\n", sock_raw);
    if(sock_raw == -1){
        printf("failed to creat socket");
    }else{
        printf("socket created");
    }
    return 0;
}
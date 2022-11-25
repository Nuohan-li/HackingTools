#include <stdio.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>



int main(){
    int sock_raw = socket(AF_PACKET, SOCK_RAW, IPPROTO_TCP);
    return 0;
}
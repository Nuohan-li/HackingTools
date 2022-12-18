#include <stdio.h>

char* test(){
    return "IPv4";
}

int main(){
    char string[100] = "IPv4";
    printf("%s", test());
    return 0;
}
#include <stdio.h>

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

int main(){
    int proto = 34958;
    char hex[4];
    // print_hex_protocol(hex, proto);
    print_hex_protocol(proto);
    return 0;
}
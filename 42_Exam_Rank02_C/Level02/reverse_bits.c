#include <stdio.h>

unsigned char	reverse_bits(unsigned char octet){
    unsigned char result;
    int i;

    i=8;
    while(i-->0){
        result=result*2+(octet%2);
        octet=octet/2;
    }
    return result;
}


int	main(void)
{
	unsigned char	resultado;
	unsigned char	octet;

	octet = 0x42;
	resultado = reverse_bits(octet);
	printf("Octeto original: 0x%X\n", octet);
	printf("Octeto con bits intercambiados: 0x%X\n", resultado);
	return (0);
}
    
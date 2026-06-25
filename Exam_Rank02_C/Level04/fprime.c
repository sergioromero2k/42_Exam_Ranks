#include <stdio.h>
#include <stdlib.h>

void	fprime(int nbr)
{
	int	div;

	div = 2;
	if (nbr == 1)
	{
		printf("1");
		return ;
	}
	while (nbr > 1)
	{
		if (nbr % div == 0)
		{
			printf("%d", div);
			nbr /= div;
			if (nbr > 1)
				printf("*");
		}
		else
			div++;
	}
}

int	main(int argc, char **argv)
{
	if (argc == 2)
		fprime(atoi(argv[1]));
	printf("\n");
	return (0);
}

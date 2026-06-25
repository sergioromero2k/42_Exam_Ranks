#include "unistd.h"

void	put_num(int n)
{
	char	*num;

	num = "0123456789";
	if (n > 9)
		put_num(n / 10);
	write(1, &num[n % 10], 1);
}

void	fizzbuzz(int num)
{
	int	i;

	i = 1;
	while (i <= num)
	{
		if (i % 3 == 0 && i % 5 == 0)
			write(1, "fizzbuzz", 8);
		else if (i % 5 == 0)
			write(1, "buzz", 4);
		else if (i % 3 == 0)
			write(1, "fizz", 4);
		else
			put_num(i);
		write(1, "\n", 1);
		i++;
	}
}
int	main(void)
{
	fizzbuzz(100);
	return (0);
}

#include <unistd.h>

/* void	ft_putnbr(int n)
{
	int				digits[10];
	int				i;
	unsigned int	num;
	char			c;

	i = 0;
	if (n == 0)
	{
		write(1, "0", 1);
		return ;
	}
	if (n < 0)
	{
		write(1, "-", 1);
		num = -n;
	}
	else
		num = n;
	while (num > 0)
	{
		digits[i++] = (num % 10) + '0';
		num /= 10;
	}
	i--;
	while (i >= 0)
		write(1, &digits[i--], 1);
} */


void	ft_putnbr(int n)
{
    char c;
    
	if (n >= 10)
		ft_putnbr(n / 10);
	c = (n % 10) + '0';
	write(1, &c, 1);
}
int	main(int argc, char **argv)
{
	(void)argv;
	ft_putnbr(argc - 1);
	write(1, "\n", 1);
	return (0);
}

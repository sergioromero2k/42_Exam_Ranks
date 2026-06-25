#include <unistd.h>

void	ft_putnbr(int n)
{
	char	c;

	if (n >= 10)
		ft_putnbr(n / 10);
	c = n % 10 + '0';
	write(1, &c, 1);
}
int	ft_atoi(char *str)
{
	int	sign;
	int	result;
	int	i;

	i = 0;
	sign = 1;
	if (!str[i])
		return (0);
	while (str[i] == '\t' || str[i] == '\n' || str[i] == '\v' || str[i] == '\f'
		|| str[i] == '\r' || str[i] == ' ')
		i++;
	if (str[i] == '-')
		return (0);
	result = 0;
	while (str[i] >= '0' && str[i] <= '9')
	{
		result = result * 10 + (str[i] - '0');
		i++;
	}
	return (sign * result);
}
void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		write(1, &str[i], 1);
		i++;
	}
}
void	tab_mult(int mult)
{
	int	i;

	i = 1;
	while (i < 10 && mult != -mult)
	{
		ft_putnbr(i);
		ft_putstr(" x ");
		ft_putnbr(mult);
		ft_putstr(" = ");
		ft_putnbr(i * mult);
		ft_putstr("\n");
		i++;
	}
}

int	main(int argc, char **argv)
{
	if (argc == 2)
		tab_mult(ft_atoi(argv[1]));
	write(1, "\n", 1);
}

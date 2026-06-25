#include <stdio.h>

int	ft_atoi_base(const char *str, int base)
{
	int	result;
	int	sign;
	int	i;
	int	value;

	result = 0;
	sign = 1;
	i = 0;
	if (base < 2 || base > 16)
		return (0);
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i] != '\0')
	{
		if (str[i] >= '0' && str[i] <= '9')
			value = str[i] - '0';
		else if (str[i] >= 'a' && str[i] <= 'f')
			value = str[i] - 'a' + 10;
		else if (str[i] >= 'A' && str[i] <= 'F')
			value = str[i] - 'A' + 10;
		else
			break ;
		if (value >= base)
			break ;
		result = result * base + value;
		i++;
	}
	return (result * sign);
}

int	main(void)
{
	printf("%d\n", ft_atoi_base("1010", 2)); // 10
	printf("%d\n", ft_atoi_base("FF", 16));  // 255
	printf("%d\n", ft_atoi_base("-1A", 16)); // -26
	printf("%d\n", ft_atoi_base("777", 8));  // 511
	return (0);
}
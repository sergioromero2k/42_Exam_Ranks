// #include <stdio.h>

// Method 1
/* int	is_power_of_2(unsigned int n)
{
	if (n == 0)
		return (0);
	while (n > 1)
	{
		if (n % 2 != 0)
			return (0);
		n = n / 2;
	}
	return (1);
} */

// Method 2
int	is_power_of_2(unsigned int n)
{
	if (n == 0)
		return (0);
	return (((n) & (n - 1)) == 0);
}
/* 
int	main(void)
{
	int	num;

	num = is_power_of_2(16);
	printf("%d", num);
}
 */
/* unsigned int	lcm(unsigned int a, unsigned int b)
{
	int	x;
	int	y;
	int	tmp;
	int	multiple;

	if (a == 0 || b == 0)
		return (0);
	x = a;
	y = b;
	while (y == 0)
	{
		tmp = y;
		y = x % y;
		x = tmp;
	}
	return ((a / x) * y);
} */

unsigned int	lcm(unsigned int a, unsigned int b)
{
    unsigned int  multiple;

    multiple=0;
	if (a == 0 || b == 0)
		return (0);
	if (a > b)
		multiple = a;
	else
		multiple = b;
	while ((1))
	{
		if (multiple % a == 0 && multiple % b == 0)
			return (multiple);
		multiple++;
	}
}

// #include <stdio.h>

// int	main(void)
// {
// 	printf("%d\n", lcm(42, 15));
// 	return (0);
// }
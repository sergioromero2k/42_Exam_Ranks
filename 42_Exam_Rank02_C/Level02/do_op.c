#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

int	do_op(int a, char op, int b)
{
	if (op == '+')
		return (a + b);
	else if (op == '-')
		return (a - b);
	else if (op == '*')
		return (a * b);
	else if (op == '/')
	{
		if (b != 0)
			return (a / b);
	}
	else if (op == '%')
	{
		if (b != 0)
			return (a % b);
	}
	return (0);
}
int	main(int argc, char **argv)
{
	int	a;
	int	b;

	if (argc == 4)
	{
		a = atoi(argv[1]);
		b = atoi(argv[3]);
		printf("%d", do_op(a, argv[2][0], b));
	}
	printf("\n");
}

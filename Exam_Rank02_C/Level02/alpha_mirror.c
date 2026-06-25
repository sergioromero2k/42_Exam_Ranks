#include <unistd.h>

char	*alpha_mirror(char *str)
{
	int		i;
	char	mirror;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
			mirror = 'Z' - (str[i] - 'A');
		else if (str[i] >= 'a' && str[i] <= 'z')
			mirror = 'z' - (str[i] - 'a');
		else
			mirror = str[i];
		write(1, &mirror, 1);
		i++;
	}
	return (str);
}
int	main(int argc, char **argv)
{
	if (argc == 2)
		alpha_mirror(argv[1]);
	write(1, "\n", 1);
	return (0);
}

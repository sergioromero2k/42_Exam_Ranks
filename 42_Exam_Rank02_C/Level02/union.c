#include <unistd.h>

void	ft_union(char *str1, char *str2)
{
	char	seen[256] = {0};
	int		i;

	i = 0;
	while (str1[i])
	{
		if (!seen[(unsigned char)str1[i]])
		{
			seen[(unsigned char)str1[i]] = 1;
			write(1, &str1[i], 1);
		}
		i++;
	}
	i = 0;
	while (str2[i])
	{
		if (!seen[(unsigned char)str2[i]])
		{
			seen[(unsigned char)str2[i]] = 1;
			write(1, &str2[i], 1);
		}
		i++;
	}
}

int	main(int argc, char **argv)
{
	if (argc == 3)
		ft_union(argv[1], argv[2]);
	write(1, "\n", 1);
	return (0);
}

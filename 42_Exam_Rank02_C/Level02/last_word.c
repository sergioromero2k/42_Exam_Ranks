#include <unistd.h>

void	last_word(char *str)
{
	int	i;
	int	start;
	int	end;

	i = 0;
	while (str[i] != '\0')
		i++;
	end = i - 1;
	while (end >= 0 && (str[end] == ' ' || str[end] == '\t'))
		end--;
	if (end < 0)
		return ;
	start = end;
	while (start >= 0 && str[start] != ' ' && str[start] != '\t')
		start--;
	start++;
	while (start <= end)
	{
		write(1, &str[start], 1);
		start++;
	}
}
int	main(int argc, char **argv)
{
	if (argc == 2)
		last_word(argv[1]);
	write(1, "\n", 1);
	return (0);
}

#include <unistd.h>

void	rstr_capitalizer(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
        // Primero pasamos todo a minúsculas si es una letra
		if (str[i] >= 'A' && str[i] <= 'Z')
			str[i] += 32;
        // Si es una letra minúscula Y el siguiente caracter es un separador o fin de cadena...
		if (str[i] >= 'a' && str[i] <= 'z' && (str[i + 1] == ' ' || str[i
				+ 1] == '\t' || str[i + 1] == '\0'))
			str[i] -= 32;
		write(1, &str[i], 1);
		i++;
	}
}
int	main(int argc, char **argv)
{
	int	i;

	if (argc == 1)
		write(1, "\n", 1);
	else
	{
		i = 1;
		while (i < argc)
		{
			rstr_capitalizer(argv[i]);
			write(1, "\n", 1);
			i++;
		}
	}
	return (0);
}

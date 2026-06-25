#include <stdio.h>

size_t	ft_strcspn(const char *s, const char *reject)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	while (s[i] != '\0')
	{
		while (reject[j] != '\0')
		{
			if (s[i] == reject[j])
				return (i);
			j++;
		}
		j = 0;
		i++;
	}
	return (i);
}
/* int	main(void)
{
	char	clave[] = "user1234@gmail.com";
	char	filtros[] = "0123456789@";
	size_t	indice;

	indice = ft_strcspn(clave, filtros);
	printf("El nombre de usuario puro tiene %zu caracteres.\n", indice);
	return (0);
} */

// #include <stdio.h>

char	*ft_strpbrk(const char *s1, const char *s2)
{
	int	i;

	if (!s1 || !s2)
		return (0);
	while (*s1 != '\0')
	{
		i = 0;
		while (s2[i] != '\0')
		{
			if (*s1 == s2[i])
				return ((char *)s1);
			i++;
		}
		s1++;
	}
	return (0);
}
// int	main(void)
// {
// 	char	clave[] = "Hola mundo";
// 	char	filtros[] = "a";
// 	char	*posicion;

// 	posicion = ft_strpbrk(clave, filtros);
// 	printf("Puntero: %s\n", posicion);
// 	return (0);
// }

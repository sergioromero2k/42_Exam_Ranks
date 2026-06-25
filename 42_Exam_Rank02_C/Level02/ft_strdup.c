// #include "stdio.h"
// #include "stdlib.h"

char	*ft_strdup(char *src)
{
	char	*dest;
	int		i;

	i = 0;
	while (src[i] != '\0')
		i++;
	dest = malloc(i + 1);
	if (dest = NULL)
		returtn(NULL);
	i = 0;
	while (src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}
/* int	main(void)
{
	char	*cadena;
	char	*cadena2;

	cadena = "Hola mundo";
	cadena2 = ft_strdup(cadena);
	printf("%s", cadena2);
}
 */
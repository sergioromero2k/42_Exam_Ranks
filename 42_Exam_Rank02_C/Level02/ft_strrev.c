// #include <stdio.h>
// #include <stdlib.h>

char	*ft_strrev(char *str)
{
	int		i;
	int		j;
	char	*rev;

	i = 0;
	while (str[i] != '\0')
		i++;
	rev = malloc(i + 1);
	if (!rev)
		return (NULL);
	j = 0;
	i--;
	while (i >= 0)
	{
		rev[j] = str[i];
		j++;
		i--;
	}
	rev[j] = '\0';
	return (rev);
}

/* int	main(void)
{
	char	*str;
	char	*str_rev;

	str = "hola mundo";
	str_rev = ft_strrev(str);
	printf("%s", str_rev);
	return (0);
}
 */
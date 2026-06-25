#include "stdlib.h"

char	**ft_split(char *str)
{
	int		j;
	int		i;
	int		k;
	char	**split;

	j = 0;
	i = 0;
	split = malloc(sizeof(char *) * 256);
	if (!split)
		return (NULL);
	while (str[i])
	{
		while (str[i] && (str[i] == '\t' || str[i] == ' ' || str[i] == '\n'))
			i++;
		if (str[i])
		{
			k = 0;
			split[j] = malloc(sizeof(char) * 4096);
			while (str[i] && !(str[i] == '\t' || str[i] == ' '
					|| str[i] == '\n'))
				split[j][k++] = str[i++];
			split[j++][k] = '\0';
		}
	}
	split[j] = NULL;
	return (split);
}

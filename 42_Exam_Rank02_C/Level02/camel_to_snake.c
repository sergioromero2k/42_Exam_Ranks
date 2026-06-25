/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   camel_to_snake.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sergio-alejandro <sergio-alejandro@stud    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 17:56:42 by sergio-alej       #+#    #+#             */
/*   Updated: 2025/12/25 18:33:41 by sergio-alej      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stdlib.h"
#include "unistd.h"

int	ft_strlen(char *str)
{
	int	i;
	int	len;

	i = 0;
	len = 0;
	while (str[i] != '\0')
	{
		if (str[i] >= 'A' && str[i] <= 'Z' && i != 0)
			len += 2;
		else
			len++;
		i++;
	}
	return (len);
}

char	*camel_to_snake(char *str)
{
	int		i;
	int		j;
	char	*snake;
	int		len;

	i = 0;
	j = 0;
	len = ft_strlen(str);
	snake = malloc(len + 1);
	if (!snake)
		return (NULL);
	while (str[i])
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
		{
			if (i != 0)
				snake[j++] = '_';
			snake[j++] = (str[i] + 32);
		}
		else
			snake[j++] = str[i];
		i++;
	}
	snake[j] = '\0';
	return (snake);
}

int	main(int argc, char **argv)
{
	int	len;

	len = ft_strlen(argv[1]);
	if (argc == 2)
		write(1, camel_to_snake(argv[1]), len);
	write(1, "\n", 1);
	return (0);
}

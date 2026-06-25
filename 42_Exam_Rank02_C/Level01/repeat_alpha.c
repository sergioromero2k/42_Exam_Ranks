/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   repeat_alpha.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sergio-alejandro <sergio-alejandro@stud    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 20:12:16 by sergio-alej       #+#    #+#             */
/*   Updated: 2025/12/22 20:35:11 by sergio-alej      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c, int num)
{
	while (num > 0)
	{
		write(1, &c, 1);
		--num;
	}
}

void	repeat_alpha(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
		{
			ft_putchar(str[i], str[i] - 'A' + 1);
		}
		else if (str[i] >= 'a' && str[i] <= 'z')
		{
			ft_putchar(str[i], str[i] - 'a' + 1);
		}
		else
		{
			ft_putchar(str[i], 1);
		}
		i++;
	}
}
int	main(int argc, char **argv)
{
	if (argc == 2)
		repeat_alpha(argv[1]);
	write(1, "\n", 1);
	return (0);
}

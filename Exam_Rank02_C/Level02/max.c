/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   max.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sergio-alejandro <sergio-alejandro@stud    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 18:38:08 by sergio-alej       #+#    #+#             */
/*   Updated: 2025/12/25 18:57:19 by sergio-alej      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stdio.h"

int	max(int *tab, unsigned int len)
{
	int				max;
	unsigned int	i;

	i = 0;
	if (!tab || len == 0)
		return (0);
	max = tab[0];
	while (i < len)
	{
		if (tab[i] > max)
			max = tab[i];
		i++;
	}
	return (max);
}
/* int	main(void)
{
	int tab[] = {9, 0, 1, 4, 4, 8, 12};

	printf("%d", max(tab, 7));
	return (0);
} */
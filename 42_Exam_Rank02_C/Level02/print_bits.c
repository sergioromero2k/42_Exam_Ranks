/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_bits.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sergio-alejandro <sergio-alejandro@stud    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 18:55:59 by sergio-alej       #+#    #+#             */
/*   Updated: 2026/01/13 08:57:36 by sergio-alej      ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

void	print_bits(unsigned char octet){
	unsigned char result;
	int i;

	i=8;
	while((i--)>0)
	{
		result=(octet>>i&1)+'0';
		write(1,&result,1);
	}

}
int	main(void)
{
	print_bits(0x42);
}

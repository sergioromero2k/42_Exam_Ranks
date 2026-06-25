#include "ft_list.h"
#include <stdio.h>
#include <stdlib.h>

int		ft_list_size(t_list *begin_list);

t_list	*create_node(void *data)
{
	t_list	*node;

	node = malloc(sizeof(t_list));
	if (!node)
		return (NULL);
	node->data = data;
	node->next = NULL;
	return (node);
}

int	main(void)
{
	t_list	*n1;
	t_list	*n2;
	t_list	*n3;

	n1 = create_node("Hola");
	n2 = create_node("Mundo");
	n3 = create_node("!");
	n1->next = n2;
	n2->next = n3;
	printf("Tamaño de la lista: %d\n", ft_list_size(n1));
	free(n1);
	free(n2);
	free(n3);
	return (0);
}
// cc -Wall -Werror -Wextra ft_list.h ft_list_size.c main.c -o main.o

#include "ft_list.h"

void	ft_list_foreach(t_list *begin_list, void (*f)(void *))
{
	t_list	*list_ptr;

	list_ptr = begin_list;
	while (list_ptr)
	{
		(*f)(list_ptr->data);
		list_ptr = list_ptr->next;
	}
}

/* void	print_int(void *data)
{
	int	*n;

	n = (int *)data;
	printf("%d\n", *n);
}
int	main(void)
{
	void (*f)(void *);

	int x;
	x = 42;
	f = print_int;
    f(&x);
    return 0;
} */
#include <stdlib.h>

int	*ft_range(int start, int end)
{
	int	len;
	int	*num;
	int	i;

	if (start >= end)
		len = start - end + 1;
	else
		len = end - start + 1;
	num = malloc(sizeof(int) * (len));
	if (!num)
		return (0);
	i = 0;
	while (i < len)
	{
		if (start <= end)
			num[i++] = start++;
		else
			num[i++] = start--;
	}
	return (num);
}

// int	main(int argc, char **argv)
// {
// 	int	*arr;
// 	int	len;
// 	int	i;

// 	if (argc == 3)
// 	{
// 		arr = ft_range(atoi(argv[1]), atoi(argv[2]));
// 		len = abs((atoi(argv[1]) - atoi(argv[2]))) + 1;
// 		i = 0;
// 		while (i < len)
// 			printf("%d, ", arr[i++]);
// 		free(arr);
// 	}
// 	printf("\n");
// 	return (0);
// }
// ./a.out 1 3
// ./a.out -1 2
// ./a.out 0 0
// ./a.out 0 -3

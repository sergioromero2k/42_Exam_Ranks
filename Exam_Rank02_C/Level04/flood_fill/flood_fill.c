typedef struct s_point
{
	int	x;
	int	y;
}		t_point;

void	flood_fill(char **tab, t_point size, t_point begin)
{
	char c;
	t_point p;

	c = tab[begin.y][begin.x];
	tab[begin.y][begin.x] = 'F';

	if (begin.y > 0 && tab[begin.y - 1][begin.x] == c)
	{
		p.x = begin.x;
		p.y = begin.y - 1;
		flood_fill(tab, size, p);
	}
	if (begin.y < size.y - 1 && tab[begin.y + 1][begin.x] == c)
	{
		p.x = begin.x;
		p.y = begin.y + 1;
		flood_fill(tab, size, p);
	}
	if (begin.x > 0 && tab[begin.y][begin.x - 1] == c)
	{
		p.x = begin.x - 1;
		p.y = begin.y;
		flood_fill(tab, size, p);
	}
	if (begin.x < size.x - 1 && tab[begin.y][begin.x + 1] == c)
	{
		p.x = begin.x + 1;
		p.y = begin.y;
		flood_fill(tab, size, p);
	}
}

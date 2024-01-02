#include "lists.h"

/**
 * check_cycle - checks if a linkedlist has a cycle in it
 * @list: The linkedlist to check for.
 *
 * Return: If no cycle, return 0. If cycle is found, return 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}

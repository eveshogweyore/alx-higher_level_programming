#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: Pointer to the first node.
 *
 * Return: On success, 1. On failure, 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head, *prev1, *prev2;
	int length = 0, start_at = 0, stop_at;

	while (curr)
	{
		length++;
		curr = curr->next;
	}

	if (length % 2 == 0)
		stop_at = length / 2;
	else
		stop_at = (length / 2) + 1;

	curr = *head;
	while (curr)
	{
		if (start_at < stop_at)
		{
			prev1 = curr;
			curr = curr->next;
			if (start_at == 0)
				prev1->next = NULL;
			else
				prev1->next = prev2;
			prev2 = prev1;
			start_at++;
		}
		else
		{
			if (prev1 == prev2 && length % 2 != 0)
				prev2 = prev2->next;
			if (curr->n != prev2->n)
				return (0);
			prev2 = prev2->next;
			curr = curr->next;
		}
	}
	return (1);
}

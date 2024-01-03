#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to first element in linked list.
 * @number: The number to be inserted into the linked list.
 *
 * Return: On success, address of new node. On failure, NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *prev_node = NULL;
	listint_t *current_node = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}

	while (current_node != NULL)
	{
		if (current_node->n > number)
		{
			new_node->next = current_node;
			if (prev_node)
				prev_node->next = new_node;
			else
				*head = new_node;
			return (new_node);
		}

		prev_node = current_node;
		current_node = current_node->next;
	}

	return (NULL);
}

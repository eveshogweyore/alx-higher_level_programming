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
	listint_t *new_node = NULL;
	listint_t *current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current != NULL)
	{
		if (current->next == NULL || current->next->n > number)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}

		current = current->next;
	}

	return (NULL);
}

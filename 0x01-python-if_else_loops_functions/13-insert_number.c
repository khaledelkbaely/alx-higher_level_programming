#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert node in a sorted singly linked lists
 *
 * @head: pointer to the address of the first node
 * @number: integer
 *
 * Return: the address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *p, *n;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	n = *head;
	p = NULL;
	while (n)
	{
		if (n->next == NULL || n->n > number)
		{
			new->next = n;
			if (p)
				p->next = new;
			else
				*head = new;
			break;
		}

		p = n;
		n = n->next;
	}
	return (new);
}

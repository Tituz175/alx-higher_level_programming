#include "lists.h"

/**
 * insert_node -> this function add a number to
 * a sorted list.
 * @head: the head of the given list
 * @number: the number to be added
 * Return: the node address of the number
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (current_node == NULL || current_node->n >= number)
	{
		*head = new_node;
		new_node->next = current_node;
		return (new_node);
	}

	while (current_node && current_node->next && number > current_node->n)
		current_node = current_node->next;

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}

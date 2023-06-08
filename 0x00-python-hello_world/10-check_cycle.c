#include "lists.h"
/**
 * check_cycle -> this function checks maybe
 * a linked list is a cycle
 * @list: the given linked list
 * Return: 1 if the linked list is a cycle
 * else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *first_next, *second_next;

	if (list == NULL || list->next == NULL)
		return (0);

	first_next = list->next;
	second_next = list->next->next;

	while (first_next && second_next && second_next->next)
	{
		if (first_next == second_next)
			return (1);
		first_next = first_next->next;
		second_next = second_next->next->next;
	}
	return (0);
}

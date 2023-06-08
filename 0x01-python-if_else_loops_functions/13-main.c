#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 10);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 0);

    print_listint(head);

    free_listint(head);

    return (0);
}

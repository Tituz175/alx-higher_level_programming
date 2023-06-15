#include <stdio.h>
#include "Python.h"

/**
 * print_python_list -> this function print the
 * details of the give list. the size, allocated
 * size and the data type of the list content.
 * @p: this is the given list
 * Return: void
 */

void print_python_list(PyObject *p)
{
	int count;

	PyListObject *l = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", l->ob_base.ob_size);
	printf("[*] Allocated = %li\n", l->allocated);
	for (count = 0; count < l->ob_base.ob_size; count++)
	{
		printf("Element %i: %s\n", count, l->ob_item[count]->ob_type->tp_name);
	}
}

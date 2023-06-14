#include <stdio.h>
#include "Python.h"

void print_list(PyObject *list)
{
	int count;
	PyListObject *l;
	l = (PyListObject *) list;
	printf("Hello World\n");
	printf("[*] Size of the Python List = %ld\n", l->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", l->allocated);
	for (count = 0; count < l->ob_base.ob_size; count++)
	{
		printf("Element %d: %s\n", count, l->ob_item[count]->ob_type->tp_name);
	}
}

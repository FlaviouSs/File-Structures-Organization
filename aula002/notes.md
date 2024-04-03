# MALLOC

The malloc function from *stdlib.h* receives an integer number as a parameter. This number represents the amount of bytes that we will allocate in main memory.

It returns a generic pointer *(void)* to access the memory allocated. This pointer can be converted explicitly or implicitly to a desired pointer type. If the memory was not successfully allocated, it will return a *NULL* value.

#### Dinamic Memory Alocation

Dynamic memory allocation is a programming concept that refers to the allocation and deallocation of memory during runtime. Unlike static memory allocation, where memory is allocated at compile-time and remains fixed throughout the program's execution, dynamic memory allocation allows the program to request memory from the operating system as needed and release it when it's no longer required.

#### How to use it:

```C
cepIndice *v = malloc(qntRegistros * sizeof(cepIndice));
```

# QSORT

The qsort function in C is used to sort an array of elements. The name *"qsort"* comes from *"Quick Sort"*, a widely-used sorting algorithm behind the implementation of this function in many C standard libraries.

#### How to use it:

```C
qsort(v, qntRegistros, sizeof(cepIndice), compara);
```

#### Parameters

```C
void qsort(void *base, size_t amount, size_t size, comparingFunction);
```

- base: It is a pointer to the array you want to sort. Since qsort is a generic function, it uses a void * pointer so that it can sort arrays of any data type.

- amount: It is the number of elements in the array you want to sort.

- size: It is the size, in bytes, of each element in the array.

- comparingFunction:  It is a pointer to a comparison function that is called to compare two elements. This comparison function should return a negative value if the first element is less than the second, a positive value if the first element is greater than the second, and zero if the two elements are equal.The typical signature for this comparison function is int ***cmp(const void *a, const void *b)***.

Example of comparing function:

```C
int compara(const void *cep1, const void *cep2)
{
	return strncmp(((cepIndice*)cep1)->cep,((cepIndice*)cep2)->cep,8);
}
```

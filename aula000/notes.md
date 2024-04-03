# Definitions

A file is a sequence of data, persistent non-volatile.

The operation of bringing data from the hard drive to RAM memory, to consume it, is too expensive. Our goal is to reduce this operation time during the acess of the hard drive. 

# FILE

It's a data type used to manipulate files. It's defined in the standard library '*<stdio.h>*' and controls input and output operations via a file pointer. Each operating system has its own implementation of the FILE structure.

#### How to use it:

```C
FILE *pointerFile;
```

# FPRINTF

It's a function that allows us to write with formatting in a file/stream. It's similar to the function 'printf', but instead of printing to the default output, it prints to the file/stream.

#### How to use it:

We usually use it to print an error message when we open a file.

```C
if(argc != 3)
	{
		fprintf(stderr,"Erro na chamada do comando.\n");
		fprintf(stderr,"Uso: %s [ARQUIVO ORIGEM] [ARQUIVO DESTINO].\n", argv[0]);
		return 1;
	}
```

#### Parameters

```C
fprintf(FILE *stream, "string formatted", ...);
```

# FREAD

It's a function used to read data from a file. It works with a random access file, so we need to read records/registers. The function reads a record from a file and stores it in a buffer, then returns the number of records read.

#### How to use it:

```C
qtd = fread(buffer,1,TAMANHO,entrada);
	while(qtd > 0)
	{
		fwrite(buffer,1,qtd,saida);
		qtd = fread(buffer,1,TAMANHO,entrada);
	}
```

#### Parameters

```C
fread(buffer, size_of_record, amount_of_records, FILE *stream);
```

buffer -> Structure that it'll store the data read

# FWRITE

As you can imagine, it's used to write in a random acess file.

#### How to use it:

```C
qtd = fread(buffer,1,TAMANHO,entrada);
	while(qtd > 0)
	{
		fwrite(buffer,1,qtd,saida);
		qtd = fread(buffer,1,TAMANHO,entrada);
	}
```

#### Parameters

```C
fwrite(buffer, size, amount, FILE *stream);
```


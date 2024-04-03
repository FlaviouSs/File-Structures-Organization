# FSEEK

    It's a function that allows us to place the file position indicaitor where we wish.

#### How to use it:

```C
fseek(f, meio * tamanhoRegistro, SEEK_SET);
```
#### Parameters

```C
fseek(FILE *stream, long offset, origin);
```

Origin -> The reference position of where the offset will be applied.

- SEEK_SET: Defines the beginning of the file as a reference point.
- SEEK_CUR: Defines the current file position indicator as a reference point.
- SEEK_END: Defines the end of the file as a reference point.

Offset -> The displacement that will be applied to the file position indicator. It can be positive, negative, or zero.

# FTEEL

It's a function that returns the actual file position indicaitor.

#### Parameters and How to use it:

```C
long position = ftell(FILE *stream);
```


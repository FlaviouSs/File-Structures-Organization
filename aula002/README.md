# Instructions

1. Unzip "cep.zip" file, it'll generate a file called "cep.dat".
2. Compile "guardaIndiceRegistro.c", pass "cep.dat" as a argument when you call it's executable command. It'll generate a file called "indice.dat"
3. Compile "BuscaCEPIndice.c", pass a CEP as argument to search for it in "indice.dat", the output of the program will tell you if the CEP was found or not.

# Explanation guardaIndiceRegistro.c

Recives "cep.dat" as argument. It calculates how many registers are in cep.dat, after its malloc memory in main memory (Inside an array, v[]). Reads cep.dat and writes the CEP of each register with its index. Sort the array and writes it in a output file called "indice.dat".

# Explanation BuscaCEPIndice.c

Recives a CEP as argument, uses Binary Search Algorithm to find it. Outputs the result in the terminal.


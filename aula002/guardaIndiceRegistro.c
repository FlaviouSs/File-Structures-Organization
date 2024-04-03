#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*

Flavio Alecio de Morais Santos
Vinicius Saidy do Amaral de Lima
Yuri Braga da Silva

*/


struct _cepIndice{
    char cep[8];
    int indice;
};
typedef struct _cepIndice cepIndice;

struct _Endereco
{
	char logradouro[72];
	char bairro[72];
	char cidade[72];
	char uf[72];
	char sigla[2];
	char cep[8];
	char lixo[2]; // Ao Espaço no final da linha + quebra de linha
};
typedef struct _Endereco Endereco;

int compara(const void *cep1, const void *cep2)
{
	return strncmp(((cepIndice*)cep1)->cep,((cepIndice*)cep2)->cep,8);
}

int main(int argc, char**argv){

    FILE *entrada, *saida;
    Endereco buffer;
    long tamanhoArquivo;
    int qntRegistros;
    int aux;
    
    if(argc != 2){
        fprintf(stderr, "USO: %s [ARQUIVO_CEPS]", argv[0]);
        return 1;
    }

    entrada = fopen(argv[1], "rb");
    if(!entrada){
        fprintf(stderr, "Não foi possível abrir o arquivo");
        return 1;
    }

    saida = fopen("indice.dat", "wb");
    fseek(entrada, 0, SEEK_END);
    tamanhoArquivo = ftell(entrada); // Descobrimos o tamanho do arquivo
    rewind(entrada);

    qntRegistros = tamanhoArquivo / sizeof(Endereco); // Descobrimos a quantidade de registros no arquivo

    cepIndice *v = malloc(qntRegistros * sizeof(cepIndice));

    aux = fread(&buffer, sizeof(Endereco), 1, entrada);
    int i = 0;
    while(aux > 0){
        strncpy(v[i].cep, buffer.cep, 8);
        v[i].indice = i;
        i++;
        aux = fread(&buffer, sizeof(Endereco), 1, entrada);
    }

    fclose(entrada);

    qsort(v, qntRegistros, sizeof(cepIndice), compara);

    fwrite(v, sizeof(v), qntRegistros, saida);

    free(v);
    fclose(saida);
    return 0;
}

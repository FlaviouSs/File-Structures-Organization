#include <stdio.h>
#include <string.h>

/*

Flavio Alecio de Morais Santos
Vinicius Saidy do Amaral de Lima
Yuri Braga Silva

*/

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

int main(int argc, char** argv){

    FILE *f;
	Endereco buffer, procurado;
    int aux;

    printf("Digite o CEP procurado: ");
    scanf("%s", procurado.cep);


    if(argc != 2)
	{
		fprintf(stderr, "USO: %s [CEP]", argv[0]);
		return 1;
	}

    long tamanhoArquivo, posicao, inicio, fim, meio, tamanhoRegistro;
    int qnt_registros, iteracoes = 0;

    f = fopen(argv[1], "rb");
    if(!f){
        fprintf(stderr, "Impossível abrir o arquivo\n");
        return 1;
    }

    fseek(f, 0, SEEK_END);
    tamanhoArquivo = ftell(f); // Descobrimos o tamanho do arquivo no geral
    rewind(f);

    tamanhoRegistro = sizeof(Endereco); // Descobrimos o tamanho de um registro

    qnt_registros = tamanhoArquivo / tamanhoRegistro; // Descobrimos a quantidade de resgistros;

    inicio = 0; // Indice do primeiro registro
    fim = qnt_registros - 1; // Indice do ultimo registro

    while(inicio <= fim){
        iteracoes++;
        meio = (inicio + fim) / 2;
        fseek(f, meio * tamanhoRegistro, SEEK_SET);
        aux = fread(&buffer, sizeof(Endereco),1, f);

        if(strncmp(procurado.cep, buffer.cep, 8) == 0){
            printf("ACHOU!");
            break;
        }
        else if(strncmp(procurado.cep, buffer.cep, 8) > 0){
            inicio = meio + 1;
        }
        else{
            fim = meio - 1;
        }
    }

    printf("Endereço: %s", buffer.logradouro);
    printf("Iterações totais: %d", iteracoes);
    fclose(f);
    return 0;
}

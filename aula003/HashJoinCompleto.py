import struct
import ctypes
import os


arquivoAleatorio1 = "data/extracao-aleatoria1.dat"
arquivoAleatorio2 = "data/extracao-aleatoria2.dat"
indexName1 = "data/aleatorio1-hash-bloco.dat"
indexName2 = "data/aleatorio2-hash-bloco.dat"
arquivoIntersecao = "data/intersecao.dat"
N = 1000 #  Quantidade máxima de chaves que podem ser armazenadas numa HashPage
hashSize = 1399 #   Quantidade de HashPages no arquivo de índices
dataFormat = "72s72s72s72s2s8s2s" # Formato de um registro CEP
dataStruct = struct.Struct(dataFormat)
keyColumnIndex = 5 #    Coluna da chave no registro CEP

class HashPage(ctypes.Structure):
    _fields_ = [
        ("size", ctypes.c_uint16),
        ("keys", ctypes.c_uint32 * N), 
        ("pointers", ctypes.c_uint32 * N),
        ("next", ctypes.c_uint32)
    ]

# Função Hash
def h(key):
    return key%hashSize

def intersecao(arquivoIndicesA, arquivoIndicesB, arquivoA, arquivoIntersecao):
    hpA = HashPage()
    hpB = HashPage()
    indicesA = open(arquivoIndicesA, "rb")
    indicesB = open(arquivoIndicesB, "rb")
    dadosA = open(arquivoA, "rb")
    intersecao = open(arquivoIntersecao, "wb")
    numeroIntesecoes = 0
    for l in range(0, hashSize): # Pecorre as HashPages do arquivo de índices A
        indicesA.readinto(hpA) # Lê a HashPage e armazena a leitura na variável 'hpA'
        for x in range(0, hpA.size): # Percorre as chaves da HashPage de 'hpA'
            p = h(hpA.keys[x]) # Calcula o valor da HashPage associado à uma chave
            indicesB.seek(p * ctypes.sizeof(hpB), os.SEEK_SET) # Posiciona o cursor no arquivo de índices B utilizando o valor calculado acima
            indicesB.readinto(hpB) # Lê a HashPage no arquivo de índices B e armazena a leitura em 'hpB' 
            for y in range(0, hpB.size): # Percorre as chaves da HashPage de 'hpB'
                if hpA.keys[x] == hpB.keys[y]: # Se a chave está presente quanto em 'hpA' quanto 'hpB':
                    dadosA.seek(hpA.pointers[x] * dataStruct.size, os.SEEK_SET) # Procuramos o registro no arquivo de dados, através do ponteiro associado
                    line = dadosA.read(dataStruct.size) # Lê o registro no arquivo de dados
                    intersecao.write(line) # Escreve o registro no arquivo de interseção
                    numeroIntesecoes += 1
                    break
    indicesA.close()
    indicesB.close()
    dadosA.close()
    intersecao.close()
    return numeroIntesecoes

def populaArquivoDeIndex(nomeArquivoDados, nomeArquivoIndex, colunaChaveProcura):
    hp = HashPage()
    recordNumber = 0
    fDados = open(nomeArquivoDados, "rb") # Abre o arquivo de dados
    fIndex = open(nomeArquivoIndex, "r+b") # Abre o arquivo de índices
    while True:
        line = fDados.read(dataStruct.size) # Lê um registro do arquivo de dados
        if len(line) == 0: # Se a leitura for igual à 0, EOF, já lemos todo o arquivo
            break
        record = dataStruct.unpack(line) # Desempacota o registro
        key = int(record[colunaChaveProcura]) # Extrai a chave de procura (CEP)
        p = h(key) # Gera o valor hash, o valor da HashPage que será responsável por guardar a chave
        fIndex.seek(p * ctypes.sizeof(hp), os.SEEK_SET) # Posiciona o cursor na devida HashPage
        fIndex.readinto(hp) # Lê a HashPage e armazena a leitura no objeto 'hp'
        fIndex.seek(p * ctypes.sizeof(hp), os.SEEK_SET) # Reposiciona o curso sobre a devida HashPage

        if (hp.size < N): # Se a HashPage não está cheia:
            hp.keys[hp.size] = key # Adiciona a chave no array de chaves
            hp.pointers[hp.size] = recordNumber # Adiciona o ponteiro do arquivo de dados
            hp.size += 1 # Acresce o número de chaves da HashPage
            fIndex.write(hp) # Atualiza o HashPage no arquivo de índice
        recordNumber += 1
    fDados.close()
    fIndex.close()
    return recordNumber

hp = HashPage()
with open(indexName1,"wb") as fi:
    for i in range(0,hashSize):
        fi.write(hp)

with open(indexName2,"wb") as fi:
    for i in range(0,hashSize):
        fi.write(hp)

x = populaArquivoDeIndex(arquivoAleatorio1, indexName1, keyColumnIndex)
print(f"{x} chaves escritas no arquivo de índices 1!")
x = populaArquivoDeIndex(arquivoAleatorio2, indexName2, keyColumnIndex)
print(f"{x} chaves escritas no arquivo de índices 2!")

x = intersecao(indexName1, indexName2, arquivoAleatorio1, arquivoIntersecao)
print(f"{x} chaves na interseção entre os arquivos!")

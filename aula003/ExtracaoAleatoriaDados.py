import struct
import random
import os

fileName = "data/cep.dat"
outputName1 = "data/extracao-aleatoria1.dat"
outputName2 = "data/extracao-aleatoria2.dat"
dataFormat = "72s72s72s72s2s8s2s" # Formato de um registro CEP
colunaDaChave = 5 # Coluna da chave de procura (CEP)
dataStruct = struct.Struct(dataFormat)

def valorAleatorio(): # Gera um número aleatório (0 <= N < 1)
    return random.random()

def extracaoAleatoria(arquivoBase, arquivoSaida):
    recordNumbers = 0
    with open(arquivoBase, "rb") as f, open(arquivoSaida, "wb") as fsaida: # Abre o arquivo bruto para leitura e o arquico de saída para escrita
        while True:
            line =  f.read(dataStruct.size) # Lê um registro do arquivo bruto
            if len(line) == 0: # Se a leitura for == 0, EOF, já lemos todo o arquivo
                break
            numeroAleatorio = valorAleatorio() # Gera o valor aleatório
            if numeroAleatorio < 0.8: # Se o valor for menor que 0.8:
                fsaida.write(line)  # Escreve o registro no arquivo de saída
                recordNumbers += 1
    return recordNumbers

x = extracaoAleatoria(fileName, outputName1)        
print(f"{x} registro escritos no arquivo aleatório 1!")
x = extracaoAleatoria(fileName, outputName2)
print(f"{x} registro escritos no arquivo aleatório 2!")

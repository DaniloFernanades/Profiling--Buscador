from memory_profiler import profile
import time
import psutil
import random

def criar(nome, maxi):
    arq = open(nome, 'w')

    for i in range(maxi):
        num = random.randint(0, maxi)
        arq.write(str(num) + '\n')
    arq.close()
    

@profile    
def busca():
    cont = 0
    nome = str(input('Nome do arquivo:'))
    palpite = int(input('Palpite:'))
    
    arq = open(nome,'r')
    
    timer_inicio = time.time()
    
    for num in (arq.readlines()):
        cont += 1
        if num.strip() == str(palpite):
            timer_fim = time.time()
            return 'Encontrado' + '(' + str(cont) + ')' + '\n' + 'Tempo Decorrido em Segundos: ' + str(timer_fim - timer_inicio)
    return 'Não Existe'
    arq.close()

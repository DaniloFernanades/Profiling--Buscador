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
def busca(nome, palpite):
    cont = 0
    with open(nome, 'r') as arquivo:
        timer_inicio = time.time()

        for num in arquivo:
            cont += 1
            if num.strip() == str(palpite):
                timer_fim = time.time()
                cpu = psutil.cpu_percent(interval=1)
                return 'Encontrado' + '(' + str(cont) + ')' + '\n' + 'Tempo Decorrido em Segundos: ' + str(
                    timer_fim - timer_inicio) + '\n' + 'Gasto de CPU: ' + str(cpu) + '%'
        timer_fim = time.time()
        cpu = psutil.cpu_percent(interval=1)
        return 'Não Existe' + '(' + str(cont) + ')' + '\n' + 'Tempo Decorrido em Segundos: ' + str(
            timer_fim - timer_inicio) + '\n' + 'Gasto de CPU: ' + str(cpu) + '%'


if __name__ == "__main__":
    nome_arquivo = 'milhao.txt'
    palpite_numerico = 246109
    resultado = busca(nome_arquivo, palpite_numerico)
    print(resultado)

#criar('trilhao.txt', 1000000000000)

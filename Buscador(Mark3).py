from memory_profiler import profile
import time
import psutil
import random

def criar():
    with open('trilhao(2).txt', 'w') as arq:
        for i in range(1000000):
            arq.write(f"{random.randint(0, 1000000000000)}\n")

@profile
def busca(palpite):
    with open('trilhao(2).txt', 'r') as arquivo:
        conjunto = set(map(int, arquivo))

    timer_inicio = time.time()

    for i in range(10000000):
        if palpite in conjunto:
            timer_fim = time.time()
            cpu = psutil.cpu_percent(interval=1)
            return f"Encontrado ({palpite}) em {timer_fim - timer_inicio:.2f} segundos. Uso de CPU: {cpu}%"
        else:
            criar()
    timer_fim = time.time()
    cpu = psutil.cpu_percent(interval=1)
    return f"Não concentrator ({palpite}) em {timer_fim - timer_inicio:.2f} segundos. Uso de CPU: {cpu}%"


if __name__ == "__main__":
    palpite_numerico = 494364946
    print(busca(palpite_numerico))

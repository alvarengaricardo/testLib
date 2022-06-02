# melhor configuração
# manter e usar a saída na apresentação

import concurrent.futures
import time
start = time.perf_counter()

def do_something(seconds):
    print(f'Iniciando espera de {seconds} segundo(s)...')
    time.sleep(seconds)
    print(f'Finalizando espera de {seconds} segundo(s)...')
    return f'Final...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    results = executor.map(do_something, secs)

finish = time.perf_counter()

print(f'Concluido em {round(finish-start, 2)} segundos')





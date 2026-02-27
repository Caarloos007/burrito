import threading
import time

N = 8 

barrier = threading.Barrier(N + 1) 

def trabajador():
    for i in range(1, N + 1):
        print(f"Trabajador 1 está haciendo el burrito {i}...")
        time.sleep(5)
        print(f"Trabajador 1 ha terminado el burrito {i}.")
    
    print("Todos los burritos han sido preparados. Los clientes empiezan a comer.")
    barrier.wait()

def cliente(id):
    print(f"Cliente {id} está esperando...")
    barrier.wait()
    print(f"Cliente {id} está comiendo.")

threads = []
t = threading.Thread(target=trabajador)
threads.append(t)
t.start()


for i in range(1, N + 1):
    t = threading.Thread(target=cliente, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
import threading
import time

N = 8 

num_trabajadores = int(input("¿Cuántos trabajadores deseas? "))
barrier = threading.Barrier(N + num_trabajadores)
lock = threading.Lock()
burrito_counter = 0 

def trabajador(id):
    global burrito_counter
    while True:
        with lock:
            if burrito_counter >= N:
                break
            current_burrito = burrito_counter + 1
            burrito_counter += 1
        
        print(f"Trabajador {id} está haciendo el burrito {current_burrito}...")
        time.sleep(5)
        print(f"Trabajador {id} ha terminado el burrito {current_burrito}.")
    
    print("Todos los burritos han sido preparados. Los clientes empiezan a comer.")
    barrier.wait()

def cliente(id):
    print(f"Cliente {id} está esperando...")
    barrier.wait()
    print(f"Cliente {id} está comiendo.")

threads = []
for i in range(1, num_trabajadores + 1):
    t = threading.Thread(target=trabajador, args=(i,))
    threads.append(t)
    t.start()


for i in range(1, N + 1):
    t = threading.Thread(target=cliente, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
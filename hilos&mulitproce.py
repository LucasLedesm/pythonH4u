#!/usr/bin/env python3

import threading    
import time
import multiprocessing

def tarea(num_tarea):
    print(f"hilo {num_tarea} iniciando")
    time.sleep(2)
    print(f"Hilo { num_tarea} Finalizando")
    
thread1 = threading.Thread(target=tarea, args=(1,))
thread2 = threading.Thread(target=tarea, args=(2,))
proceso1 = multiprocessing.Process(target=tarea, args=(3,))
proceso2 = multiprocessing.Process(target=tarea, args=(4,))

thread1.start()
thread2.start()
proceso1.start()
proceso2.start()
thread1.join()
thread2.join()
proceso1.join()
proceso2.join()
print(f"los hilos y procesos han finalizado exitosamente")
import threading

# lock_global = threading.Lock()

class Contador:
    def __init__(self):
        self.valor = 0


def sumador(contador):#, lock):
    for _ in range(10**6):
        #lock.acquire()
        contador.valor += 1
        #lock.release()


contador = Contador()

t1 = threading.Thread(target=sumador, args=(contador,))#lock_global))
t2 = threading.Thread(target=sumador, args=(contador,))#lock_global))

t1.start()
t2.start()
t1.join()
t2.join()

print("Listo, nuestro contador vale", contador.valor)

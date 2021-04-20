###############
# USO DE JOIN #
###############

import threading
from time import sleep


class Mall(threading.Thread):

    def __init__(self, utilidades):
        super().__init__()
        self.utilidades = utilidades

    def run(self):
        sleep(4)
        self.utilidades += 10


mall = Mall(2)
mall.start()
# mall.join()
# mall.join(timeout=3)
# print(mall.is_alive())


print("\n***************************")
print("Las utilidades finales son:", mall.utilidades)

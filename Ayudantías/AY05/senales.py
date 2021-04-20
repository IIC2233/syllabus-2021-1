import threading
import time


# Tenemos dos eventos.
# Esta es para avisar que el video ya está listo para ser reproducido.
video_cargado = threading.Event()
# Esta es para avisar que el audio ya está listo para ser reproducido.
audio_cargado = threading.Event()


def reproducir_video(nombre):
    print(f"Cargando video {nombre} en t={time.time():.6f}")
    # Supongamos que se demora 3 segundos
    time.sleep(3)
    print(f"¡Video cargado! en t={time.time():.6f}")
    # Avisamos que el video ya está cargado
    video_cargado.set()
    # Esperamos a que el audio ya se haya cargado
    audio_cargado.wait()
    # ¡Listo!
    print(f"Reproduciendo video en t={time.time():.6f}")


def reproducir_audio(nombre):
    print(f"Cargando audio {nombre} en t={time.time():.6f}")
    # Supongamos que se demora 5 segundos
    time.sleep(5)
    print(f"¡Audio cargado! en t={time.time():.6f}")
    # Avisamos que el audio ya está cargado
    audio_cargado.set()
    # Esperamos a que el video ya se haya cargado
    video_cargado.wait()
    # ¡Listo!
    print(f"Reproduciendo audio en t={time.time():.6f}")


t1 = threading.Thread(target=reproducir_audio, args=("'No Te Enamores' - Paloma Mami",))
t2 = threading.Thread(target=reproducir_video, args=("'No Te Enamores' - Paloma Mami",))

t1.start()
t2.start()

t1.join()
t2.join()

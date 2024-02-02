import threading

def funcion_hilo(numero):
    for i in range(numero):
        print(f"hilo {i}")

def main():
    hilo1 = threading.Thread(target=funcion_hilo, args=(5,))
    hilo2 = threading.Thread(target=funcion_hilo, args=(5,))

    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()

if __name__ == "__main__":
    main()
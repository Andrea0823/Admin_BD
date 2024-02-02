import threading

def funcion_hilo(numero_hilo, rango):
    for i in range(rango):
        print(f"hilo {numero_hilo}-{i}")

def main():
    hilo1 = threading.Thread(target=funcion_hilo, args=(1,5))
    hilo2 = threading.Thread(target=funcion_hilo, args=(2,5))

    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()

if __name__ == "__main__":
    main()
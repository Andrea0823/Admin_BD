import threading

# array => caja de nombre hilos
hilos = []

cantidad_hilos = input("Cantidad de hilos: ")
# 5 , cantidad_hilos = 5

def function_hilo(numero, rango):
    for i in range(rango):
        print(f"Hilo {numero} - {i}")

# "camaro", "chevy", "vocho", "1,2,3,4,5", "1,2,3,4,5"

for i in range(int(cantidad_hilos)):
    hilo = threading.Thread(target=function_hilo, args=(i, 5))
    hilos.append(hilo)

    # objeto hilo = funciones

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los hilos han terminado.")





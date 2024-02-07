import mysql.connector
import threading

def conectarAndConsultar(numero):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='usuario1',
            password='user',
            database='pruebas'
        )

        cursor = conexion.cursor()

        consulta = "SELECT nombre, email FROM clientes LIMIT 20;"
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        # for resultado in resultados:
            # print(f"Hilo {numero} - {resultado}")

    finally:
        # Verificar si la variable 'cursor' existe activa y si su valor no es None
        if 'cursor' in locals() and cursor is not None:
            # Cerrar el cursor para liberar recursos asociados
            cursor.close()

        # Verificar si la variable 'conexion' existe activa y si su valor no es None
        if 'conexion' in locals() and conexion is not None:
            # Cerrar la conexión a la base de datos para liberar recursos y cerrar la conexión correctamente
            conexion.close()


hilos = []

cantidad_hilos = input("Cantidad de hilos: ")

for i in range(int(cantidad_hilos)):
    hilo = threading.Thread(target=conectarAndConsultar, args=(i, ))
    hilos.append(hilo)

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los hilos han terminado.")
import time

inicio = time.time()

for i in range(10000):
    print(f"{i} - ", end="")

final = time.time()

print(f"He tardado {round(final - inicio, 1)} segundos.")
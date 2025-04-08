import math
import time
import timeit

def caminos_recursivo(m, n):
    if m == 1 or n == 1:  
        return 1
    return caminos_recursivo(m - 1, n) + caminos_recursivo(m, n - 1)  

def caminos_combinatorio(m, n):
    return math.comb(m + n - 2, n - 1) 

def comparar_con_time(m, n):

    start = time.time()
    resultado_recursivo = caminos_recursivo(m, n)
    end = time.time()
    tiempo_recursivo = end - start
    print("Resultado recursivo:", resultado_recursivo)
    print("Tiempo recursivo:", tiempo_recursivo)

    start = time.time()
    resultado_combinatorio = caminos_combinatorio(m, n)
    end = time.time()
    tiempo_combinatorio = end - start
    print("Resultado combinatorio:", resultado_combinatorio)
    print("Tiempo combinatorio:", tiempo_combinatorio)

def comparar_con_timeit(m, n):
    recursivo_timeit = timeit.timeit(lambda: caminos_recursivo(m, n), number=1)
    combinatorio_timeit = timeit.timeit(lambda: caminos_combinatorio(m, n), number=1)
    print("Recursivo con timeit:", recursivo_timeit)
    print("Combinatorio con timeit:", combinatorio_timeit)

m, n = 5, 5  

print("Comparación con time:")
comparar_con_time(m, n)

print("\nComparación con timeit:")
comparar_con_timeit(m, n)

"""
Obtener lista de factores (divisores exactos) de un número.
"""

# Entradas
numero = int(input("Introduzca un número: "))

# Proceso
factores = []
for factor in range(1, numero + 1):
    if numero % factor == 0:
        factores.append(factor)
factores = [str(i) for i in factores]
factores = ", ".join(factores)

# Salidas
print(f"Factores: {factores}")

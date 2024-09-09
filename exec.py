import math

# Função para calcular o cosseno
def calcular_cosseno(angulo):
    # Convertendo o ângulo de graus para radianos, já que a função cos usa radianos
    radianos = math.radians(angulo)
    return math.cos(radianos)

# Programa principal
angulo = float(input("Digite o ângulo em graus: "))
cosseno = calcular_cosseno(angulo)

print(f"O cosseno de {angulo} graus é: {cosseno:.6f}")

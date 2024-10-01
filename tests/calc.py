import numpy as np
import matplotlib.pyplot as plt

# Definindo a função para o cálculo da interferência
def calculate_interference(lambda_, beta, x, y):
    # Convertendo beta para radianos
    beta_rad = np.radians(beta)
    
    # Termo da equação
    term1 = -2 * np.pi / lambda_
    
    # Equação lambda
    eq_lambda = term1 * (np.cos(beta_rad) * x - np.sin(beta_rad) * y)
    
    # Equação geral
    eq_geral = 2 + 2 * np.cos(eq_lambda)
    
    return eq_geral

# Parâmetros
lambda_ = 5  # Comprimento de onda
x_vals = np.linspace(-10, 10, 400)  # Valores de x
y_vals = np.linspace(-10, 10, 400)  # Valores de y
X, Y = np.meshgrid(x_vals, y_vals)  # Criando a grade

# Calculando para diferentes ângulos beta
betas = [0, 45, 90, 135]  # Diferentes ângulos de rotação
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for i, beta in enumerate(betas):
    ax = axes[i//2, i%2]
    Z = calculate_interference(lambda_, beta, X, Y)
    
    # Gerando o gráfico de contorno da interferência
    contour = ax.contourf(X, Y, Z, levels=100, cmap='viridis')
    fig.colorbar(contour, ax=ax)
    ax.set_title(f'Interferência com β = {beta}°')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

plt.tight_layout()
plt.show()
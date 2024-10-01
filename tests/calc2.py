import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importando o toolkit 3D

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

# Calculando para o ângulo beta de 45°
Z = calculate_interference(lambda_, 45, X, Y)

# Criando a figura para gráfico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Gerando o gráfico 3D de superfície
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title('Superfície de Interferência 3D com β = 45°')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Interferência')

plt.show()
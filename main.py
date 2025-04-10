import matplotlib.pyplot as plt  # Importa pyplot para usar 'plt'
import numpy as np  # Corrige "nupy" a "numpy"

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")  # Corrige "sublot" a "subplot"

# Definición de vectores (ejemplo)
v1 = np.array([1, 2, 3])  # Usa numpy.array para operaciones vectoriales
v2 = np.array([4, 5, 6])

# Graficar vectores en 3D (ejemplo básico)
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='Vector 1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', label='Vector 2')

# Configuraciones adicionales
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.legend()
plt.title('Vectores en 3D')
plt.show()
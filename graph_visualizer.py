import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib.patches import FancyArrowPatch

plt.style.use('seaborn-v0_8-darkgrid')

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

def format_math_expr(expr):
    """Convierte 'a/b' → fracción, 'a!b' → raíz"""
    if '!' in expr:
        grado, rad = expr.split('!')
        return r'$\sqrt[' + grado + ']{' + rad + '}$' if grado else r'$\sqrt{' + rad + '}$'
    elif '/' in expr:
        num, den = expr.split('/')
        return r'$\frac{' + num + '}{' + den + '}$'
    return expr

def visualize_vectors_2d(v1, v2, angle, expr1, expr2):
    """Muestra vectores 2D con notación matemática"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Vectores
    ax.quiver(0, 0, v1[0], v1[1], color='#FF355E', angles='xy', scale_units='xy', scale=1, width=0.01)
    ax.quiver(0, 0, v2[0], v2[1], color='#4453E2', angles='xy', scale_units='xy', scale=1, width=0.01)
    
    # Etiquetas con expresiones originales
    ax.annotate(f'({format_math_expr(expr1[0])}, {format_math_expr(expr1[1])})',
                xy=(v1[0], v1[1]), xytext=(v1[0]+0.5, v1[1]+0.5), color='#FF355E', fontsize=12)
    ax.annotate(f'({format_math_expr(expr2[0])}, {format_math_expr(expr2[1])})',
                xy=(v2[0], v2[1]), xytext=(v2[0]+0.5, v2[1]+0.5), color='#4453E2', fontsize=12)
    
    # Ángulo
    angle_v1 = np.arctan2(v1[1], v1[0])
    angle_v2 = np.arctan2(v2[1], v2[0])
    
    # Asegurar que el arco se dibuje en la dirección correcta
    if angle_v2 < angle_v1:
        angle_v2 += 2 * np.pi
    
    radius = 0.6 * min(np.linalg.norm(v1), np.linalg.norm(v2)) * 0.8
    theta = np.linspace(angle_v1, angle_v2, 30)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    ax.plot(x, y, color='#2E8B57', lw=3, alpha=0.8)
    
    # Posición del texto del ángulo
    mid_idx = len(theta) // 2
    ax.text(x[mid_idx], y[mid_idx], f'{angle:.1f}°', color='#2E8B57', fontsize=14, 
            bbox=dict(facecolor='white', alpha=0.8, boxstyle='round'))

    # Configuración
    max_lim = max(np.max(np.abs(v1)), np.max(np.abs(v2))) * 1.5
    ax.set_xlim(-max_lim, max_lim)
    ax.set_ylim(-max_lim, max_lim)
    ax.set_xlabel('Eje X', fontsize=12)
    ax.set_ylabel('Eje Y', fontsize=12)
    ax.set_title(f'Ángulo entre vectores: {angle:.2f}°', fontsize=14)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.show()

def visualize_vectors_3d(v1, v2, angle, expr1, expr2):
    """Muestra vectores 3D con notación matemática"""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Vectores 3D
    arrow_props = dict(mutation_scale=20, arrowstyle='-|>', shrinkA=0, shrinkB=0)
    a1 = Arrow3D([0, v1[0]], [0, v1[1]], [0, v1[2]], color='#FF355E', lw=2, **arrow_props)
    a2 = Arrow3D([0, v2[0]], [0, v2[1]], [0, v2[2]], color='#4453E2', lw=2, **arrow_props)
    ax.add_artist(a1)
    ax.add_artist(a2)
    
    # Etiquetas
    ax.text(v1[0], v1[1], v1[2], 
            f'({format_math_expr(expr1[0])}, {format_math_expr(expr1[1])}, {format_math_expr(expr1[2])})',
            color='#FF355E', fontsize=10)
    ax.text(v2[0], v2[1], v2[2],
            f'({format_math_expr(expr2[0])}, {format_math_expr(expr2[1])}, {format_math_expr(expr2[2])})',
            color='#4453E2', fontsize=10)
    
    # Ángulo 3D - Mejorado
    u1 = v1/np.linalg.norm(v1)
    u2 = v2/np.linalg.norm(v2)
    
    # Verificar si los vectores son casi paralelos
    cross_product = np.cross(u1, u2)
    cross_norm = np.linalg.norm(cross_product)
    
    if cross_norm < 1e-8:  # Si son casi paralelos
        # Calcular un vector perpendicular arbitrario
        if abs(u1[0]) < abs(u1[1]):
            normal = np.array([0, -u1[2], u1[1]])
        else:
            normal = np.array([-u1[2], 0, u1[0]])
    else:
        normal = cross_product / cross_norm
        
    tangent = np.cross(normal, u1)
    
    theta = np.linspace(0, np.radians(angle), 20)
    radius = 0.5 * min(np.linalg.norm(v1), np.linalg.norm(v2)) * 0.5
    arc = radius * (np.cos(theta)[:, None]*u1 + np.sin(theta)[:, None]*tangent)
    
    ax.plot(arc[:,0], arc[:,1], arc[:,2], color='#2E8B57', lw=3)
    
    # Posición del texto del ángulo
    mid_idx = len(theta) // 2
    ax.text(arc[mid_idx,0], arc[mid_idx,1], arc[mid_idx,2], f'{angle:.1f}°', 
            color='#2E8B57', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

    # Configuración
    max_lim = max(np.max(np.abs(v1)), np.max(np.abs(v2))) * 1.3
    ax.set_xlim(-max_lim, max_lim)
    ax.set_ylim(-max_lim, max_lim)
    ax.set_zlim(-max_lim, max_lim)
    ax.set_xlabel('Eje X', fontsize=10)
    ax.set_ylabel('Eje Y', fontsize=10)
    ax.set_zlabel('Eje Z', fontsize=10)
    ax.set_title(f'Ángulo 3D: {angle:.2f}°', fontsize=14)
    plt.tight_layout()
    plt.show()
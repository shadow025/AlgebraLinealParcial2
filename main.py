import matplotlib.pyplot as plt
import numpy as np
from math import acos, degrees
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

plt.style.use('seaborn-v0_8-darkgrid')
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 2])

arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', shrinkA=0, shrinkB=0)

a1 = Arrow3D([0, v1[0]], [0, v1[1]], [0, v1[2]], 
            color='#FF355E', lw=2, **arrow_prop_dict)
ax.add_artist(a1)

a2 = Arrow3D([0, v2[0]], [0, v2[1]], [0, v2[2]], 
            color='#4453E2', lw=2, **arrow_prop_dict)
ax.add_artist(a2)

ax.text(v1[0], v1[1], v1[2], f'({v1[0]}, {v1[1]}, {v1[2]})', 
        color='#FF355E', fontsize=10)
ax.text(v2[0], v2[1], v2[2], f'({v2[0]}, {v2[1]}, {v2[2]})', 
        color='#4453E2', fontsize=10)

dot_product = np.dot(v1, v2)
norm_v1 = np.linalg.norm(v1)
norm_v2 = np.linalg.norm(v2)
angle_rad = acos(np.clip(dot_product/(norm_v1*norm_v2), -1, 1))
angle_deg = degrees(angle_rad)

def draw_angle_arc_3d(ax, v1, v2, radius=1.0, color='#2E8B57'):
    # Normalizar vectores
    u1 = v1/np.linalg.norm(v1)
    u2 = v2/np.linalg.norm(v2)
    
    normal = np.cross(u1, u2)
    if np.linalg.norm(normal) < 1e-10:  
       
        if np.abs(u1[0]) < np.abs(u1[1]):
            normal = np.cross(u1, [1, 0, 0])
        else:
            normal = np.cross(u1, [0, 1, 0])
            
    normal = normal / np.linalg.norm(normal)
    
    tangent = np.cross(normal, u1)
    tangent = tangent / np.linalg.norm(tangent)
    
    theta = np.linspace(0, angle_rad, 30)
    arc_x = radius * (np.cos(theta) * u1[0] + np.sin(theta) * tangent[0])
    arc_y = radius * (np.cos(theta) * u1[1] + np.sin(theta) * tangent[1])
    arc_z = radius * (np.cos(theta) * u1[2] + np.sin(theta) * tangent[2])
    
    ax.plot(arc_x, arc_y, arc_z, color=color, linewidth=3, alpha=0.8)
    
    mid_idx = len(arc_x)//2
    ax.text(arc_x[mid_idx], arc_y[mid_idx], arc_z[mid_idx],
            f'3D: {angle_deg:.1f}°', color=color, fontsize=12)

v1_xy = np.array([v1[0], v1[1], 0])
v2_xy = np.array([v2[0], v2[1], 0])

ax.plot([0, v1_xy[0]], [0, v1_xy[1]], [0, 0], 'r--', alpha=0.5)
ax.plot([0, v2_xy[0]], [0, v2_xy[1]], [0, 0], 'b--', alpha=0.5)

ax.plot([v1[0], v1[0]], [v1[1], v1[1]], [0, v1[2]], 'r:', alpha=0.3)
ax.plot([v2[0], v2[0]], [v2[1], v2[1]], [0, v2[2]], 'b:', alpha=0.3)

dot_product_xy = np.dot(v1_xy[:2], v2_xy[:2])
norm_v1_xy = np.linalg.norm(v1_xy[:2])
norm_v2_xy = np.linalg.norm(v2_xy[:2])
angle_rad_xy = acos(np.clip(dot_product_xy/(norm_v1_xy*norm_v2_xy), -1, 1))
angle_deg_xy = degrees(angle_rad_xy)

def draw_angle_arc_xy(ax, v1_xy, v2_xy, radius=0.7, color='#FF9500'):
    
    angle_v1 = np.arctan2(v1_xy[1], v1_xy[0])
    angle_v2 = np.arctan2(v2_xy[1], v2_xy[0])
    
    if abs(angle_v2 - angle_v1) > np.pi:
        if angle_v1 < angle_v2:
            angle_v1 += 2 * np.pi
        else:
            angle_v2 += 2 * np.pi
    
    theta = np.linspace(min(angle_v1, angle_v2), max(angle_v1, angle_v2), 50)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.zeros_like(theta)
    
    ax.plot(x, y, z, color=color, linewidth=3, alpha=0.8)
    
    mid_idx = len(theta)//2
    ax.text(x[mid_idx], y[mid_idx], 0,
            f'XY: {angle_deg_xy:.1f}°', color=color, fontsize=12)

draw_angle_arc_3d(ax, v1, v2, radius=1.0)
draw_angle_arc_xy(ax, v1_xy, v2_xy, radius=0.7)

max_coord = max(np.max(v1), np.max(v2)) * 1.3
ax.set_xlim([0, max_coord])
ax.set_ylim([0, max_coord])
ax.set_zlim([0, max_coord])
ax.set_xlabel('Eje X', fontsize=12, labelpad=10)
ax.set_ylabel('Eje Y', fontsize=12, labelpad=10)
ax.set_zlabel('Eje Z', fontsize=12, labelpad=10)

ax.set_title(f'Ángulos entre vectores 3D\n'
             f'Ángulo 3D: {angle_deg:.2f}° | Ángulo XY: {angle_deg_xy:.2f}°', 
             fontsize=14, pad=20)

legend_elements = [
    plt.Line2D([0], [0], color='#FF355E', lw=2, label=f'Vector 1: [{v1[0]}, {v1[1]}, {v1[2]}]'),
    plt.Line2D([0], [0], color='#4453E2', lw=2, label=f'Vector 2: [{v2[0]}, {v2[1]}, {v2[2]}]'),
    plt.Line2D([0], [0], color='#2E8B57', lw=2, label=f'Ángulo 3D: {angle_deg:.2f}°'),
    plt.Line2D([0], [0], color='#FF9500', lw=2, label=f'Ángulo XY: {angle_deg_xy:.2f}°')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=10)

info_text = f'• Producto punto 3D: {dot_product:.2f}\n' \
            f'• Producto punto XY: {dot_product_xy:.2f}\n' \
            f'• Norma v1: {norm_v1:.2f}\n' \
            f'• Norma v2: {norm_v2:.2f}\n' \
            f'• Norma v1 (XY): {norm_v1_xy:.2f}\n' \
            f'• Norma v2 (XY): {norm_v2_xy:.2f}'
ax.text2D(0.05, 0.05, info_text, transform=ax.transAxes,
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'),
         fontsize=10, verticalalignment='bottom')

ax.grid(True, linestyle=':', alpha=0.6)
ax.xaxis.pane.set_alpha(0.1)
ax.yaxis.pane.set_alpha(0.1)
ax.zaxis.pane.set_alpha(0.1)
ax.view_init(elev=30, azim=45)  

ax.plot([0], [0], [0], 'ko', markersize=5)
ax.text(0, 0, 0, '(0,0,0)', fontsize=9)

plt.tight_layout()
plt.show()
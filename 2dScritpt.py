import matplotlib.pyplot as plt
import numpy as np
from math import acos, degrees

plt.style.use('seaborn-v0_8-darkgrid')
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)


v1 = np.array([2, 5])
v2 = np.array([8, 1])

ax.quiver(0, 0, v1[0], v1[1],
          color='#FF355E', label=f'Vector 1: [{v1[0]}, {v1[1]}]',
          angles='xy', scale_units='xy', scale=1, width=0.008)
ax.quiver(0, 0, v2[0], v2[1],
          color='#4453E2', label=f'Vector 2: [{v2[0]}, {v2[1]}]',
          angles='xy', scale_units='xy', scale=1, width=0.008)

ax.annotate(f'({v1[0]}, {v1[1]})', 
            xy=(v1[0], v1[1]), 
            xytext=(v1[0]+0.1, v1[1]+0.1),
            fontsize=10,
            color='#FF355E')

ax.annotate(f'({v2[0]}, {v2[1]})', 
            xy=(v2[0], v2[1]), 
            xytext=(v2[0]+0.1, v2[1]+0.1),
            fontsize=10,
            color='#4453E2')

dot_product = np.dot(v1, v2)
norm_v1 = np.linalg.norm(v1)
norm_v2 = np.linalg.norm(v2)
angle_rad = acos(np.clip(dot_product/(norm_v1*norm_v2), -1, 1))
angle_deg = degrees(angle_rad)

def draw_angle_arc(ax, v1, v2, radius=0.5, color='#2E8B57'):
    angle_v1 = np.arctan2(v1[1], v1[0])
    
    angle_v2 = np.arctan2(v2[1], v2[0])
    
    if abs(angle_v2 - angle_v1) > np.pi:
        if angle_v1 < angle_v2:
            angle_v1 += 2 * np.pi
        else:
            angle_v2 += 2 * np.pi
    
    theta = np.linspace(min(angle_v1, angle_v2), max(angle_v1, angle_v2), 50)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    ax.plot(x, y, color=color, linewidth=3, alpha=0.8)
    
    mid_angle = (angle_v1 + angle_v2) / 2
    label_x = radius * 1.2 * np.cos(mid_angle)
    label_y = radius * 1.2 * np.sin(mid_angle)
    ax.text(label_x, label_y, f'{angle_deg:.1f}°', 
            color=color, fontsize=12, ha='center', va='center',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor=color, boxstyle='round,pad=0.3'))

draw_angle_arc(ax, v1, v2, radius=0.8)

max_limit = max(np.concatenate([v1, v2])) * 1.3
ax.set_xlim([0, max_limit])
ax.set_ylim([0, max_limit])
ax.set_xlabel('Eje X', fontsize=12, labelpad=10)
ax.set_ylabel('Eje Y', fontsize=12, labelpad=10)
ax.set_title(f'Ángulo entre vectores: {angle_deg:.2f}°', fontsize=14, pad=20)

info_text = f'• Producto punto: {dot_product:.2f}\n' \
            f'• Norma v1: {norm_v1:.2f}\n' \
            f'• Norma v2: {norm_v2:.2f}\n' \
            #f'• Ángulo: {angle_deg:.2f}°'
ax.text(0.05, 0.95, info_text, transform=ax.transAxes,
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'),
        fontsize=10, verticalalignment='top')

ax.grid(True, linestyle=':', alpha=0.6)
ax.set_aspect('equal')  
legend = ax.legend(loc='upper right', fontsize=10, shadow=True)
legend.get_frame().set_facecolor('white')
legend.get_frame().set_edgecolor('gray')

ax.plot(0, 0, 'ko', markersize=5)
ax.text(0.1, 0.1, '(0,0)', fontsize=9)

plt.tight_layout()
plt.show()
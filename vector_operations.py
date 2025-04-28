import numpy as np
from math import acos, degrees

def calculate_angle_2d(v1, v2):
    """Calcula el ángulo entre 2 vectores 2D en grados"""
    if len(v1) != 2 or len(v2) != 2:
        raise ValueError("Vectores deben ser 2D")
    
    v1_np = np.array(v1)
    v2_np = np.array(v2)
    
    # Prevenir división por cero
    norm_v1 = np.linalg.norm(v1_np)
    norm_v2 = np.linalg.norm(v2_np)
    
    if norm_v1 == 0 or norm_v2 == 0:
        raise ValueError("Los vectores no pueden tener magnitud cero")
    
    dot = np.dot(v1_np, v2_np)
    cos_angle = np.clip(dot / (norm_v1 * norm_v2), -1.0, 1.0)
    return degrees(acos(cos_angle))

def calculate_angle_3d(v1, v2):
    """Calcula el ángulo entre 2 vectores 3D en grados"""
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Vectores deben ser 3D")
    
    v1_np = np.array(v1)
    v2_np = np.array(v2)
    
    # Prevenir división por cero
    norm_v1 = np.linalg.norm(v1_np)
    norm_v2 = np.linalg.norm(v2_np)
    
    if norm_v1 == 0 or norm_v2 == 0:
        raise ValueError("Los vectores no pueden tener magnitud cero")
    
    dot = np.dot(v1_np, v2_np)
    cos_angle = np.clip(dot / (norm_v1 * norm_v2), -1.0, 1.0)
    return degrees(acos(cos_angle))
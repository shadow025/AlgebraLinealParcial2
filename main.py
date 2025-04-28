import re
import math
import numpy as np
from vector_operations import calculate_angle_2d, calculate_angle_3d
from graph_visualizer import visualize_vectors_2d, visualize_vectors_3d

def parse_value(input_str):
    """Convierte una entrada (número, fracción a/b, raíz a!b) a float"""
    input_str = input_str.strip()
    
    if '/' in input_str:  # Fracción
        num, den = input_str.split('/')
        try:
            return float(num) / float(den)
        except:
            raise ValueError("Fracción inválida. Use formato 'a/b'")
    
    elif '!' in input_str:  # Raíz
        parts = input_str.split('!')
        if len(parts) == 2:
            grado, radicando = parts
            grado = 2 if grado == '' else float(grado)
            try:
                return float(radicando) ** (1/grado)
            except:
                raise ValueError("Raíz inválida. Use formato 'a!b' para √[a](b)")
        else:
            raise ValueError("Formato de raíz inválido")
    
    else:  # Número normal
        try:
            return float(input_str)
        except:
            raise ValueError("Entrada no numérica")

def get_vector_input(dimension):
    """Recoge un vector conservando las expresiones originales"""
    vector = []
    expressions = []
    
    for i in range(dimension):
        while True:
            try:
                value = input(f"Ingrese el componente {i+1} del vector (formato: número, a/b, o a!b): ")
                expressions.append(value)
                vector.append(parse_value(value))
                break
            except ValueError as e:
                print(f"Error: {e}")
    
    return vector, expressions

def main():
    print("\nCalculadora de ángulo entre vectores")
    print("-----------------------------------")
    
    # Selección de dimensión
    while True:
        dim = input("¿Vectores 2D o 3D? (2/3): ").strip()
        if dim in ['2', '3']:
            dimension = int(dim)
            break
        print("Error: Ingrese 2 o 3")
    
    # Input de vectores
    print("\nVector 1:")
    v1, expr1 = get_vector_input(dimension)
    
    print("\nVector 2:")
    v2, expr2 = get_vector_input(dimension)
    
    # Cálculo y visualización
    try:
        if dimension == 2:
            angle = calculate_angle_2d(v1, v2)
            visualize_vectors_2d(v1, v2, angle, expr1, expr2)
        else:
            angle = calculate_angle_3d(v1, v2)
            visualize_vectors_3d(v1, v2, angle, expr1, expr2)
        
        print(f"\nEl ángulo entre los vectores es: {angle:.2f}°")
    except Exception as e:
        print(f"\nError: {e}\nRevise los vectores ingresados")

if __name__ == "__main__":
    main()
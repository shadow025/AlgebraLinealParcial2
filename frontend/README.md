# Interfaz de Entrada de Vectores

Este proyecto es una interfaz simple para ingresar dos vectores en 2D o 3D, con opciones para ingresar fracciones, raíces cuadradas y potencias en formato de texto. Los datos se envían como cadenas de texto crudas que luego serán interpretadas por el backend para realizar los cálculos matemáticos.

## Funcionalidad

- **Dimensiones**: El usuario puede elegir entre trabajar con vectores de 2 dimensiones o 3 dimensiones.
- **Entrada de Vectores**: El usuario ingresa los valores de dos vectores en formato de texto.
- **Formatos permitidos**:
  - **Fracciones**: `numerador/denominador` (Ej: `3/4`)
  - **Raíces**: `n!m` (Ej: `2!9` para la raíz cuadrada de 9, `3!27` para la raíz cúbica de 27)
  - **Potencias**: `base^exponente` (Ej: `2^3` para 2 elevado a 3, `5^2` para 5 elevado a 2)

Cuando el usuario envíe los datos, estos se guardan en variables como cadenas de texto y se envían al backend para su procesamiento.

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado Node.js y npm. Si no los tienes instalados, puedes hacerlo desde su [sitio web oficial](https://nodejs.org/).

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Instala las dependencias del proyecto:

   ```bash
   npm install
   ```

3. Para correr la aplicación, usa el siguiente comando:

   ```bash
   npm run dev
   ```

4. Abre tu navegador y ve a [http://localhost:3000](http://localhost:3000) para ver la interfaz.

## ¿Cómo funciona la interfaz?

1. El usuario selecciona la dimensión (2D o 3D) de los vectores.
2. Luego, ingresa los valores de cada componente de los vectores (X, Y, y Z si es 3D).
3. Al hacer clic en el botón **"Enviar datos"**, los valores de los vectores se envían al backend como cadenas de texto.

**Ejemplo de entrada**:

- **Vector 1**: `3/4`, `5!25`, `2^3`
- **Vector 2**: `1/2`, `2!16`, `3^2`

**Nota**: El backend debe poder interpretar las cadenas de texto con las siguientes reglas:

- `3/4` se convierte en `0.75`
- `5!25` se interpreta como `√25 = 5`
- `2^3` se interpreta como `8`

## Estructura del proyecto

El código React se encuentra en la carpeta `frontend` y los archivos principales son:

- `App.jsx`: Contiene la estructura principal de la aplicación y el componente `VectorInputForm`.
- `VectorInputForm.jsx`: Contiene el formulario para ingresar los vectores y sus validaciones.

## ¿Cómo recibiré los datos en el backend?

Los datos que se envíen desde la interfaz estarán en el siguiente formato:

```json
{
  "vector1": ["3/4", "5!25", "2^3"],
  "vector2": ["1/2", "2!16", "3^2"],
  "dimension": "3D"
}
```

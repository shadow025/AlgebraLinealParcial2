import React, { useState } from 'react';

export default function VectorInputForm() {
    const [dimension, setDimension] = useState('2D');

    const [x1, setX1] = useState('');
    const [y1, setY1] = useState('');
    const [z1, setZ1] = useState('');
    const [x2, setX2] = useState('');
    const [y2, setY2] = useState('');
    const [z2, setZ2] = useState('');

    const [error, setError] = useState('');

    const handleSubmit = () => {
        const campos2D = [x1, y1, x2, y2];
        const campos3D = [x1, y1, z1, x2, y2, z2];

        const camposValidar = dimension === '2D' ? campos2D : campos3D;
        const hayVacios = camposValidar.some(campo => campo.trim() === '');

        if (hayVacios) {
            setError('Por favor llena todos los campos.');
            return;
        }

        setError('');

        const datos = {
            dimension,
            vector1: { x: x1, y: y1, ...(dimension === '3D' && { z: z1 }) },
            vector2: { x: x2, y: y2, ...(dimension === '3D' && { z: z2 }) }
        };

        console.log('Enviando datos:', datos);
    };

    return (
        <div>
            <h2>Ángulo entre vectores</h2>

            <label>Dimensión:</label>
            <select value={dimension} onChange={e => setDimension(e.target.value)}>
                <option value="2D">2D</option>
                <option value="3D">3D</option>
            </select>

            <div>
                <h3>Vector 1</h3>
                <input placeholder="X1" value={x1} onChange={e => setX1(e.target.value)} />
                <input placeholder="Y1" value={y1} onChange={e => setY1(e.target.value)} />
                {dimension === '3D' && (
                    <input placeholder="Z1" value={z1} onChange={e => setZ1(e.target.value)} />
                )}
            </div>

            <div>
                <h3>Vector 2</h3>
                <input placeholder="X2" value={x2} onChange={e => setX2(e.target.value)} />
                <input placeholder="Y2" value={y2} onChange={e => setY2(e.target.value)} />
                {dimension === '3D' && (
                    <input placeholder="Z2" value={z2} onChange={e => setZ2(e.target.value)} />
                )}
            </div>

            <div>
                <p>Usar funciones:</p>
                <ul>
                    <li><strong>1/2</strong> para fracción</li>
                    <li><strong>2!9</strong> para raíz (cuadrada si no hay número antes del '!')</li>
                    <li><strong>2^3</strong> para potencia (cuadrado por defecto si falta exponente)</li>
                </ul>
            </div>

            {error && <p style={{ color: 'red' }}>{error}</p>}

            <button onClick={handleSubmit}>Enviar datos</button>
        </div>
    );
}

# Laboratorio: Minimax y Poda Alfa-Beta

## Descripción
Este proyecto implementa los algoritmos Minimax y Poda Alfa-Beta para resolver un árbol de decisión simplificado.

## Objetivo
Comparar el resultado y la eficiencia de Minimax frente a Poda Alfa-Beta.

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución
```bash
python -m src.main
```

## Pruebas
```bash
pytest --cov=src --cov-report=term-missing
```

## Preguntas de análisis
1. ¿Por qué Minimax y Alfa-Beta devuelven el mismo valor?
Ambos exploran el mismo árbol de decisión; Alfa-Beta solo poda ramas que no afectan el resultado final, por lo que el valor óptimo es idéntico.

2. ¿Cuándo Alfa-Beta reduce más nodos?
Cuando el árbol está bien ordenado (primero las ramas más prometedoras), Alfa-Beta puede podar muchas ramas, especialmente en árboles profundos con muchas hojas.

3. ¿Qué ocurre si el árbol está mal ordenado?
Si las ramas prometedoras están al final, Alfa-Beta casi no poda y explora casi todos los nodos, funcionando igual que Minimax.

4. ¿Cómo se aplicaría este algoritmo en ajedrez, damas o tres en raya?
Se evalúan todas las jugadas posibles hasta cierta profundidad, asignando puntajes a las posiciones, y se elige la jugada con mejor valor para el jugador actual.
```

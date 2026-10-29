# Práctica 1 - Fundamentos de los Sistemas Inteligentes (FSI)

Este repositorio contiene el código de la primera práctica de FSI. El objetivo principal ha sido completar el código base de los algoritmos de búsqueda para encontrar rutas óptimas, utilizando como ejemplo el grafo de las ciudades de Rumanía.

## ¿Qué se ha implementado?

A partir de los métodos de búsqueda en anchura (BFS) y profundidad (DFS) que ya venían en el código base, hemos añadido los siguientes algoritmos:

1. **Ramificación y Acotación sin subestimación**
2. **Ramificación y Acotación con subestimación (A*)**

Para integrarlo limpiamente con la función genérica `graph_search` del código base, hemos creado dos nuevas estructuras de datos al final de `search.py`: `PriorityQueue` y `AStarQueue`. Tuvimos que crearlas desde cero porque, aunque los comentarios del código mencionaban una `PriorityQueue`, esta no estaba implementada en los ficheros proporcionados.

También hemos modificado ligeramente `graph_search` para añadir un contador de **nodos expandidos**, lo que permite hacer la comparativa que se pide en el enunciado.

## Comparativa de Resultados (Arad -> Bucarest)

Al ejecutar los cuatro algoritmos buscando la ruta desde la ciudad de Arad hasta Bucarest, hemos obtenido los siguientes datos:

| Algoritmo | Nodos Expandidos | Coste Total | Ruta Encontrada (Invertida en código) |
| :--- | :--- | :--- | :--- |
| **BFS** (Anchura) | 8 | 450 | B -> F -> S -> A |
| **DFS** (Profundidad) | 7 | 733 | B -> P -> C -> D -> M -> L -> T -> A |
| **RyA sin subestimación** | 12 | 418 (Óptimo) | B -> P -> R -> S -> A |
| **RyA con subestimación** (A*) | 5 | 418 (Óptimo) | B -> P -> R -> S -> A |

### Análisis de los métodos

*   **BFS:** Encuentra la solución con menos saltos entre ciudades, pero ignora los costes, por lo que la ruta no es la más corta en distancia.
*   **DFS:** Es muy ineficiente en cuanto a coste (733). El algoritmo profundiza por una rama aleatoria y explora un camino larguísimo antes de dar con el objetivo.
*   **Ramificación y Acotación (sin subestimación):** Garantiza encontrar el coste óptimo (418), pero para estar seguro tiene que expandir más nodos (12), ya que busca de forma concéntrica en todas direcciones evaluando solo el coste acumulado.
*   **Ramificación y Acotación (con subestimación):** También encuentra la ruta óptima, pero al usar la distancia en línea recta como "brújula" (heurística), expande muchos menos nodos, descartando rápidamente las ciudades que se alejan de Bucarest.

## Cómo ejecutar el código

Para probar todos los algoritmos de búsqueda y ver la comparativa de resultados, basta con ejecutar el archivo principal: `run.py`

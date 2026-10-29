# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("BFS")
bfs = search.breadth_first_graph_search(ab)
if bfs:
    print("Ruta:", bfs.path(), "Coste:", bfs.path_cost)


print("\nDFS")
dfs = search.depth_first_graph_search(ab)
if dfs: 
    print("Ruta:", dfs.path(), "Coste:", dfs.path_cost)


print("\nRamificación y Acotación sin subestimación")    
rya = search.ramificacion_y_acotacion_sin_subestimacion(ab)
if rya: 
    print("Ruta:", rya.path(), "Coste:", rya.path_cost)


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

from graph import Graph
from dijkstra import dijkstra

# 그래프 생성 및 초기화
g = Graph()
g.add_node('A')
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'D', 10)
g.add_undirected_edge('C', 'D', 3)

# 그래프 출력
print("Graph:")
for node, edges in g.get_graph().items():
    print(f"{node}: {edges}")

# 다익스트라 테스트
print("\nDijkstra's Algorithm:")
print(dijkstra(g.get_graph(), 'A'))
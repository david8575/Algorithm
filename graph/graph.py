class Graph:
    def __init__(self):
        # 노드와 간선을 저장할 딕셔너리
        self.graph = {}
        
    def add_node(self, node):
        # 노드를 그래프에 추가
        if node not in self.graph:
            self.graph[node] = {}
            
    def add_edge(self, from_node, to_node, weight):
        # 방향성 간선 추가
        if from_node not in self.graph:
            self.add_node(from_node)
        if to_node not in self.graph:
            self.add_node(to_node)
        self.graph[from_node][to_node] = weight
    
    def add_undirected_edge(self, node1, node2, weight):
        # 무방향 간선 추가
        self.add_edge(node1, node2, weight)
        self.add_edge(node2, node1, weight)

    def display(self):
        # 그래프 출력
        for node, edges in self.graph.items():
            print(f"{node}: {edges}")

    def get_graph(self):
        # 그래프 반환
        return self.graph
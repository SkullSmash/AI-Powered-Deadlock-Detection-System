import networkx as nx

class DeadlockDetector:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_process(self, process_id, resource_id):
        self.graph.add_edge(process_id, resource_id)

    def add_resource(self, resource_id, process_id):
        self.graph.add_edge(resource_id, process_id)

    def detect_deadlock(self):
        cycles = list(nx.simple_cycles(self.graph))
        return bool(cycles), cycles

    def get_graph_structure(self):
        return {
            "nodes": list(self.graph.nodes),
            "links": [{"source": u, "target": v} for u, v in self.graph.edges]
        }

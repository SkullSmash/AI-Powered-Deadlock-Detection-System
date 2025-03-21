import networkx as nx
import random

class DeadlockDetector:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_process(self, process_id, resource_id):
        """ Adds an edge between process and resource """
        self.graph.add_edge(process_id, resource_id)
    
    def add_resource(self, resource_id, process_id):
        """ Adds an edge between resource and process """
        self.graph.add_edge(resource_id, process_id)
    
    def detect_deadlock(self):
        """ Detects if there is a cycle in the graph (Deadlock) """
        try:
            cycle = nx.find_cycle(self.graph, orientation='original')
            return True, cycle
        except nx.NetworkXNoCycle:
            return False, []

if __name__ == "__main__":
    detector = DeadlockDetector()
    
    # Simulating processes and resources
    processes = ["P1", "P2", "P3"]
    resources = ["R1", "R2", "R3"]
    
    # Randomly allocate resources to processes
    for i in range(3):
        detector.add_process(processes[i], resources[i])
        detector.add_resource(resources[i], processes[(i+1) % 3])  # Circular allocation
    
    # Check for deadlocks
    deadlock, cycle = detector.detect_deadlock()
    if deadlock:
        print("Deadlock detected! Cycle:", cycle)
    else:
        print("No deadlock detected.")

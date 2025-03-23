import networkx as nx
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Function to generate a random process-resource graph
def generate_graph(num_processes=5, num_resources=3):
    total_nodes = num_processes + num_resources
    G = nx.DiGraph()
    nodes = [f"P{i}" for i in range(num_processes)] + [f"R{i}" for i in range(num_resources)]
    G.add_nodes_from(nodes)

    edges = []
    for _ in range(np.random.randint(3, num_processes * 2)):  # Random edges
        src, tgt = np.random.choice(nodes, 2, replace=False)
        edges.append((src, tgt))
    G.add_edges_from(edges)

    adj_matrix = nx.to_numpy_array(G, nodelist=nodes)  # Ensure fixed order
    deadlock = int(bool(list(nx.simple_cycles(G))))
    return adj_matrix, deadlock


# Generate dataset
def generate_dataset(samples=1000, num_processes=5, num_resources=3):
    total_nodes = num_processes + num_resources
    data = []
    
    for _ in range(samples):
        adj_matrix, deadlock = generate_graph(num_processes, num_resources)
        features = adj_matrix.flatten().tolist()
        data.append(features + [deadlock])

    # Fix column count
    feature_count = total_nodes * total_nodes  # Square adjacency matrix
    columns = [f"edge_{i}" for i in range(feature_count)] + ["deadlock"]
    
    df = pd.DataFrame(data, columns=columns)

    # Save to CSV
    df.to_csv("deadlock_dataset.csv", index=False)
    print("✅ Dataset saved as deadlock_dataset.csv")

    return df


if __name__ == "__main__":
    generate_dataset()

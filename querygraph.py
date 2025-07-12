import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes (tables)
tables = ["customer", "orders", "lineitem", "nation"]
G.add_nodes_from(tables)

# Add edges (foreign key joins)
edges = [
    ("customer", "orders", {"join": "c_custkey = o_custkey"}),
    ("orders", "lineitem", {"join": "o_orderkey = l_orderkey"}),
    ("customer", "nation", {"join": "c_nationkey = n_nationkey"})
]
G.add_edges_from(edges)

# Define positions for a tree-like layout
pos = {
    "customer": (0, 2),
    "nation": (-2, 1),
    "orders": (2, 1),
    "lineitem": (2, 0)
}

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2000)

# Draw the edges
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2, arrows=True, arrowstyle='-|>')

# Draw the labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Draw edge labels (join conditions)
edge_labels = {(u, v): d["join"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', font_size=10)

# Display the plot
plt.title("Query Graph for TPC-H Query 5 Join Structure")
plt.axis("off")
plt.tight_layout()
plt.show()

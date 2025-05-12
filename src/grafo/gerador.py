import networkx as nx
import random

def grafo_aleatorio(num_nos=6, prob=0.3, orientado=True, com_pesos=True):
    G = nx.gnp_random_graph(num_nos, prob, directed=orientado)
    if com_pesos:
        for (u, v) in G.edges():
            G[u][v]['weight'] = random.randint(1, 10)
    return G

def grafo_customizado(arestas, orientado=True):
    G = nx.DiGraph() if orientado else nx.Graph()
    G.add_weighted_edges_from(arestas)
    return G
import networkx as nx
import matplotlib.pyplot as plt

def calcular_scc(G):
    sccs = list(nx.strongly_connected_components(G))
    cmap = plt.cm.get_cmap("tab10", len(sccs))
    cor_por_no = {}
    for i, comp in enumerate(sccs):
        for no in comp:
            cor_por_no[no] = cmap(i)
    return [cor_por_no[n] for n in G.nodes()]

def calcular_dijkstra(G, origem, destino):
    caminho = nx.dijkstra_path(G, origem, destino)
    return list(zip(caminho, caminho[1:]))

def calcular_prim(G):
    T = nx.minimum_spanning_tree(G.to_undirected(), algorithm='prim')
    return list(T.edges())

def calcular_kruskal(G):
    T = nx.minimum_spanning_tree(G.to_undirected(), algorithm='kruskal')
    return list(T.edges())
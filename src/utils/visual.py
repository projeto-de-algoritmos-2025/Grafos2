# src/utils/visual.py
import networkx as nx
from matplotlib.patches import Ellipse

def desenhar_grafo(G, ax, canvas, path_edges=None, node_colors=None, scc_groups=None, legenda_callback=None):
    ax.clear()
    pos = nx.spring_layout(G, k=1.0, seed=42)  # k menor para reduzir dispersão

    if not node_colors:
        node_colors = ['skyblue'] * len(G.nodes)

    nx.draw(G, pos, with_labels=True, ax=ax,
            node_color=node_colors, edge_color='gray', node_size=700)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

    legenda_texto = ""

    if path_edges:
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5, ax=ax)

    all_x, all_y = [], []

    if scc_groups:
        legenda_texto += f"Foram encontrados {len(scc_groups)} componentes fortemente conectados:\n\n"
        for i, comp in enumerate(scc_groups):
            legenda_texto += f"Componente {i+1}: {sorted(comp)}\n"
            xs = [pos[n][0] for n in comp]
            ys = [pos[n][1] for n in comp]
            all_x.extend(xs)
            all_y.extend(ys)
            if xs and ys:
                ellipse = Ellipse(
                    (sum(xs)/len(xs), sum(ys)/len(ys)),
                    width=max(xs) - min(xs) + 2.0,
                    height=max(ys) - min(ys) + 2.0,
                    edgecolor='black',
                    facecolor='none',
                    linestyle='--',
                    linewidth=1.2,
                    zorder=2
                )
                ax.add_patch(ellipse)

    # Adiciona ajuste automático de limites baseado em todos os nós, mesmo sem SCC
    if not all_x or not all_y:
        all_x = [pos[n][0] for n in G.nodes]
        all_y = [pos[n][1] for n in G.nodes]

    if all_x and all_y:
        padding = 1.0
        ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
        ax.set_ylim(min(all_y) - padding, max(all_y) + padding)

    fig = ax.get_figure()
    fig.set_size_inches(16, 10)
    ax.set_position([0.01, 0.01, 0.98, 0.98])
    canvas.draw()

    if legenda_callback and legenda_texto:
        legenda_callback(legenda_texto)

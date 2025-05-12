# src/interface/app.py
import tkinter as tk
from tkinter import simpledialog
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Ellipse
from grafo.gerador import grafo_aleatorio, grafo_customizado
from grafo.algoritmos import calcular_scc, calcular_dijkstra, calcular_prim, calcular_kruskal
from utils.visual import desenhar_grafo

class GrafoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Algoritmos de Grafos")

        self.G = grafo_aleatorio()

        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.pack(pady=5)

        tk.Label(self.frame_botoes, text="Escolha o algoritmo:").grid(row=0, column=0, columnspan=4, pady=(0, 5))

        self.btn_scc = tk.Button(self.frame_botoes, text="SCC", command=self.mostrar_scc)
        self.btn_scc.grid(row=1, column=0)

        self.btn_dijkstra = tk.Button(self.frame_botoes, text="Dijkstra", command=self.mostrar_dijkstra)
        self.btn_dijkstra.grid(row=1, column=1)

        self.btn_prim = tk.Button(self.frame_botoes, text="Prim", command=self.mostrar_prim)
        self.btn_prim.grid(row=1, column=2)

        self.btn_kruskal = tk.Button(self.frame_botoes, text="Kruskal", command=self.mostrar_kruskal)
        self.btn_kruskal.grid(row=1, column=3)

        tk.Label(self.frame_botoes, text="Escolha o tipo de grafo:").grid(row=2, column=0, columnspan=4, pady=(10, 5))

        self.btn_random = tk.Button(self.frame_botoes, text="Grafo Aleatório", command=self.gerar_aleatorio)
        self.btn_random.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.btn_custom = tk.Button(self.frame_botoes, text="Grafo Customizado", command=self.gerar_customizado)
        self.btn_custom.grid(row=3, column=2, columnspan=2, sticky="ew")

        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(fill="both", expand=True)

        self.fig, self.ax = plt.subplots(figsize=(16, 10))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_principal)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.config(width=1000, height=700)
        canvas_widget.pack(side="left", fill="both", expand=True)

        self.texto_legenda = tk.Text(self.frame_principal, width=30, height=20)
        self.texto_legenda.pack(side="right", padx=10, pady=10, fill="y")
        self.texto_legenda.insert("1.0", "Legenda dos SCCs\n")
        self.texto_legenda.configure(state="disabled")

        self.desenhar()

    def desenhar(self, path_edges=None, node_colors=None, scc_groups=None, pos_override=None, legenda_callback=None):
        desenhar_grafo(
            G=self.G,
            ax=self.ax,
            canvas=self.canvas,
            path_edges=path_edges,
            node_colors=node_colors,
            scc_groups=scc_groups,
            legenda_callback=legenda_callback
        )

    def atualizar_legenda(self, texto):
        self.texto_legenda.configure(state="normal")
        self.texto_legenda.delete("1.0", tk.END)
        if texto:
            self.texto_legenda.insert(tk.END, texto)
        self.texto_legenda.configure(state="disabled")

    def mostrar_scc(self):
        try:
            sccs = list(nx.strongly_connected_components(self.G))
            cmap = plt.cm.get_cmap("tab10", len(sccs))
            cor_por_no = {}
            for i, comp in enumerate(sccs):
                for no in comp:
                    cor_por_no[no] = cmap(i)
            node_colors = [cor_por_no[n] for n in self.G.nodes()]
            self.desenhar(node_colors=node_colors, scc_groups=sccs, legenda_callback=self.atualizar_legenda)
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao mostrar SCC: {e}")

    def mostrar_dijkstra(self):
        try:
            origem = int(simpledialog.askstring("Origem", "Digite o nó de origem:"))
            destino = int(simpledialog.askstring("Destino", "Digite o nó de destino:"))
            path_edges = calcular_dijkstra(self.G, origem, destino)
            self.desenhar(path_edges=path_edges)
        except nx.NetworkXNoPath:
            tk.messagebox.showinfo("Caminho não encontrado", "Não existe caminho entre os nós selecionados.")
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao calcular Dijkstra: {e}")


    def mostrar_prim(self):
        try:
            path_edges = calcular_prim(self.G)
            self.desenhar(path_edges=path_edges)
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao calcular Prim: {e}")

    def mostrar_kruskal(self):
        try:
            path_edges = calcular_kruskal(self.G)
            self.desenhar(path_edges=path_edges)
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao calcular Kruskal: {e}")

    def gerar_aleatorio(self):
        self.G = grafo_aleatorio(num_nos=6, prob=0.4)
        self.desenhar(legenda_callback=self.atualizar_legenda)

    def gerar_customizado(self):
        try:
            entrada = simpledialog.askstring("Arestas", "Digite as arestas no formato (origem.destino.peso) separadando-as por vírgula:" \
            "exemplo: (3.2.1),(3.2.2),(3.1.1)")
            lista = [tuple(map(int, parte.strip().strip("()").split("."))) for parte in entrada.split(",")]
            self.G = grafo_customizado(lista)
            self.desenhar(legenda_callback=self.atualizar_legenda)
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao criar grafo customizado: {e}")

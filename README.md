# **Visualizador de Grafos**

### **Número do trabalho:** 2
### **Conteúdo da Disciplina:** Grafos, SCC (Strongly Connected Components), Dijkstra, Prim-Heap, Kruskal

### **Alunos**

| Matrícula   | Aluno                                 |
|-------------|---------------------------------------|
| 190033011   | Luana Souza Silva Torres              |
| 211045196   | Suzane Alves Duarte                   |

---

## **Sobre**

Este projeto é uma aplicação interativa desenvolvida em Python com interface gráfica usando `tkinter`, `networkx` e `matplotlib`. Seu objetivo é auxiliar na visualização e compreensão dos principais algoritmos de grafos:  
- Componentes Fortemente Conectados (SCC)  
- Caminho mínimo com Dijkstra  
- Árvore Geradora Mínima com Prim  
- Árvore Geradora Mínima com Kruskal

Dessa forma, a aplicação permite ao usuário:
- Gerar grafos aleatórios ou definir grafos customizados via entrada.
- Selecionar um algoritmo e visualizar seus efeitos sobre o grafo.
- Observar agrupamentos, caminhos mínimos e árvores geradoras desenhadas dinamicamente.
- Consultar a legenda lateral com informações dos SCCs.

A interface também exibe o grafo com cores, caminhos destacados e componentes cercados por elipses tracejadas.

---

## **Objetivos do Projeto**

- Proporcionar uma forma visual e didática de aprendizado de grafos.
- Facilitar a experimentação prática com algoritmos clássicos.
- Estimular a curiosidade e intuição dos alunos sobre estruturas e caminhos.

---

## **Instalação**

- **Linguagem:** Python 3
- **Bibliotecas:** `tkinter`, `networkx`, `matplotlib`

### **Pré-requisitos:**

Certifique-se de instalar as dependências com:

```bash
pip install -r requirements.txt
```

No Ubuntu/Debian/Linux, para garantir que o `tkinter` está presente:

```bash
sudo apt install python3-tk
```

### **Como executar a aplicação:**

```bash
python src/main.py
```

---

## **Uso**

1. Ao abrir a aplicação, ela iniciará em tela cheia.

2. Você pode:
   - Selecionar o tipo de grafo (aleatório ou customizado).
   - Selecionar um dos algoritmos (SCC, Dijkstra, Prim, Kruskal).

3. O grafo será desenhado com:
   - Nós e arestas visíveis.
   - Caminhos ou agrupamentos destacados.
   - Elipses tracejadas ao redor dos SCCs.

4. A legenda ao lado exibe os nós de cada componente fortemente conectado. 

---

5. Exemplo da Aplicação utilizando um grafo gerado aleatoriamente e o algoritmo de Kruskal
<div>
<img src="src\assets\kruskalExemplo.png">
</div>


## **Vídeo de Apresentação**
<div class="video-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 20px 0; border-radius: 8px;">
    <iframe 
        src="https://youtu.be/oWhBgi1trDA" 
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
        allowfullscreen>
    </iframe>
</div>
<center><em>Vídeo de Apresentação</em></center>


O vídeo de apresentação também também pode ser acessado clicando [aqui](https://youtu.be/oWhBgi1trDA).


## **Outros**

- Elipses tracejadas indicam agrupamentos SCC.
- Cores distintas são atribuídas a cada componente SCC.
- Caminhos mínimos são exibidos em vermelho.
- Os grafos são por padrão direcionados e transformados em não-direcionados para as soluções de Kruskal e Prim.

---
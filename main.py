import numpy as np
from collections import deque
import random
import networkx as nx
import matplotlib.pyplot as plt
import ot

def adj_to_dist(adj_matrix):
    n = len(adj_matrix)
    distance_matrix = np.full((n, n), np.inf)

    for start in range(n):
        # BFS
        queue = deque([start])
        distances = [-1] * n
        distances[start] = 0

        while queue:
            current = queue.popleft()
            for neighbor in range(n):
                if adj_matrix[current][neighbor] == 1 and distances[neighbor] == -1:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)

        for end in range(n):
            if distances[end] != -1:
                distance_matrix[start][end] = distances[end]

    return distance_matrix.astype(int)

def plot_graph(adj_matrix):
    G = nx.from_numpy_array(adj_matrix)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray',
            node_size=800, font_size=12, font_weight='bold')

    plt.title("Graph")
    plt.savefig("graph.png")
    print("Saved: 'graph.png' に保存しました")

def gen_random_adj_matrix(n, edge_prob=0.3, seed=None):
    # n : ノード数
    # edge_prob : 各辺が存在する確率
    # seed : ランダムシード

    if seed is not None:
        np.random.seed(seed)

    # 上三角行列にランダムな0/1を生成（対角は0）
    upper_tri = np.triu(np.random.rand(n, n) < edge_prob, k=1).astype(int)

    # 対称行列に変換（上三角 + 転置）
    adj_matrix = upper_tri + upper_tri.T

    return adj_matrix

def main():
    adj = gen_random_adj_matrix(6, edge_prob=0.5, seed=42)
    plot_graph(adj)

if __name__ == "__main__":
    main()

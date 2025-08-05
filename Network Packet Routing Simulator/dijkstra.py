import tkinter as tk
from tkinter import messagebox
import heapq
import time
import threading
import math

class NetworkSimulator:
    def __init__(self, master):
        self.master = master
        master.title("Network Packet Routing Simulator (Dijkstra)")

        # Instructions label
        self.instructions = tk.Label(master, text="Enter input (example format):\n"
                                                  "5 6\n"
                                                  "1 2 2\n"
                                                  "1 3 1\n"
                                                  "2 3 1\n"
                                                  "1 4 3\n"
                                                  "4 5 2\n"
                                                  "5 3 5\n"
                                                  "1 5", font=("Arial", 10))
        self.instructions.pack()

        # Multiline input box
        self.input_text = tk.Text(master, height=10, width=40)
        self.input_text.pack()

        # Run button
        self.run_button = tk.Button(master, text="Build Graph & Find Path", command=self.run_simulation)
        self.run_button.pack()

        # Canvas for drawing
        self.canvas = tk.Canvas(master, width=700, height=500, bg="white")
        self.canvas.pack()

        # Result label
        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack()

        # To store node positions and canvas objects
        self.node_positions = {}
        self.node_objects = {}
        self.edge_objects = []

    def parse_input(self, input_str):
        lines = input_str.strip().split('\n')
        if len(lines) < 2:
            messagebox.showerror("Error", "Invalid input format")
            return None

        try:
            nodes, edges = map(int, lines[0].split())
            edge_lines = lines[1:1 + edges]
            last_line = lines[1 + edges]
        except Exception:
            messagebox.showerror("Error", "Invalid input format")
            return None

        graph = {i: {} for i in range(1, nodes + 1)}

        for line in edge_lines:
            u, v, w = map(int, line.split())
            graph[u][v] = w
            graph[v][u] = w  # Assuming undirected graph

        source, destination = map(int, last_line.split())

        return nodes, graph, source, destination

    def generate_positions(self, nodes):
        # Arrange nodes evenly in a circle
        center_x, center_y = 350, 250
        radius = 200
        self.node_positions = {}
        for i in range(1, nodes + 1):
            angle = 2 * math.pi * (i - 1) / nodes
            x = center_x + int(radius * math.cos(angle))
            y = center_y + int(radius * math.sin(angle))
            self.node_positions[i] = (x, y)

    def draw_graph(self, graph):
        self.canvas.delete("all")
        self.node_objects.clear()
        self.edge_objects.clear()

        # Draw edges with weights
        drawn_edges = set()
        for u in graph:
            for v in graph[u]:
                if (v, u) in drawn_edges:
                    continue
                x1, y1 = self.node_positions[u]
                x2, y2 = self.node_positions[v]
                self.canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)
                mid_x, mid_y = (x1 + x2)//2, (y1 + y2)//2
                self.canvas.create_text(mid_x, mid_y, text=str(graph[u][v]), font=("Arial", 10, "bold"), fill="blue")
                drawn_edges.add((u, v))

        # Draw nodes
        for node, (x, y) in self.node_positions.items():
            oval = self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue", outline="black", width=2)
            self.canvas.create_text(x, y, text=str(node), font=("Arial", 12, "bold"))
            self.node_objects[node] = oval

    def dijkstra(self, graph, start, goal):
        queue = [(0, start)]
        dist = {node: float('inf') for node in graph}
        dist[start] = 0
        parent = {node: None for node in graph}
        visited = set()

        while queue:
            cost, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            if node == goal:
                break
            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_cost = cost + graph[node][neighbor]
                    if new_cost < dist[neighbor]:
                        dist[neighbor] = new_cost
                        parent[neighbor] = node
                        heapq.heappush(queue, (new_cost, neighbor))

        # Reconstruct path
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

        if path[0] == start:
            return path, dist[goal]
        else:
            return [], float('inf')

    def animate_path(self, path):
        # Highlight nodes and edges on path step-by-step
        for i in range(len(path)):
            node = path[i]
            # Highlight node
            self.canvas.itemconfig(self.node_objects[node], fill="orange")
            if i > 0:
                # Highlight edge from previous node
                prev = path[i-1]
                x1, y1 = self.node_positions[prev]
                x2, y2 = self.node_positions[node]
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=4, tags="highlight")
            self.canvas.update()
            time.sleep(0.7)

    def run_simulation(self):
        input_str = self.input_text.get("1.0", tk.END)
        parsed = self.parse_input(input_str)
        if not parsed:
            return
        nodes, graph, source, destination = parsed

        self.generate_positions(nodes)
        self.draw_graph(graph)
        self.result_label.config(text="Calculating shortest path...")

        # Run Dijkstra and animation in a separate thread to prevent UI freeze
        def run():
            path, cost = self.dijkstra(graph, source, destination)
            if not path:
                self.result_label.config(text=f"No path from {source} to {destination}")
                return
            self.result_label.config(text=f"Shortest Path: {' → '.join(map(str,path))} | Total Cost: {cost}")
            self.animate_path(path)

        threading.Thread(target=run).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSimulator(root)
    root.mainloop()

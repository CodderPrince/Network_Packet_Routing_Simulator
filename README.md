# Network Packet Routing Simulator 🚦📡
---

````markdown
**A comprehensive Network Packet Routing Simulator featuring both C++ and Python implementations of Dijkstra’s shortest path algorithm with interactive and animated visualizations.**

---

## 📚 Project Overview

This project demonstrates the shortest path routing in a network using Dijkstra’s algorithm. It includes:

- **C++ version:** Command-line tool with step-by-step console output and packet movement simulation using Windows API.
- **Python version:** GUI application built with Tkinter offering dynamic graph input and colorful, animated packet routing visualization.

---

## 🎯 Key Features

### Common Features
- Implementation of Dijkstra's shortest path algorithm for network routing.
- Simulation of packet movement from source to destination.
- User-defined graph input (nodes, edges, weights, source & destination).

### C++ Version Highlights
- Console-based interface with detailed debug output.
- Step-by-step node visiting and distance updates.
- Packet movement simulation with `Sleep()` delays for realism.
- Suitable for quick testing and command-line usage.

### Python Version Highlights
- Modern GUI using Tkinter for interactive input.
- Visual graph rendering with colorful nodes and weighted edges.
- Animated packet movement along the shortest path.
- Easy-to-use interface ideal for demonstrations and teaching.

---

## 📷 Screenshots (Python GUI)

<div align="center" style="margin: 15px 0;">
  <img src="https://github.com/CodderPrince/Network_Packet_Routing_Simulator/blob/main/Network%20Packet%20Routing%20Simulator/UI/image_2025-08-05_17-09-05.png" alt="Screenshot 1" width="300" style="margin:5px;"/>
  <img src="https://github.com/CodderPrince/Network_Packet_Routing_Simulator/blob/main/Network%20Packet%20Routing%20Simulator/UI/image_2025-08-05_17-09-39.png" alt="Screenshot 2" width="300" style="margin:5px;"/>
  <br/>
  <img src="https://github.com/CodderPrince/Network_Packet_Routing_Simulator/blob/main/Network%20Packet%20Routing%20Simulator/UI/image_2025-08-05_17-10-42.png" alt="Screenshot 3" width="300" style="margin:5px;"/>
  <img src="https://github.com/CodderPrince/Network_Packet_Routing_Simulator/blob/main/Network%20Packet%20Routing%20Simulator/UI/image_2025-08-05_17-12-02.png" alt="Screenshot 4" width="300" style="margin:5px;"/>
  <br/>
  <img src="https://github.com/CodderPrince/Network_Packet_Routing_Simulator/blob/main/Network%20Packet%20Routing%20Simulator/UI/image_2025-08-05_17-12-39.png" alt="Screenshot 5" width="300" style="margin:5px;"/>
</div>

---

## 🛠️ Technologies Used

| Technology | Usage                                 |
|------------|-------------------------------------|
| C++        | Core algorithm, console simulation  |
| Windows API (Sleep) | Timing and delays in C++      |
| Python     | GUI, algorithm implementation       |
| Tkinter    | Python GUI framework                 |
| heapq      | Python priority queue (Dijkstra)    |
| time       | Animation delays in Python           |

---

## 🚀 Getting Started

### C++ Version

1. Compile the source:

```bash
g++ -o dijkstra dijkstra.cpp
````

2. Run the executable:

```bash
./dijkstra
```

3. Input your graph details and watch the stepwise output in the console.

---

### Python Version

1. Run the Python script (requires Python 3):

```bash
python network_simulator.py
```

2. Use the GUI to enter graph nodes, edges, weights, source, and destination.

3. Visualize the animated shortest path packet routing.

---

## 📖 Sample Input Format (C++ and Python)

```
7 10
1 2 3
1 3 1
2 3 7
2 4 5
3 4 2
3 5 4
4 6 6
5 6 1
5 7 8
6 7 3
1 7
```

* First line: number of nodes and edges
* Next lines: edges (from to weight)
* Last line: source and destination nodes

---

## 💡 Tips for Usage

* For the C++ version, the console outputs the internal steps and routing updates, helping to debug or understand Dijkstra’s behavior.
* The Python version’s GUI shows a colorful, animated representation for better visualization and learning.

---

## 💬 Developer Info

**Md. An Nahian Prince**
Department of CSE, Begum Rokeya University, Rangpur
🌐 [GitHub – CodderPrince](https://github.com/CodderPrince)

---

## 📌 License

Open-source and free for educational use. Contributions and forks are welcome.

---

⭐ *If you find this project helpful, please star the repository!*
📤 *Feel free to share it with peers or anyone interested in network routing algorithms.*

```
©️ 2025, 𝗠𝗱. 𝗔𝗻 𝗡𝗮𝗵𝗶𝗮𝗻 𝗣𝗿𝗶𝗻𝗰𝗲
```

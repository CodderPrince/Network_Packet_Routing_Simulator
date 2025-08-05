/*
Dijkstra's Algorithm
Single Pair Shortest Path
T.C: O((V + E)logV)
S.C: O(V + E)
*/

#include <bits/stdc++.h>
#include <windows.h>

using namespace std;

#define MX 105
#define INF 1e8

struct node
{
    int node;
    int cost;
};

vector<node> Graph[MX];
bool vis[MX];
int dist[MX];
int parent[MX];

void reset()
{
    for (int i = 0; i < MX; i++)
    {
        Graph[i].clear();
        vis[i] = false;
        dist[i] = INF;
        parent[i] = -1;
    }
}

class cmp
{
public:
    bool operator()(node &A, node &B)
    {
        return A.cost > B.cost;
    }
};

void dijkstra(int source)
{
    priority_queue<node, vector<node>, cmp> PQ;
    dist[source] = 0;
    PQ.push({source, 0});

    cout << "\nStarting Dijkstra from node " << source << "...\n";

    while (!PQ.empty())
    {
        node current = PQ.top();
        PQ.pop();

        int u = current.node;
        int cost = current.cost;

        if (vis[u])
            continue;

        vis[u] = true;
        cout << "Visiting node " << u << " with current cost " << cost << "\n";

        for (auto &edge : Graph[u])
        {
            int v = edge.node;
            int w = edge.cost;

            if (!vis[v] && dist[u] + w < dist[v])
            {
                dist[v] = dist[u] + w;
                parent[v] = u;
                PQ.push({v, dist[v]});
                cout << "  Updated distance of node " << v << " to " << dist[v] << " via node " << u << "\n";
            }
        }
    }
}

vector<int> reconstructPath(int src, int dest)
{
    vector<int> path;
    for (int at = dest; at != -1; at = parent[at])
        path.push_back(at);
    reverse(path.begin(), path.end());
    if (path[0] == src)
        return path;
    return {};
}

void simulatePacketMovement(const vector<int> &path)
{
    cout << "\nSimulating packet movement from source to destination...\n";
    for (int i = 0; i < path.size(); i++)
    {
        cout << "Packet at router " << path[i];
        if (i != path.size() - 1)
            cout << " -> moving to router " << path[i + 1];
        cout << "\n";

        Sleep(700);
    }
    cout << "Packet reached destination.\n";
}

int main()
{
    reset();

    int nodes, edges;
    cout << "Enter number of routers (nodes) and links (edges): ";
    cin >> nodes >> edges;

    cout << "Enter edges in format: from to weight\n";
    for (int i = 1; i <= edges; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        Graph[u].push_back({v, w});
        Graph[v].push_back({u, w});
    }

    int source, destination;
    cout << "Enter source and destination routers: ";
    cin >> source >> destination;

    dijkstra(source);

    cout << "\n--- Final Distances from Source " << source << " ---\n";
    for (int i = 1; i <= nodes; i++)
    {
        cout << "Router " << i << ": ";
        if (dist[i] == INF)
            cout << "UNREACHABLE\n";
        else
            cout << dist[i] << "\n";
    }

    vector<int> path = reconstructPath(source, destination);
    if (path.empty())
    {
        cout << "\nNo path found from " << source << " to " << destination << ".\n";
    }
    else
    {
        cout << "\nShortest Path: ";
        for (int i = 0; i < path.size(); i++)
        {
            cout << path[i];
            if (i != path.size() - 1)
                cout << " -> ";
        }
        cout << "\n";

        simulatePacketMovement(path);
    }

    return 0;
}

/*
Sample Input:
5 6
1 2 2
1 3 1
2 3 1
1 4 3
4 5 2
5 3 5
1 5
*/

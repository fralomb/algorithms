## example Breadth First Search

import queue;

starting_node = 0;
#  complexity  => O( #vertices + #edges )
graph = [
    [9, 7, 11],
    [10, 8],
    [12, 3],
    [2, 4, 7],
    [3],
    [6],
    [7, 5],
    [6, 3, 0, 11],
    [12, 1, 9],
    [10, 8, 0],
    [1, 9],
    [0, 7],
    [8, 2]
]
visited = [False for i in graph];
shortest_path = [None for i in graph];
q = queue.Queue();

def solve_bfs(start, end):
    print("Starting from node " + str(start));
    q.put(start);
    shortest_path[start] = 0;


    while not q.empty():
        curr = q.get();
        if not visited[curr]:
            ## make some processing
            visited[curr] = True;
            shortest_path[curr] = start;
            print("Processing node: " + str(curr));
            
        for next in graph[curr]:
            if not visited[next]:
                print("Adding neighbour " + str(next));
                q.put(next);

def print_path(computed_path):
    path = "";
    for index, item in enumerate(computed_path):
        if index == len(computed_path) - 1:
            path += str(item);
        else:
            path += str(item) + " -> ";
    print(path);


def bfs(start_node, end_node):
    solve_bfs(start_node);

bfs(0, len(graph)-1)
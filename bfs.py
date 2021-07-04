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
shortestp = [None for i in graph];
prev = [None for i in graph];
q = queue.Queue();

def getShortestPath(start, end):
    revertedPath=[];

    revertedPath.append(end);
    head = prev[end];
    while head != None:
        revertedPath.append(head);
        head = prev[head];

    revertedPath.reverse()
    if revertedPath[0] == start:
        return revertedPath;
    else:
        return []


def bfs(start, end):
    print("Starting from node " + str(start));
    q.put(start);

    while not q.empty():
        curr = q.get();
        if not visited[curr]:
            ## make some processing
            visited[curr] = True;
            print("Processing node: " + str(curr));
            prev_node = prev[curr];
            if prev_node == None:
                shortestp[curr] = 0;
            else:
                shortestp[curr] = shortestp[prev_node] + 1;
            print("Current cost: " + str(shortestp[curr]));
            if curr == end:
                print("End node reached " + str(end));
                break;
             
        for next in graph[curr]:
            if not visited[next]:
                print("Adding neighbour " + str(next));
                q.put(next);
                prev[next] = curr;
    print(getShortestPath(start, end));





bfs(0, 4)
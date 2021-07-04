## example Depth First search single graph

starting_node = 0;
#  complexity  => O( #vertices + #edges )
graph = [
    [1, 9],
    [0, 8],
    [3],
    [2, 4, 5, 7],
    [3],
    [3, 6],
    [5, 7],
    [8, 10, 11, 3],
    [1, 9, 7],
    [0, 8],
    [7, 11],
    [10, 7]
]
visited = [False for i in graph];


def dfs(current_node):
    if visited[current_node]:
        print("node " + str(current_node) + " already visited");
        return;
    print("index: " + str(current_node));
    visited[current_node] = True;

    for neighbour in graph[current_node]:
        dfs(neighbour);


# start search
dfs(starting_node);
## example connected components

starting_node = 0;
#  complexity  => O( #vertices + #edges )
graph = [
    [4, 13, 8, 14],
    [5],
    [15, 9],
    [9],
    [0, 8],
    [1, 16, 17],
    [11, 7],
    [6, 11],
    [4, 0, 14],
    [3, 2, 15],
    [15],
    [6, 7],
    [],
    [0, 14],
    [0, 13, 8],
    [10, 2, 9],
    [5],
    [5]
]
visited = [False for i in graph];
labeled = [False for i in graph];

def labelNodes():
    label = 0;
    for index, links in enumerate(graph):
        if visited[index]:
            continue;
        label += 1;
        dfs(index, label);
        print(label, findNodesWith(label))

def findNodesWith(searchedLabel):
    nodes = [];
    for index, label in enumerate(labeled):
        if label == searchedLabel:
            nodes.append(index);
    return nodes

def dfs(current_node, label):
    if visited[current_node]:
        print("node " + str(current_node) + " already visited");
        return;
    labeled[current_node] = label;
    print("index: " + str(current_node));
    visited[current_node] = True;

    for neighbour in graph[current_node]:
        dfs(neighbour, label);
    
# start search
labelNodes();
import os

parent_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
inputs = "inputs/day11-data.txt"
file_path = os.path.join(parent_dir, inputs)

server_graph = {}
with open(file_path, "r") as fp:
    for line in fp.readlines():
        node = line.split(":")[0]
        neighbors = line.split(":")[1].split()
        server_graph[node] = neighbors


def dfs(node, visited):
    paths = 0
    for neighbor in server_graph[node]:
        if neighbor in visited:
            continue
        if neighbor == "out":
            paths += 1
            continue

        new_visited = visited.copy()
        new_visited.add(neighbor)
        paths += dfs(neighbor, new_visited)

    return paths


print(dfs("you", set()))

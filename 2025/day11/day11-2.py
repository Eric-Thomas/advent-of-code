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


def dfs(node, visited, target, memo):
    if node in memo:
        return memo[node]
    paths = 0
    for neighbor in server_graph[node]:
        if neighbor == target:
            paths += 1
            continue
        if neighbor in visited or neighbor == "out":
            continue

        new_visited = visited.copy()
        new_visited.add(neighbor)
        paths += dfs(neighbor, new_visited, target, memo)

    memo[node] = paths
    return paths


svr_dac = dfs("svr", set(), "dac", {})
dac_fft = dfs("dac", set(), "fft", {})
fft_out = dfs("fft", set(), "out", {})
svr_fft = dfs("svr", set(), "fft", {})
fft_dac = dfs("fft", set(), "dac", {})
dac_out = dfs("dac", set(), "out", {})

print((svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out))

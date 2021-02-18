# input  arranged

nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'z']
heuristic_value = [14, 12, 11, 6, 4, 11, 0]
starting_node = 'a'
target_node = 'z'
connected_nodes = ['ab', 'ac', 'be', 'bf', 'cd', 'ce', 'de', 'ez', 'fz']
edge_value = [4, 3, 12, 5, 7, 10, 2, 5, 16]


# input  un-arranged

# nodes = ['a', 'b', 'f', 'z', 'e', 'd', 'c']
# heuristic_value = [14, 12, 11, 0, 4, 6, 11]
# connected_nodes = ['ab', 'bf', 'fz', 'be', 'ez', 'ac', 'ce', 'cd', 'de']
# edge_value = [4, 5, 16, 12, 5, 3, 10, 7, 2]
# starting_node = 'a'
# target_node = 'z'


def compare_and_remove(path_cost, path):
    minimum = min(path_cost)
    min_index = path_cost.index(minimum)
    shortest_path = path[min_index]
    path_cost.remove(path_cost[min_index])
    path.remove(path[min_index])
    return shortest_path


def from_start(curr, records, rec_val):
    summation = 0
    for i in range(0, len(curr) - 1, 1):
        c_path = curr[i] + curr[i + 1]
        if c_path in records:
            c_index = records.index(c_path)
            summation += rec_val[c_index]
    return summation


found_paths = []
found_paths_cost = []
new_current_path = ''
goal_node_paths = []
goal_nodes_costs = []

current_path = starting_node
print("found paths : " + str(found_paths))
print("found paths costs :" + str(found_paths_cost))
print("current path = " + current_path)

while True:
    for access in connected_nodes:
        if current_path[-1:] in access[0]:
            new_current_path = current_path + access[-1]
            if current_path == starting_node:
                total_cost = (0 + edge_value[connected_nodes.index(new_current_path)]
                              + heuristic_value[nodes.index(access[-1])])
            else:
                total_cost = (from_start(new_current_path[0:-1], connected_nodes, edge_value)
                              + heuristic_value[nodes.index(access[-1])]
                              + edge_value[connected_nodes.index(new_current_path[-2:])])
            if new_current_path[-1] == target_node:
                print("Target path: " + new_current_path)
                goal_node_paths.append(new_current_path)
                goal_nodes_costs.append(total_cost)
            else:
                found_paths.append(new_current_path)
                found_paths_cost.append(total_cost)

    if len(found_paths) == 0:
        break
    else:
        print(found_paths)
        print(found_paths_cost)
        current_path = compare_and_remove(found_paths_cost, found_paths)
        print("Current path: " + current_path)

print(goal_node_paths)
print(goal_nodes_costs)

print("Shortest path from " + starting_node + " to " + target_node + " = "
      + goal_node_paths[goal_nodes_costs.index(min(goal_nodes_costs))])

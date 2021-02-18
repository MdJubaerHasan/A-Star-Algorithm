# input  arranged

nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'z']  # names of nodes
heuristic_value = [14, 12, 11, 6, 4, 11, 0]  # heuristic value of nodes nodes sequential tp nodes[]
starting_node = 'a'
target_node = 'z'
connected_nodes = ['ab', 'ac', 'be', 'bf', 'cd', 'ce', 'de', 'ez', 'fz']  # name of connected nodes
edge_value = [4, 3, 12, 5, 7, 10, 2, 5, 16]  # edge values of connected nodes sequentially


# This method is called for comparing and removing the minimal path value from the found_paths_cost = []
def compare_and_remove(path_cost, path):
    minimum = min(path_cost)  # find minimum from found_paths_cost = [] when passed in argument
    min_index = path_cost.index(minimum)  # find index of that minimum value
    shortest_path = path[min_index]  # mark that as current shortest path
    path_cost.remove(path_cost[min_index])  # remove the shortest path from found_paths_cost = []
    path.remove(path[min_index])  # remove the shortest path from found_paths = []
    return shortest_path  # return the current shortest path


# This method is called for calculating the total path value from start to the previous node of the current node
def from_start(curr, records, rec_val):
    # Suppose current path is a->b->c->d->e, and current visiting node is 'e'
    # we can segment this and calculate the value of a->b, b->c, c->d by matching substring with connected_nodes []
    # and getting their corresponding edge cost from edge_value [] using index
    summation = 0
    for i in range(0, len(curr) - 1, 1):
        c_path = curr[i] + curr[i + 1]  # a+b, b+c ...
        if c_path in records:
            c_index = records.index(c_path)  # getting index of the segment from connected_nodes []
            summation += rec_val[c_index]  # adding the values on the go
    return summation  # returning the summation for more calculation later


found_paths = []  # keeps the path names for visiting and comparing
found_paths_cost = []  # keeps the path value for visiting and comparing
new_current_path = ''
goal_node_paths = []  # keeps the path names that reached goal node
goal_nodes_costs = []  # keeps the path values that reached goal node

current_path = starting_node  # Staring from node 'a'
print("found paths : " + str(found_paths))
print("found paths costs :" + str(found_paths_cost))
print("current path = " + current_path)

while True:
    for access in connected_nodes:  # access is the names of connected nodes
        if current_path[-1:] in access[0]:  # as in a path like a->b->c, 'c' is the current node, always from the last

            # so we have to find where we can go from 'c'
            # as access contains the name of the connected nodes, we can easily find that from its index[0]
            # because , fo example, 'ce', means c->e, 'ce' is an array itself, and 'c' is the index 0 of it

            new_current_path = current_path + access[-1]  # found 'c', now we have to add 'e' part
            # as always it'll be one digit from the last
            if current_path == starting_node:  # this will happen only once, this is to make sure g(starting node) = 0
                # is used to calculate the path
                total_cost = (0 + edge_value[connected_nodes.index(new_current_path)]
                              + heuristic_value[nodes.index(access[-1])])
                # here 0 is the g(starting node)
                # here edge_value[connected_nodes.index(new_current_path)] is value of new current path i.e a->b
                # here heuristic_value[nodes.index(access[-1])] is the heuristic value of 'e' mentioned in line 54
                # this is only considered for first iteration
            else:  # this will happen repetitively after first iteration
                total_cost = (from_start(new_current_path[0:-1], connected_nodes, edge_value)
                              + heuristic_value[nodes.index(access[-1])]
                              + edge_value[connected_nodes.index(new_current_path[-2:])])

                # here from_start(new_current_path[0:-1], connected_nodes, edge_value)
                # is calculating the total value of all the nodes from the start
                # to one less, because we will calculate g(n) of the current node and add with it
                # here heuristic_value[nodes.index(access[-1])] is the heuristic value of 'e' mentioned in line 54
                # here edge_value[connected_nodes.index(new_current_path[-2:])] is calculating the g(n) of the current
                # node , as it's between last 2 nodes, that's why -2 is written .
                # for example , a->b->c->d is path, from_start() method already calculated total of (a->b,b-c)
                # so, c->d will be calculated by edge_value[connected_nodes.index(new_current_path[-2:])], aka g(d)

            if new_current_path[-1] == target_node:  # here we are checking if the last node of the path is target
                # if we reach the target node, we add that to the goal_node_path
                # and their total cost to the goal_nodes_costs for finding shortest path later
                print("Target path: " + new_current_path)
                goal_node_paths.append(new_current_path)
                goal_nodes_costs.append(total_cost)
            else:  # if we haven't reached goal node yet, we add the path value and total cost of
                # the path in the array named found_paths [] for traversing and computing later
                found_paths.append(new_current_path)
                found_paths_cost.append(total_cost)

    if len(found_paths) == 0:  # if there is no more path left in found path , means we already visited all the
        # possible nodes, we'll no longer continue iteration and break here
        break
    else:  # if there are elements in found_paths[] array, means we can traverse more
        print(found_paths)  # print remaining paths
        print(found_paths_cost)  # print he cost of those paths sequentially
        current_path = compare_and_remove(found_paths_cost, found_paths)  # here we are comparing the minimal
        # path from the found_paths [] , taking them out for traversing
        print("Current path: " + current_path)  # printing the currently traversing path

print(goal_node_paths)  # printing all the available paths to the goal
print(goal_nodes_costs)  # printing values of all the paths that reaches goal node

print("Shortest path from " + starting_node + " to " + target_node + " = "
      + goal_node_paths[goal_nodes_costs.index(min(goal_nodes_costs))])
# here we are comparing to find the minimum value from all the paths that reached goal node, keep it's index to find
# the path name and finally print the name.
# Thank You for reading patiently 😊

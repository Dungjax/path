from heapq import heappush, heappop
from common import grid, directions_by_position, directions_by_name, directions_match, GRID_SIZE
from pipe import Node, Pipe, StartPipe, EndPipe, pipes

def find_using_astar(start_node : StartPipe, goal_node : EndPipe):
    pipes.clear()
    grid[start_node.position] = start_node
    grid[goal_node.position] = goal_node
    open_list = []
    closed_set = set()

    start_next_direction = directions_by_name.get(start_node.end_direction)
    start_next_node = Pipe((start_node.position[0] + start_next_direction[0], start_node.position[1] + start_next_direction[1]))

    if grid.get(start_next_node.position):
        return None

    goal_next_direction = directions_by_name.get(goal_node.start_direction)
    goal_next_node = Pipe((goal_node.position[0] + goal_next_direction[0], goal_node.position[1] + goal_next_direction[1]))
    if grid.get(goal_next_node.position):
        return None
    goal_next_node.end_direction = directions_match.get(goal_node.start_direction)

    goal_next_node.g_cost = 0
    goal_next_node.f_cost = heuristic(goal_next_node, start_next_node)
    
    heappush(open_list, goal_next_node)
    
    for step in range(500):
        current_node = heappop(open_list)

        closed_set.add(current_node.position)
        
        if current_node.position == start_next_node.position:
            current_node.start_direction = directions_match.get(start_node.end_direction)
            return retrace_path(current_node)
        
        for neighbor in get_neighbors(current_node):
            if neighbor.position in closed_set:
                continue
            
            new_g_cost = current_node.g_cost + 1 # 1 is movement cost to neighbor
            
            if new_g_cost < neighbor.g_cost:
                neighbor.g_cost = new_g_cost
                neighbor.h_cost = heuristic(neighbor, start_next_node)
                neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                neighbor.parent = current_node

                if neighbor not in open_list:
                    heappush(open_list, neighbor)
    
    return None

def heuristic(current_node, goal):
    return abs(current_node.position[0] - goal.position[0]) + abs(current_node.position[1] - goal.position[1])

def get_neighbors(current_node):
    neighbors = []
    
    for direction in directions_by_position.keys():
        
        neighbor_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])
        
        if 0 <= neighbor_position[0] <= GRID_SIZE and 0 <= neighbor_position[1] <= GRID_SIZE and not grid.get(neighbor_position):
            neighbor = Pipe(neighbor_position)
            neighbors.append(neighbor)

    return neighbors

def get_direction(current_node, other):
    direction = (current_node.position[0] - other.position[0], current_node.position[1] - other.position[1])

    return directions_by_position.get(direction)

def retrace_path(current_node):
    path = []

    while current_node:
        path.append(current_node)
        pipes[current_node.position] = current_node

        if current_node.parent:
            current_node.parent.start_direction = get_direction(current_node, current_node.parent)
            current_node.end_direction = directions_match.get(current_node.parent.start_direction)

        current_node.set_image()
        current_node = current_node.parent
    
    return path

# result = find_using_astar(StartPipe((7, 13), "D"), EndPipe((8, 4), "U"))


# for r in result:
#     print(r.position, r.start_direction, r.end_direction)

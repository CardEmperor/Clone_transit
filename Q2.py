"""
Enter the solution for Q2 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""


def bidirectional_dij(source: int, destination: int, graph_object) -> int:
    """
    Bi-directional Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1

    try:
    # Enter your code here
    startsource = [Queue(source, 0.0)]   # Creating initial start node for forward search using HeapQ and setting its value to 0.0
    startdestination = [Queue(destination, 0.0)]   # Creating initial start node for forward search using HeapQ and setting its value to 0.0

    goal_source = set()
    goal_destination = set()

    pre_source = dict()
    pre_destination = dict()
    dist_source = dict()                                                 # Dictionary to store distance from source to target
    dist_destination = dict()                                                 # Dictionary to store distance from target to source

    v_dist = {'weight': math.inf}                                         # sourceetting other vertex initial distance to inf
    node = {'weight': None}


    pre_source[source] = None
    pre_destination[destination] = None
    dist_source[source] = 0.0
    dist_destination[destination] = 0.0
    def update(v, weight,goal):
        if v in goal:
            distance = dist_destination[v] + weight
            if v_dist['weight'] > distance:
                v_dist['weight'] = distance
                node['weight'] = v

    while startsource and startdestination:
        if dist_source[startsource[0].v] + dist_destination[startdestination[0].v] >= v_dist['weight']:
            return reverse_traversal(node['weight'], pre_source, pre_destination)

        if len(startsource) + len(goal_source) < len(startdestination) + len(goal_destination):
            C = hq.heappop(startsource).v                #Pop the smallest item off the heap, maintaining the heap invariant.
            goal_source.add(C)                                                                             #C is current node
            for fwd in graph_object[C]:
                if fwd in goal_source:
                    continue
                cur_dist = dist_source[C] + graph_object[C][fwd]['weight']
                if fwd not in dist_source or cur_dist < dist_source[fwd]:
                    dist_source[fwd] = cur_dist
                    pre_source[fwd] = C
                    hq.heappush(startsource, Queue(fwd, cur_dist))
                    update(fwd, cur_dist, goal_destination)
        else:
            C = hq.heappop(startdestination).v                # Pop the smallest item off the heap, maintaining the heap invariant
            goal_destination.add(C)
            for back in graph_object[C]:
                if back in goal_destination:
                    continue
                cur_dist = dist_destination[C] + graph_object[back][C]['weight']
                if back not in dist_destination or cur_dist < dist_destination[back]:
                    dist_destination[back] = cur_dist
                    pre_destination[back] = C
                    hq.heappush(startdestination, Queue(back, cur_dist))
                    update(back, cur_dist, goal_source)

    return []
    def distance(G, path):
    dist = 0.0
    tot_v = len(path) -1  #Total Number of Vertex minus 1
    for i in range(tot_v):
        dist += G[path[i]][path[i + 1]]['weight']
    return dist
    
    shortest_path_distance = distance(G_to_dict, bi_path)
    
    
        return shortest_path_distance
    except:
        return shortest_path_distance

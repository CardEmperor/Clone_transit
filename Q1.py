"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""
import pandas as pd
import numpy as np
import sys

df = pd.read_csv("/content/ChicagoSketch_net.txt",delimiter="\t")
df1 = df.dropna(how='all', axis='columns')

init_node = df1["init_node"]
term_node = df1["term_node"]
length = df1["length"]

def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    try:
        # Enter your code here
        def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph_object = self.construct_graph_object(nodes, init_graph)
        
        def construct_graph_object(self, nodes, init_graph):
            '''
            This method ensures symmetrical graph_object. If there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
            '''
            graph_object = {}
            for node in nodes:
                graph_object[node] = {}

            graph_object.update(init_graph)

            for node, edges in graph_object.items():
                for adjacent_node, value in edges.items():
                    if graph_object[adjacent_node].get(node, False) == False:
                        graph_object[adjacent_node][node] = value

        return graph_object
    
        def get_nodes(self):
            "Returns the nodes of the graph_object."
            return self.nodes

        def get_outgoing_edges(self, node):
            "Returns the neighbors of a node."
            connections = []
            for out_node in self.nodes:
                if self.graph_object[node].get(out_node, False) != False:
                    connections.append(out_node)
            return connections

        def value(self, node1, node2):
            "Returns the value of an edge between two nodes."
            return self.graph_object[node1][node2]
            return graph_object
        except:
            return graph_object


def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        # Enter your code here
        def dijkstra(graph_object, source):
          unvisited_nodes = list(graph_object.get_nodes())
          shortest_path = {}
          previous_nodes = {}
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
          max_value = sys.maxsize
          for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0   
          shortest_path[source] = 0

          while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes: # Iterate over the nodes
              if current_min_node == None:
                current_min_node = node
              elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = graph_object.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
               tentative_value = shortest_path[current_min_node] + graph_object.value(current_min_node, neighbor)
               if tentative_value < shortest_path[neighbor]:
                  shortest_path[neighbor] = tentative_value
            # We also update the best path to the current node
                  previous_nodes[neighbor] = current_min_node  

            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)
    
  return previous_nodes, shortest_path
        return shortest_path_distance
    except:
        return shortest_path_distance

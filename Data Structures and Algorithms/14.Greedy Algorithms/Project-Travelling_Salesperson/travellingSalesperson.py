import random
from random import randrange
from Graph import Graph
from Vertex import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed=False):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# Define your functions below:
def check_visited(visited_tracker):
  for vertex in visited_tracker:
    if visited_tracker[vertex] == "unvisited":
      return False
  return True

def travelling_salesperson(graph):
  ts_path = ""
  visited_tracker = { v: "unvisited" for v in graph.graph_dict}

  current_vertex = random.choice(list(graph.graph_dict))
  visited_tracker[current_vertex] = "visited"
  ts_path += current_vertex
  visited_all = check_visited(visited_tracker)
  while not visited_all:
    current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
    current_vertex_edge_weights = {}
    for edge in current_vertex_edges:
      current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_weight(edge)

      found_next_vertex = False
      next_vertex = ""
      
      while not found_next_vertex:
        if current_vertex_edge_weights is None:
          break
        
        next_vertex = min(current_vertex_edge_weights, key=current_vertex_edge_weights.get)
        
        if visited_tracker[next_vertex] == "visited":
          current_vertex_edge_weights.pop(next_vertex)
        else:
          found_next_vertex = True

        if current_vertex_edge_weights is None:
          visited_all = True
        else:
          current_vertex = next_vertex
          visited_tracker[current_vertex] = "visited"
          ts_path += current_vertex
    visited_all = check_visited(visited_tracker)
  print(ts_path)




route = build_tsp_graph()
travelling_salesperson(route)
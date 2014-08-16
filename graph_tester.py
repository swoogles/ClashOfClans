from graph_tool.all import *
import random

# from Queue import Queue
ug = Graph(directed=False)
ug.set_directed(False)
assert(ug.is_directed() == False)
vertices = []
g1 = Graph()
v1 = ug.add_vertex()
v2 = ug.add_vertex()
e = ug.add_edge(v1, v2)
vertices.append(v1)
vertices.append(v2)

for i in range(8):
    vOld = v1
    v1 = ug.add_vertex()
    v2 = ug.add_vertex()
    v3 = ug.add_vertex()
    e = ug.add_edge(v1, v2)
    e = ug.add_edge(v2, v3)

    e = ug.add_edge(random.choice(vertices), v2)
    e = ug.add_edge(random.choice(vertices), v3)

    vertices.append(v1)
    vertices.append(v2)
    vertices.append(v3)

graph_draw(ug, vertex_text=ug.vertex_index, vertex_font_size=18, output_size=(200, 200))
# graph_draw(ug, vertex_text=ug.vertex_index, vertex_font_size=18, output_size=(200, 200), output="two-nodes.png")

# while 1:
# 
#     frontier = Queue()
#     frontier.put(start)
#     visited = {}
#     visited[start] = True
# 
#     while not frontier.empty():
#         current = frontier.get()
#         for next in graph.neighbors(current):
#             if next not in visited:
#                 frontier.put(next)
#                 visited[next] = True
#                 print("cool")

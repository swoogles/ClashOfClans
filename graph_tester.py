from graph_tool.all import *
ug = Graph(directed=False)
ug.set_directed(False)
assert(ug.is_directed() == False)
g1 = Graph()
v1 = ug.add_vertex()
v2 = ug.add_vertex()
e = ug.add_edge(v1, v2)
graph_draw(ug, vertex_text=ug.vertex_index, vertex_font_size=18, output_size=(200, 200))
# graph_draw(ug, vertex_text=ug.vertex_index, vertex_font_size=18, output_size=(200, 200), output="two-nodes.png")
while 1:

    frontier = queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        print("cool")
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

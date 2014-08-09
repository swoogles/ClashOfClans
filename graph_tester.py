from graph_tool.all import *
g = Graph()
ug = Graph(directed=False)
ug = Graph()
ug.set_directed(False)
assert(ug.is_directed() == False)
g1 = Graph()
# ... construct g1 ...
g2 = Graph(g1)                 # g1 and g2 are copies
v1 = g.add_vertex()
v2 = g.add_vertex()
e = g.add_edge(v1, v2)
graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18, output_size=(200, 200))
# graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18, output_size=(200, 200), output="two-nodes.png")
while 1:
    x=1

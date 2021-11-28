import sys
from graph import Graph, Vertex


def create_graph(filename):
    g = Graph()
    prisoner_vertex = None
    exit_vertex = None
    cameras = set()
    vertices = {}
    with open(filename, "r") as graph_file:
        row, col = map(int, graph_file.readline().split())
        for line in graph_file:
            line = line.strip()
            if len(line) == 0: continue
            i, j = map(int, line.split())
            cameras.add((i, j))

    for i in range(row):
        for j in range(col):
            # if (i, j) not in cameras:
            v = Vertex((i, j))
            vertices[(i, j)] = v
            if (i, j) in cameras: v.has_camera = True
            g.add_vertex(v)
            if i == 0 and j == 0: prisoner_vertex = v
            if i == row - 1 and j == col - 1: exit_vertex = v

    for i in range(row):
        for j in range(col):
            if (i, j) in vertices:
                src = vertices[(i, j)]
                north = (i - 1, j)
                if north in vertices: g.add_undirected_edge(src, vertices[north])
                west = (i, j - 1)
                if west in vertices: g.add_undirected_edge(src, vertices[west])
                east = (i, j + 1)
                if east in vertices: g.add_undirected_edge(src, vertices[east])
                south = (i + 1, j)
                if south in vertices: g.add_undirected_edge(src, vertices[south])

    return g, prisoner_vertex, exit_vertex


def count_exit_paths(g, source, exit):
    if exit is source:
        return 1
    elif source.visited or source.has_camera:
        return 0
    else:
        count = 0
        source.visited = True
        for dest in g.adjacency_list[source]:
            count += count_exit_paths(g, dest, exit)
        source.visited = False
        return count


if __name__ == "__main__":
    prison_filename = sys.argv[1]
    prison_graph, prisoner_vertex, exit_vertex = create_graph(prison_filename)
    num_paths = count_exit_paths(prison_graph, prisoner_vertex, exit_vertex)
    print(num_paths)

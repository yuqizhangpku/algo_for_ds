import networkx as nx
import urllib2

homer = urllib2.urlopen('http://people.sc.fsu.edu/~jburkardt/datasets/sgb/homer.dat')
def read_nodes(gfile):
    text = gfile.read().split('\n')
    t = 0
    while text[t] != '':
        t += 1
    node_part = text[:t]
    vertile_part = text[t+1:]  ## In order to delete the lines that begin wihth *
    nodes = []
    for k in range(len(node_part)):
        if node_part[k].split(' ')[0] != '*':
            nodes.append(node_part[k].split(' ')[0])
    return nodes
nodes = read_nodes(homer)
print nodes

homer = urllib2.urlopen('http://people.sc.fsu.edu/~jburkardt/datasets/sgb/homer.dat')
def read_edges(gfile):
    text = gfile.read().split('\n')
    t = 0
    while text[t] != '':
        t += 1
    edge_part = text[t+1:]  ## In order to delete the lines that begin wihth *
    edge = []
    connected = []
    for k in range(len(edge_part) - 1):
        if edge_part[k][0] != '*':
            try:
                connected.extend((edge_part[k].split(':'))[1].split(';'))
            except:
                print edge_part[k].split(':')
    for m in connected:
        i = 0
        while i <= len(m.split(',')) - 1:
            j = i + 1
            while j <= len(m.split(',')) - 1:
                edge.append((m.split(',')[i], m.split(',')[j]))
                j += 1
            i += 1
    return edge
edge = read_edges(homer)
print edge

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edge)


def stack_pop(lst):
    poped = lst[-1]
    lst = lst[:-1]
    return poped


def Search(graph, root):
    # TODO: implement function
    if graph.neighbors(root) == []:
        return [root]   ### REMEMBER To ADD the root as the single element in a component!!!
    else:
        ordered_list = []
        stack_for_found = [root]
        while stack_for_found != []:
            point = stack_for_found[-1]
            stack_for_found.pop(-1)
            if point in ordered_list:
                pass
            else:
                ordered_list.append(point)
                neigh = sorted(graph.neighbors(point), reverse=True)
                for p in neigh:
                    stack_for_found.append(p)
    return ordered_list


def union(a, b):
    return list(set(a) | set(b))

def connected_components(graph):
    components = []
    visited = []
    while list(set(graph.nodes()) - (set(visited))) != []:
        root = sorted(list(set(graph.nodes()) - (set(visited))))[0]
        connected = Search(graph, root)
        components.append(connected)
        print(connected)
        print(len(connected))
        visited = union(visited, connected)
    return components
character_interactions = connected_components(G)

component_sizes = [len(c) for c in character_interactions]
print "There are 12 connected components in the Iliad:", len(component_sizes) == 12
print "The giant component has size 542:", max(component_sizes) == 542
print "There are 5 isolated characters:", len([c for c in component_sizes if c == 1]) == 5
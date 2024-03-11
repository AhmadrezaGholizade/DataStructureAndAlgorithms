import random
from A_star_Module import Graph

V = 6
E = 15

if E > V * (V - 1) or E < 1:
    raise ValueError("Invalid E number")
    
g = Graph()
g.random_nodes(V)
g.random_edges(E)

START = random.choice(g.nodes())
GOAL = random.choice(g.nodes())

while GOAL == START:
    GOAL = random.choice(g.nodes())
            
g.show(start = START, destination = GOAL)

# ------ A*

path = Graph.A_star(START, GOAL)

g.show(path = path, start = START, destination = GOAL)
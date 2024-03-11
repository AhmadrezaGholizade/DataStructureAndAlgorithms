import random
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import FancyArrowPatch

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

class Node():
    def __init__(self, position):
        try:
            if not isinstance(position, tuple):
                if len(position) != 2:
                    raise ValueError("Invalid position (should be (x, y))")
        except:
            raise ValueError("Invalid position (should be (x, y))")
        self.position = position
        self.f = None
        self.g = None
        self.h = None
        self.p = None
        self.adj = []
    def f_update(self):
        self.f = self.g + self.h
    def __str__(self):
        return f"Node({self.position[0]}, {self.position[1]})"
    def __repr__(self):
        return f"Node({self.position[0]}, {self.position[1]})"
    def __eq__(self, other):
        return self.position == other.position
    def __hash__(self):
        return hash(self.position)
    def __gt__(self, other):
        return self.f > other.f
    def __lt__(self, other):
        return self.f < other.f
    def __ge__(self, other):
        return self.f >= other.f
    def __le__(self, other):
        return self.f <= other.f
    
class Graph():
    def __init__(self):
        self.V = set()
    def add_V(self, position):
        self.V.add(Node(position))
    def add_E(self, node1, node2):
        if (node1 in self.V) or (node2 in self.V):
            node1.adj.append((node2, round(distance(node2.position, node1.position), 2)))
        else:
            raise ValueError("Invalid Edge")
    def nodes(self):
        return list(self.V)
    def edges(self):
        edges = []
        for n in self.nodes():
            for adj in n.adj:
                edges.append((n, *adj))
        return edges
    def random_nodes(self, Num):
        for i in range(Num):
            self.add_V((round(random.random() * 100, 2), round(random.random() * 100, 2)))
    def random_edges(self, Num):
        temp = list(self.V)
        for i in range(Num):
            n1 = random.choice(temp)
            n2 = random.choice(temp)
            while n2 == n1:
                n2 = random.choice(temp)
            self.add_E(n1, n2)
    def V_x(self):
        return [node.position[0] for node in self.nodes()]
    def V_y(self):
        return [node.position[1] for node in self.nodes()]
    def show(self, path = 0, start = None, destination = None):
        fig, ax = plt.subplots()
        for node in self.nodes():
            node = node.position
            ax.scatter(*node, color = 'olive')
        for edge in self.edges():
            x0, y0 = edge[0].position[0], edge[0].position[1]
            x2, y2 = edge[1].position[0], edge[1].position[1]

            x1, y1, s = move_perpendicular((x0, y0), (x2, y2), 2)

            t = np.linspace(0, 1, 50)
            x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
            y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2

            rand_color = (random.random(), random.random(), random.random())
            ax.plot(x, y, color = (*rand_color, 0.4))
            arrow = FancyArrowPatch((x[-2], y[-2]), (x[-1], y[-1]), arrowstyle='-|>', mutation_scale=12, color = (*rand_color, 0.4))

            ax.add_patch(arrow)
            plt.text(x1, y1, str(round(edge[2])), fontsize = 6, ha='center', va='center', rotation = s * 180 / math.pi , color = rand_color)
        if path == None:
            plt.title("There is no possible path")
        elif isinstance(path, list):
            plt.text(path[0].position[0], path[0].position[1] + 1.6, 'Source', fontsize = 7, va='center', ha='center', color = 'black')
            plt.text(path[-1].position[0], path[-1].position[1] + 1.6, 'Destination', fontsize = 7, ha='center', va='center', color = 'black')
            for i in range(len(path) - 1):
                x0, y0 = path[i].position[0], path[i].position[1]
                x2, y2 = path[i + 1].position[0], path[i + 1].position[1]

                x1, y1, s = move_perpendicular((x0, y0), (x2, y2), 2)

                t = np.linspace(0, 1, 50)
                x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
                y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2

                ax.plot(x, y, ':', color = 'black', label = 'Path')
                arrow = FancyArrowPatch((x[-2], y[-2]), (x[-1], y[-1]), arrowstyle='-|>', mutation_scale=12, color = 'black')
                ax.add_patch(arrow)
            handles, labels = plt.gca().get_legend_handles_labels()
            by_label = dict(zip(labels, handles))
            ax.legend(by_label.values(), by_label.keys())
            plt.title(f"Path Cost: {round(path[-1].g, 2)}")
        if start:
            plt.text(start.position[0], start.position[1] + 1.6, 'Source', fontsize = 7, ha='center', va='center', color = 'black')
            ax.scatter(*start.position, color = 'black')
        if destination:
            plt.text(destination.position[0], destination.position[1] + 1.6, 'Destination', fontsize = 7, ha='center', va='center', color = 'black')
            ax.scatter(*destination.position, color = 'black')
        plt.show()


    def A_star(START, GOAL):
        START.g = 0
        OPEN = MinHeap()
        OPEN.insert(START)
        CLOSED = set()
        while not(OPEN.is_empty()):
            # OPEN.display()
            n = OPEN.extract_min()
            if n == GOAL:
                # print("I've got")
                path = []
                n = n.p
                path.insert(0, GOAL)
                while isinstance(n, Node):
                    path.insert(0, n)
                    # print("path:", n)
                    n = n.p
                return path
            CLOSED.add(n)
            # print(n.adj)
            for m, w in n.adj:
                # print(m)
                if (m in OPEN.heap) or (m in CLOSED):
                    if m.g < (n.g + w):
                        continue
                if m in CLOSED:
                    CLOSED.remove(m)
                OPEN.remove(m)
                m.g = n.g + w
                if m.h == None:
                    m.h = distance(m.position, GOAL.position)
                m.p = n
                m.f_update()
                OPEN.insert(m)
                # print(m, w)

def move_perpendicular(point1, point2, distance):
    # Calculate the midpoint between the two points
    mid_point = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)
    
    # Calculate the vector from point1 to point2
    delta_x = point2[0] - point1[0]
    delta_y = point2[1] - point1[1]
    
    # Calculate the length of the line segment
    length = np.sqrt(delta_x ** 2 + delta_y ** 2)
    
    # Normalize the vector
    unit_x = delta_x / length
    unit_y = delta_y / length
    
    # Calculate the perpendicular vector
    perp_x = -unit_y
    perp_y = unit_x
    
    # Move the midpoint along the perpendicular direction
    new_x = mid_point[0] + distance * perp_x
    new_y = mid_point[1] + distance * perp_y

    s = math.atan(delta_y / delta_x)
    
    return (new_x, new_y, s)

class MinHeap():
    def __init__(self):
        self.heap = []
    
    def is_empty(self):
        return self.heap == []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_item

    def heapify_down(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def remove(self, item):
        try:
            while True:
                i = self.heap.index(item)
                self.heapify_down(i)
                del self.heap[-1]
        except ValueError:
            pass

    def display(self):
        print("Min Heap:", self.heap)



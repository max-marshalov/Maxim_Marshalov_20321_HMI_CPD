##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-02 10:05:26 am
 # @copyright SMTU
 #
import heapq
class LinkedGraph:
    def __init__(self) -> None:
        self._links = []
        self._vertex = []
    
    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)


    def add_link(self, link):
        for edge in self._links:
            if (link.v1 == edge.v2 and link.v2 == edge.v1) or (link.v1 == edge.v1 and link.v2 == edge.v2):
                break
        else:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)
            

       
    
    def find_path(self, start_v, stop_v):
        distances = {}  # Словарь для хранения расстояний от начальной вершины до всех остальных вершин
        previous_vertices = {}  # Словарь для хранения предыдущих вершин образующих кратчайший путь
        queue = []  # Очередь для выбора вершины с минимальным расстоянием

        # Инициализация расстояний
        for vertex in self._vertex:
            distances[vertex] = float('inf')
        distances[start_v] = 0

        # Добавление начальной вершины в очередь
        queue.append((distances[start_v], start_v))
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            # Обновление расстояний
            for link in current_vertex.links:
                neighbor_vertex = link.v2 if current_vertex == link.v1 else link.v1
                distance = current_distance + link.dist
                if distance < distances[neighbor_vertex]:
                    distances[neighbor_vertex] = distance
                    previous_vertices[neighbor_vertex] = current_vertex
                    queue.append((distance, neighbor_vertex))

        # Формирование пути
        path = []
        current_vertex = stop_v
        while current_vertex != start_v:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.append(start_v)
        path.reverse()

        # Возвращаем кратчайший путь и список ребер на этом пути
        edges = []
        for i in range(len(path) - 1):
            v1 = path[i]
            v2 = path[i + 1]
            for link in self._links:
                if (link.v1 == v1 and link.v2 == v2) or (link.v1 == v2 and link.v2 == v1):
                    edges.append(link)
                    break

        return path, edges

# Задание 
Необходимо написать универсальную основу для представления ненаправленных связных графов и поиска в них кратчайших маршрутов. Далее, этот алгоритм предполагается применять для прокладки маршрутов: на картах, в метро и так далее.
Для универсального описания графов, вам требуется объявить в программе следующие классы:

**Vertex** - для представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.);
**Link** - для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.);
**LinkedGraph** - для представления связного графа в целом (карта целиком).

Объекты класса **Vertex** должны создаваться командой:
```Py
v = Vertex()
```
и содержать локальный атрибут:

_links - список связей с другими вершинами графа (список объектов класса Link).

Также в этом классе должно быть объект-свойство (property):

links - для получения ссылки на список _links.

Объекты следующего класса **Link** должны создаваться командой:
```Py
link = Link(v1, v2)
```
где v1, v2 - объекты класса Vertex (вершины графа). Внутри каждого объекта класса Link должны формироваться следующие локальные атрибуты:

_v1, _v2 - ссылки на объекты класса Vertex, которые соединяются данной связью;

_dist - длина связи (по умолчанию 1); это может быть длина пути, время в пути и др.

В классе Link должны быть объявлены следующие объекты-свойства:

v1 - для получения ссылки на вершину v1;

v2 - для получения ссылки на вершину v2;

dist - для изменения и считывания значения атрибута _dist.

Наконец, объекты третьего класса **LinkedGraph** должны создаваться командой:
```Py
map_graph = LinkedGraph()
```

В каждом объекте класса LinkedGraph должны формироваться локальные атрибуты:

_links - список из всех связей графа (из объектов класса Link);

_vertex - список из всех вершин графа (из объектов класса Vertex).

В самом классе LinkedGraph необходимо объявить (как минимум) следующие методы:

def add_vertex(self, v): ... - для добавления новой вершины v в список _vertex (если она там отсутствует);

def add_link(self, link): ... - для добавления новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует);

def find_path(self, start_v, stop_v): ... - для поиска кратчайшего маршрута из вершины start_v в вершину stop_v.

Метод find_path() должен возвращать список из вершин кратчайшего маршрута и список из связей этого же маршрута в виде кортежа: 

([вершины кратчайшего пути], [связи между вершинами])

Поиск кратчайшего маршрута необходимо реализовать через алгоритм Дейкстры поиска кратчайшего пути в связном взвешенном графе.

В методе add_link() при добавлении новой связи следует автоматически добавлять вершины этой связи в список _vertex, если они там отсутствуют.

Проверку наличия связи в списке _links следует определять по вершинам этой связи. Например, если в списке имеется объект:

_links = [Link(v1, v2)]

то добавлять в него новые объекты Link(v2, v1) или Link(v1, v2) нельзя (обратите внимание у всех трех объектов будут разные id, т.е. по id определять вхождение в список нельзя).

**Подсказка**: проверку на наличие существующей связи можно выполнить с использованием функции filter() и указанием нужного условия для отбора объектов.

Однако, в таком виде применять классы для схемы карты метро не очень удобно. Например, здесь нет указаний названий станций, а также длина каждого сегмента равна 1, что не соответствует действительности.

Чтобы поправить этот момент и реализовать программу поиска кратчайшего пути в метро между двумя произвольными станциями, объявите еще два дочерних класса:

class **Station**(Vertex): ... - для описания станций метро;

class **LinkMetro**(Link): ... - для описания связей между станциями метро.

Объекты класса **Station** должны создаваться командой:
```Py
st = Station(name)
```
где name - название станции (строка). В каждом объекте класса Station должен дополнительно формироваться локальный атрибут:

name - название станции метро.

(Не забудьте в инициализаторе дочернего класса вызывать инициализатор базового класса).

В самом классе Station переопределите магические методы __str__() и __repr__(), чтобы они возвращали название станции метро (локальный атрибут name).

Объекты второго класса LinkMetro должны создаваться командой:
```Py
link = LinkMetro(v1, v2, dist)
```
где v1, v2 - вершины (станции метро); dist - расстояние между станциями (любое положительное число).
# Результат работы 
<image src="images/passed.png" alt="Tests passed">

# Листинг кода 
1. ### LinkedGraph.py ###
```python
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
```
2. ### Vertex.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-02 10:05:39 am
 # @copyright SMTU
 #
from core.Link import Link
class Vertex:
    def __init__(self) -> None:
        self.__links = []
    @property
    def links(self) -> list:
        return self.__links
    @links.setter
    def links(self, link: Link):
        self.__links.append(link)
```
3. ### Link.py ###
```python
##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-02 10:05:31 am
 # @copyright SMTU
 #
class Link:
    def __init__(self , v1, v2, dist=1):
        self.__v1 = v1
        self.__v2 = v2
        self.__dist = dist
    @property
    def v1(self):
        return self.__v1
    @property
    def v2(self):
        return self.__v2
    @property
    def dist(self):
        return self.__dist
    @dist.setter
    def dist(self, new_dist):
        self.__dist = new_dist
```

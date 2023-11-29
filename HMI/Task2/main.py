##
# @author Maxim Marshalov <marshalmaxim@gmail.com>
 # @file Description
 # @desc Created on 2023-10-02 10:05:56 am
 # @copyright SMTU
 #
from core.Vertex import Vertex
from core.Link import Link
from core.LinkedGraph import LinkedGraph
from metroServices.LinkMetro import LinkMetro
from metroServices.Station import Station

if __name__ == '__main__':
    map2 = LinkedGraph()
    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()
    map2.add_link(Link(v1, v2))
    map2.add_link(Link(v2, v3))
    map2.add_link(Link(v2, v4))
    map2.add_link(Link(v3, v4))
    map2.add_link(Link(v4, v5))
    # Тесты
    assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
    assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
    map2.add_link(Link(v2, v1))
    assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"
    path = map2.find_path(v1, v5)
    s = sum([x.dist for x in path[1]])
    assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"
    assert issubclass(Station, Vertex) and issubclass(LinkMetro,
                                                      Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"
    map2 = LinkedGraph()
    v1 = Station("1")
    v2 = Station("2")
    v3 = Station("3")
    v4 = Station("4")
    v5 = Station("5")
    map2.add_link(LinkMetro(v1, v2, 1))
    map2.add_link(LinkMetro(v2, v3, 2))
    map2.add_link(LinkMetro(v2, v4, 7))
    map2.add_link(LinkMetro(v3, v4, 3))
    map2.add_link(LinkMetro(v4, v5, 1))
    assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
    assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
    path = map2.find_path(v1, v5)
    assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
    s = sum([x.dist for x in path[1]])
    assert s == 7, "неверная суммарная длина маршрута для карты метро"

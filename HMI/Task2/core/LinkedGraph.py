import Link
class LinkedGraph:
    def __init__(self) -> None:
        self._links = []
        self._vertex = []
    
    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)


    def add_link(self, link):
        link.v1.links.append(link)
        link.v2.links.append(link)
        self.add_vertex(link.v1)
        self.add_vertex(link.v2)
        if link not in self._links:
            self._links.append(link)
            

       
    
    def find_path(self, start_v, stop_v):
        pass

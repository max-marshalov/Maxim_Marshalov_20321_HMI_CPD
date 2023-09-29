class Vertex:
    def __init__(self) -> None:
        self._links = []
    @property
    def links(self):
        return self._links
    @links.setter
    def links(self, link):
        self._links.append(link)

class Link:
    def __init__(self , v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1
    @property
    def v1(self):
        return self._v1
    @property
    def v2(self):
        return self._v2
    @property
    def dist(self):
        return self._dist
    @dist.setter
    def dist(self, new_dist):
        self._dist = new_dist

class Point:
    def __init__(self, id: int, name: str):
        self.name = name
        self.id = id
        self.__neighbors = []

    def add_neighbor(self, p,  d: int, e: float):
        # p - other point on the graph
        # d - distance between the point
        # e angle from the point, positive - right, negative - left
        if len(self.__neighbors) == 0 or len(self.__neighbors) > 0 and p not in [x for x in self.__neighbors[0]]:
            self.__neighbors.append((p, d, e))
            return True
        return False

    def get_neighbors(self):
        return self.__neighbors

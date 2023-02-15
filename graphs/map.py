import vars
from point import Point


class Map:
    def __init__(self):
        self.points = [Point(*x) for x in vars.ps]
        for i, p in enumerate(vars.ps_relations):
            for j, r in enumerate(p):
                if type(r) is tuple:
                    self.points[i].add_neighbor(self.points[j], *r)
        self.start = self.points[0]

    def __get_edeges(self):
        ret = []
        for i, p in enumerate(vars.ps_relations):
            for j, r in enumerate(p):
                if type(r) is tuple:
                    ret.append((i, j))
        return ret

    def __eulerian_path(self):
        edges = self.__get_edeges()
        current_point, prev_point, ret = self.points[0], [], []
        count = 1
        while count > 0:
            for neighbor in current_point.get_neighbors():
                if (current_point.id - 1, neighbor[0].id - 1) in edges:
                    prev_point.append(current_point)
                    edges.remove((current_point.id - 1, neighbor[0].id - 1))
                    edges.remove((neighbor[0].id - 1, current_point.id - 1))
                    current_point = self.points[neighbor[0].id - 1]
                    count += 1
                    break
            else:
                count -= 1
                ret.append(current_point.id)
                current_point = prev_point.pop()
        return ret

    def __dijkstra(self, start=None):
        ret = []
        [ret.append([]) for _ in range(len(vars.ps))]
        visited = []
        n = self.start
        unvisited = list(range(len(vars.ps)))
        if start:
            n = self.points[start - 1]
            ret[start - 1] = [0, start]
        else:
            ret[0] = [0, 1]
        while len(unvisited) > 0:
            for i in n.get_neighbors():
                if i[0].id - 1 in unvisited:
                    pos = i[0].id - 1
                    if len(ret[pos]) != 2:
                        ret[pos].append(i[1] + ret[n.id - 1][0])
                        ret[i[0].id - 1].append(n.id)
                    elif ret[pos][0] > ret[n.id - 1][0] + i[1]:
                        ret[pos][0] = ret[n.id - 1][0] + i[1]
                        ret[pos][1] = n.id
            i_min = [9999, -1]
            unvisited.remove(n.id - 1)
            for i in unvisited:
                if len(ret[i]) > 0 and ret[i][0] < i_min[0]:
                    i_min[1] = i
                    i_min[0] = ret[i][0]
            visited.append(n.id - 1)
            n = self.points[i_min[1]]
        return ret

    def shortest_route(self, start, to):
        if not start:
            start = 0
        dijkstra = self.__dijkstra(start=start)
        route = str(to)
        i = to - 1
        while i != start - 1:
            route += "," + str(dijkstra[i][1])
            i = dijkstra[i][1] - 1
        route = route[::-1]
        return route

    def go_in_all_routes(self):
        ret = "".join([str(x) + "-->" for x in self.__eulerian_path()[::-1]])
        return ret

    def get_commends_route(self, start, to):
        route = self.shortest_route(start, to).split(',')
        commends = []
        i = 0
        current_angle = 0
        while i < len(route) - 1:
            val = vars.ps_relations[int(route[int(i)]) - 1][int(route[int(i) + 1]) - 1]
            commends.append('e ' + str(val[1] - current_angle))
            commends.append('d ' + str(val[0]))
            current_angle += val[1]
            i += 1
        return commends


if __name__ == '__main__':
    t = Map()
    print("rout that goes in all ")
    print(t.get_commends_route(2, 5))


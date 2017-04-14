
class CellularAutmaton1d:

    def __init__(self, array_len, num_states, num_neighbors, transitions):
        self.array = [-1 for i in range(array_len)]
        self.num_states = num_states
        self.num_neighbors = num_neighbors
        self.transition = transitions

    def random_initialize(self):
        pass

    def update(self):
        pass

    def dump(self):
        pass


if __name__ == "__main__":
    a = CellularAutmaton1d(70, 2, 1, [0, 1, 1, 0])
    for i in range(100):
        a.update()
        a.dump()

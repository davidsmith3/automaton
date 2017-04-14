import collections
import random


class CellularAutmaton1d:

    def __init__(self, array_len, num_states, num_neighbors, transitions):
        self.array = [-1 for i in range(array_len)]
        self.num_states = num_states
        self.num_neighbors = num_neighbors
        self.transition = transitions

    def random_initialize(self):
        self.array = [random.randint(0, (self.num_states-1)) for i in self.array]

    def get_slice(self, start, end):
        dq = collections.deque(self.array)
        dq.rotate(start*-1)
        return [dq[i] for i in range(end - start)]

    def update(self):
        t_array = []
        for i, v in enumerate(self.array):
            start_index = i - self.num_neighbors
            end_index = i + self.num_neighbors + 1
            slice = self.get_slice(start_index, end_index)
            sum_neighbors = sum(slice)
            t_array.append(self.transition[sum_neighbors])
            # print('Index: {} Val: {} Start: {} End: {} Slice: {} Sum: {} Result: {}'.format(i, v, start_index, end_index, slice, sum_neighbors, t_array[-1]))
        self.array = t_array

    def dump(self):
        if self.num_states <= 10:
            print(''.join([str(i) for i in self.array]))
        else:
            print(self.array)


if __name__ == "__main__":
    a = CellularAutmaton1d(70, 2, 1, [0, 1, 1, 0])
    a.random_initialize()
    a.dump()
    for i in range(100):
        a.update()
        a.dump()

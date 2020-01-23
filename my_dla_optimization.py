"""
My speed optimization of diffusion limited aglomeration (DLA)
inspired by a question on code-review:
https://codereview.stackexchange.com/questions/235883/how-to-increase-the-efficiency-of-dla-algorithm

@author: Nathanael Jöhrmnann
"""
from collections import defaultdict
from multiprocessing.pool import Pool
from multiprocessing.spawn import freeze_support
from typing import Optional, List

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multinomial


def main():
    dla_simulator = DLASimulator(area_size=(200, 200), max_steps=200) # , max_factor=0.5)  # max_steps is 167 for 500x500
    dla_simulator.simulate(particles=
                           30)
    dla_simulator.plot()
    print("done")


class DLASimulator:
    def __init__(self, area_size: tuple, max_steps: int, initial_particles_pos: Optional[List[tuple]] = None, max_factor=1.0):
        self.area_size = area_size
        if initial_particles_pos is None:
            initial_particles_pos = [(area_size[0] // 2, area_size[1] // 2)]
        self.initial_particles_pos = initial_particles_pos
        self.distance_matrix = None  # only to help code completion
        self.init_distance_matrix()
        self.set_stick_particles(self.initial_particles_pos)

        self.max_steps = min(max_steps, self.distance_matrix.max())  # no need to precalculate more than max distance
        self.max_steps = max(int(self.max_steps*max_factor), 1)  # no need to precalculate more than max distance

        self.list_of_position_probability_lists = generate_list_of_position_probability_lists(self.max_steps)

    def simulate(self, particles: int = 1000, reset: bool = False):
        print("start simulation")
        if reset:
            self.init_distance_matrix()
            self.set_stick_particles(self.initial_particles_pos)
        for _ in range(particles):
            particle = self.get_new_particle()
            self.simulate_particle(particle)
            print(f"particle {_} sticked")

    def simulate_particle(self, particle):
        while True:
            distance = self.distance_matrix[particle[1], particle[0]]
            if distance == 0:
                self.set_stick_particle(particle)
                break
            elif distance < 0:
                # raise Exception("There is already a particle on This position")
                break
            else:
                pos_x, pos_y = self.get_random_step(distance)
                particle[0] = min(max(particle[0] + pos_x, 0), self.area_size[0]-1)
                particle[1] = min(max(particle[1] + pos_y, 0), self.area_size[1]-1)

    # calc distance to border for all positions (allowed steps for each position)
    def init_distance_matrix(self):
        size_x, size_y = self.area_size
        self.distance_matrix = np.zeros(self.area_size, np.int16)

        for pos_x in range(size_x):
            for pos_y in range(size_y):
                self.distance_matrix[pos_y, pos_x] = min(pos_x + 1, pos_y + 1, size_x-pos_x, size_y - pos_y)

    def set_stick_particles(self, particles):
        for particle in particles:
            self.set_stick_particle(particle)

    def set_stick_particle(self, particle):
        pos_x, pos_y = particle
        self.distance_matrix[pos_y, pos_x] = -1  # no ther particle allowed on this position
        self.update_with_stick_poition(pos_x + 1, pos_y)
        self.update_with_stick_poition(pos_x - 1, pos_y)
        self.update_with_stick_poition(pos_x, pos_y + 1)
        self.update_with_stick_poition(pos_x, pos_y - 1)

    def update_with_stick_poition(self, stick_x, stick_y):  # todo: this takes >2/3 of computation tim (200x200) -> check, wich part to update; consider numpy arry operation to change qhole row/col)
        size_x, size_y = self.area_size
        for pos_x in range(size_x):
            for pos_y in range(size_y):
                distance_to_stick = abs(pos_x-stick_x) + abs(pos_y-stick_y)
                self.distance_matrix[pos_y, pos_x] = min(self.distance_matrix[pos_y, pos_x], distance_to_stick)

    def get_new_particle(self) -> list:
        random = np.random.randint(4)
        if random == 0:
            pos_x = 0
            pos_y = np.random.randint(self.area_size[1])
        elif random == 1:
            pos_x = self.area_size[0] - 1
            pos_y = np.random.randint(self.area_size[1])
        elif random == 2:
            pos_x = np.random.randint(self.area_size[0])
            pos_y = 0
        elif random == 3:
            pos_x = np.random.randint(self.area_size[0])
            pos_y = self.area_size[1] - 1
        else:
            raise Exception("Something went wrong in get_new_particle()")
        return [pos_x, pos_y]

    def get_random_step(self, distance):
        pos_x, pos_y = (0, 0)
        step_list = self.list_of_position_probability_lists[min(distance, self.max_steps)]
        random = np.random.random()
        for key, value in step_list.items():
            if value >= random:
                pos_x = key[0]
                pos_y = key[1]
                old_value = value
                assert old_value <= value
                break
        return pos_x, pos_y

    def plot(self):
        canvas = np.zeros(self.area_size)
        for x in range(self.area_size[0]):
            for y in range(self.area_size[1]):
                if self.distance_matrix[y, x] == -1:
                    canvas[y, x] = 1

        plt.matshow(canvas)
        plt.show()
        plt.savefig("rand_walk_500particles.png", dpi=150)


def calc_symmetric_positions(position_list: dict) -> dict:
    result = {}
    for key, value in position_list.items():
        pos_x = key[0]
        pos_y = key[1]

        result[-pos_x, pos_y] = position_list[(pos_x, pos_y)]
        result[-pos_x, -pos_y] = position_list[(pos_x, pos_y)]
        result[pos_x, -pos_y] = position_list[(pos_x, pos_y)]

        result[pos_y, pos_x] = position_list[(pos_x, pos_y)]
        result[-pos_y, pos_x] = position_list[(pos_x, pos_y)]
        result[-pos_y, -pos_x] = position_list[(pos_x, pos_y)]
        result[pos_y, -pos_x] = position_list[(pos_x, pos_y)]

    return result


# no need for complete matrix, only list with actualy reachable positions; 1.055 times faster (compared to matrix)
def calc_position_probability_list_symmetric(number_of_steps) -> dict:
    result = {}
    # position_list = defaultdict(lambda:0.0) # multiprocessing needs to pickle -> can't have a lambda
    position_list = defaultdict(float)
    if number_of_steps == 0:
        result[(0, 0)] = 1
        return position_list

    p_list = [0.25, 0.25, 0.25, 0.25]  # all directions have same probability
    rv = multinomial(number_of_steps, p_list)

    # this loop finds all reachable positions
    for n_right in range(number_of_steps + 1):
        for n_left in range(number_of_steps - n_right + 1):
            pos_x = n_right - n_left
            if pos_x > 0:  # due to symmetry
                continue
            for n_down in range(number_of_steps - n_left - n_right + 1):
                n_up = number_of_steps - n_left - n_right - n_down
                pos_y = n_up - n_down
                # if pos_y > 0:  # unnecessary; pos_x is already <=0
                #     continue
                if pos_y > pos_x:  # due to symmetry
                    continue

                # this takes up >95% of computation time in calc_position_probability_list_symmetric!
                # thus optimizing loop with impact on readability not helpful
                # todo: check with pypy
                position_list[pos_y, pos_x] += rv.pmf([n_left, n_right, n_down, n_up])

    position_list.update(calc_symmetric_positions(position_list))

    # create cummulative distribution values:
    sum=0
    for key, value in position_list.items():
        sum += value
        result[key] = sum
    assert np.isclose(sum, 1.0)
    return result
    # return position_list


def generate_list_of_position_probability_lists_single_process(max_number_of_steps):
    result = []
    for i in range(max_number_of_steps+1):
        result.append(calc_position_probability_list_symmetric(i))
    return result


def generate_list_of_position_probability_lists(max_number_of_steps, multiprocessing=True):
    if not multiprocessing:
        return generate_list_of_position_probability_lists_single_process(max_number_of_steps)

    with Pool() as pool:  # processes=None (or no argument given) ->  number returned by os.cpu_count() is used.
        result = pool.map(calc_position_probability_list_symmetric, range(max_number_of_steps+1))
    return result


if __name__ == '__main__':
    freeze_support()  # needed for windows
    main()
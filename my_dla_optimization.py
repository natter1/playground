"""
My speed optimization of diffusion controlled aglomeration
inspired by a question on code-review:
https://codereview.stackexchange.com/questions/235883/how-to-increase-the-efficiency-of-dla-algorithm

@author: Nathanael Jöhrmnann
"""
from collections import defaultdict
from multiprocessing.pool import Pool
from multiprocessing.spawn import freeze_support

import numpy as np
from scipy.stats import multinomial


def main():
    max_steps = 100
    generate_list_of_position_probability_lists(max_steps)
    generate_list_of_position_probability_lists_multiprocessing(max_steps)



# we do not need complete matrix, only list with possible positions; also 1.055 times faster
def calc_position_probability_list_symmetric(number_of_steps) -> dict:
    result = defaultdict(lambda:0.0)  # np.zeros((size_y, size_x))  # size: (2n+1) * (2n+1)
    if number_of_steps == 0:
        result[(0, 0)] = 1
        return result

    p_list = [0.25, 0.25, 0.25, 0.25]  # all directions have same probability
    rv = multinomial(number_of_steps, p_list)

    for n_left in range(number_of_steps + 1):
        for n_right in range(number_of_steps - n_left + 1):
            for n_down in range(number_of_steps - n_left - n_right + 1):
                n_up = number_of_steps - n_left - n_right - n_down
                pos_x = n_right - n_left
                pos_y = n_up - n_down
                if pos_x > 0:
                    continue
                if pos_y > 0:
                    continue
                if pos_y > pos_x:
                    continue

                result[pos_y, pos_x] += rv.pmf([n_left, n_right, n_down, n_up])

    # calc symmetric positions
    symmetric_positions = {}
    for key, value in result.items():
        pos_x = key[0]
        pos_y = key[1]

        symmetric_positions[-pos_x, pos_y] = result[(pos_x, pos_y)]
        symmetric_positions[-pos_x, -pos_y] = result[(pos_x, pos_y)]
        symmetric_positions[pos_x, -pos_y] = result[(pos_x, pos_y)]

        symmetric_positions[pos_y, pos_x] = result[(pos_x, pos_y)]
        symmetric_positions[-pos_y, pos_x] = result[(pos_x, pos_y)]
        symmetric_positions[-pos_y, -pos_x] = result[(pos_x, pos_y)]
        symmetric_positions[pos_y, -pos_x] = result[(pos_x, pos_y)]

    result.update(symmetric_positions)


    # assert np.isclose(result.sum(), 1.0)
    return result


def generate_list_of_position_probability_lists(max_number_of_steps):
    result = []
    for i in range(max_number_of_steps+1):
        result.append(calc_position_probability_list_symmetric(i))
        # print(f"i (without multiprocessing): {i}")
    return result


def generate_list_of_position_probability_lists_multiprocessing(max_number_of_steps):
    with Pool() as pool:  # processes=None (or no argument given) ->  number returned by os.cpu_count() is used.
        result = pool.map(calc_position_probability_list_symmetric, range(max_number_of_steps+1))
    return result


# with Pool(processes=None) as pool:  # None ->  If processes is None then the number returned by os.cpu_count() is used.
if __name__ == '__main__':
    freeze_support()  # needed for windows
    main()
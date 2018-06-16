import numpy as np
import time
import sys


def print_binary_func(binary_image, symbol_list):
    h, w = binary_image.shape
    for i in range(h):
        # print(' ' * 50, end='')
        time.sleep(0.1)
        for j in range(w):
            if binary_image[i, j] == 0:
                print('  ', end='', file=sys.stdout, flush=True)
            else:
                print(np.random.choice(symbol_list), end='', file=sys.stdout, flush=True)
        print()

def print_gray_func(binary_image, symbol_list):

    h, w = binary_image.shape
    for i in range(h):
        # print(' ' * 50, end='')
        time.sleep(0.1)
        for j in range(w):
            if binary_image[i, j] == 0:
                print('  ', end='', file=sys.stdout, flush=True)
            else:
                print(np.random.choice(symbol_list), end='', file=sys.stdout, flush=True)
        print()



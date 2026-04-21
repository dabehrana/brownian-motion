import math

from matplotlib import pyplot as plt
from matplotlib.colors import Colormap
import pandas as pd


def get_float_from_user(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("\n\033[1;93m" +
                  "Invalid value. Please try again..." +
                  "\033[0m")


def get_int_from_user(prompt):
    while True:
        try:
            value = int(get_float_from_user(prompt))
            return value
        except ValueError:
            print("\n\033[1;93m" +
                  "Invalid value. Please try again..." +
                  "\033[0m")


def find_coprime(n):
    # Given n, find a number that is coprime from a set of trial values

    # test from a subset of prime numbers which should produce seemingly random results
    trial_values = [13, 17, 19, 23, 37, 43, 47, 53, n-1]

    for a in trial_values:
        if math.gcd(a, n):
            return a


def conduct_bijection(i, n, a):
    # Given gcd(a,n) = 1, exists a bijection from {1,...,n} to itself

    return (a * i) % n

def conduct_plots(n, cmap : Colormap, motions: list[pd.Series]):
        # Will use this value to "randomise" the order of colours on the graph
        a = find_coprime(n)
        for i in range(n):
            # "randomise" the order of colours on the graph
            j = conduct_bijection(
                i, n, a)
            motions[i].plot(color=cmap(j))
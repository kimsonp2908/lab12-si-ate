

from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]

def sample_tree() -> GameTree:
    return [[3, 5], [2, 9]]

def medium_tree() -> GameTree:
    return [[[3, 5], [6, 9]], [[1, 2], [0, -1]], [[7, 4], [8, 6]]]

def ordered_tree_for_pruning() -> GameTree:
    return [[[10, 9], [8, 7]], [[6, 5], [4, 3]], [[2, 1], [0, -1]]]

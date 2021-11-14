import functools
from typing import List, Callable


class Node:

    def __init__(self,
                 inputs: List[str],
                 function: Callable,
                 name: str = None,
                 output: str = None):
        self.function = function
        self.inputs = inputs
        self.name = name if name is not None else self.get_func_name(function)
        self.output = output if output is not None else self.name

    def __repr__(self):
        return self.name

    @staticmethod
    def get_func_name(f):
        if isinstance(f, (functools.partial, functools.partialmethod)):
            fname = f.func.__name__
        else:
            fname = f.__name__
        return fname

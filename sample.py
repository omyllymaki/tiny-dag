import logging

from graph import Graph
from node import Node

logging.basicConfig(level=logging.DEBUG)


def print_input(func):
    def inner(*args, **kwargs):
        print(f"Input for function {func}: {args}, {kwargs}")
        out = func(*args, **kwargs)
        return out

    return inner


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def main():
    nodes = [
        Node(["add1", "x"], add, "add2"),
        Node(["add1", "add2"], mul, "mul"),
        Node(["x", "y"], add, "add1"),
        Node(["mul", "z"], div, "div"),
    ]

    graph = Graph(nodes, wrappers=[print_input])
    print("Graph: ", graph)
    graph.render()

    data = {"x": 5, "y": 3, "z": 3}
    graph.check(data)
    results = graph.calculate(data)
    print(f"Result: {results}")


if __name__ == "__main__":
    main()

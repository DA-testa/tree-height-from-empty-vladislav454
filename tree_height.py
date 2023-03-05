#Vladislavs Sereda 221RDB440 12 gr.

import sys
import threading
import numpy

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def compute_height(node):
    if not node.children:
        return 1
    heights = [compute_height(child) for child in node.children]
    return max(heights) + 1


def main():
    input_type = input("")
    n = 0
    parents = []
    if "I" in input_type:
        n = input("")
        n = int(n.replace("\\r\\n",""))
        print(n)
        parents = list(map(int, input("").split()))
    else:
        file_path = input("")
        while "a" in file_path:
            file_path = input("")
        with open(f"main/tree-height-from-empty-vladislav454/test/{file_path}.txt", "r") as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))

    nodes = [Node(i) for i in range(n)]
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    if root:
        height = compute_height(root)
        print(height)
    else:
        print("Error: No root node found in the input.")

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

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
    if "I" in input_type:
        print(2)
        n = input("")
        n = int(n.join(i for i in n if i.isdigit()))
        parents = list(map(int, input("").split()))
    else:
        file_path = input("")
        while "a" in filename:
            filename = input("")
            with open(f"folder/{filename}.txt", "r") as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))

    nodes = [Node(i) for i in range(n)]
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    height = compute_height(root)
    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

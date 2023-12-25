from aoc import read_input

lines = read_input(split_lines=False)
nums = [int(n) for n in lines.split()]


class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def total_metadata(self):
        total = 0
        stack = [self]
        while stack:
            node = stack.pop()
            total += sum(node.metadata)
            stack += node.children
        return total

    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)

        total = 0
        for i in self.metadata:
            if (i - 1) < len(self.children):
                total += self.children[i - 1].value()
        return total


def parse_node(index):
    num_children = nums[index]
    num_metadata = nums[index + 1]

    children = []
    curr = index + 2
    for _ in range(num_children):
        node, curr = parse_node(curr)
        children.append(node)

    metadata = nums[curr : curr + num_metadata]

    return Node(children, metadata), curr + num_metadata


root, _ = parse_node(0)

print(root.total_metadata())
print(root.value())

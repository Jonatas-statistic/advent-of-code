import re

from network import Node


re_letters = re.compile(r'[A-Z0-9]+')

def get_nodes(text_nodes: str, rule: str = 'AAA', instructions:str = None, depth:int = 1) -> Node|list[Node]:
    rule_len = len(rule)
    rule_nodes = []
    for line in text_nodes.splitlines():
        name, left, right = re_letters.findall(line)
        node = Node(name)
        node.left = Node(left)
        node.right = Node(right)

        if name[-rule_len:] == rule:
            rule_nodes.append(node)

    # cycle and z_points
    for node in Node._nodes.values():
        node.cycle = node
        node.z_points = set()
        z_point = 1
        if instructions:
            node.depth = depth
            for _ in range(depth):
                for direction in instructions:
                    node.cycle = next_(direction, nodes=[node.cycle])[0]
                    if node.cycle.name[-1] == 'Z':
                        node.z_points.add(z_point)
                    z_point += 1

    return rule_nodes


def read_maps(directory: str, rule: str = 'AAA', depth:int = 1):
    with open(directory) as f:
        maps = f.read()
    instructions, text_nodes = maps.split('\n\n')
    
    instructions = instructions.strip()
    nodes = get_nodes(text_nodes, rule=rule, instructions=instructions, depth=depth)

    return instructions, nodes


# Part Two
def next_(direction: str, nodes: list[Node]):
    if direction == 'L':
        for index in range(len(nodes)):
            nodes[index] = nodes[index].left
    elif direction == 'R':
        for index in range(len(nodes)):
            nodes[index] = nodes[index].right
    return nodes


def next_cycle(nodes: list[Node]):
    for  index in range(len(nodes)):
        nodes[index] = nodes[index].cycle
    return nodes


def is_all_rule(nodes: list[Node], rule: str = 'ZZZ'):
    rule_len = len(rule)
    for node in nodes:
        if node.name[-rule_len:] != rule:
            return False
    return True


def reach_rule(instructions: str, nodes: list[Node], rule: str = 'ZZZ'):
    steps = 1
    while True:
        for direction in instructions:
            next_(direction, nodes)
            if is_all_rule(nodes, rule=rule):
                return steps
            steps += 1


def reach_rule_two(instructions: str, nodes: list[Node], rule: str = 'Z'):
    len_instr = len(instructions)
    steps = 0
    meta = 1_000_000
    while True:
        if all(map(lambda node: node.z_points, nodes)):
            z_points: set = nodes[0].z_points
            for index in range(1, len(nodes)):
                z_points = z_points.intersection(nodes[index].z_points)
            if z_points:
                return steps + min(z_points)
        nodes = next_cycle(nodes)
        steps += len_instr * nodes[0].depth

        if steps > meta:
            print(steps)
            meta *= 2
                  

if __name__ == '__main__':
    instructions, nodes = read_maps('maps.txt')

    # Part One
    steps = reach_rule(instructions, nodes)
    print(f'Part One: {steps}')

    # Part Two
    instructions, nodes = read_maps('maps.txt', rule = 'A', depth=2**10)
    steps = reach_rule_two(instructions, nodes, rule='Z')
    print(f'Part Two: {steps}')
    
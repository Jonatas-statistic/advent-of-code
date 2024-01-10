import os
import pytest

from network import Node
from main import read_maps, reach_rule, reach_rule_two


@pytest.fixture
def maps():
    return read_maps(os.path.join('test', 'test_maps.txt'))


def test_instructions(maps):
    instructions, _ = maps

    assert instructions == 'LLR'


def test_nodes(maps):
    _, nodes = maps

    aaa = Node(name='AAA')
    bbb = Node(name='BBB')
    zzz = Node(name='ZZZ')

    aaa.left, aaa.right = bbb, bbb
    bbb.left, bbb.right = aaa, zzz
    zzz.left, zzz.right = zzz, zzz

    assert nodes == [aaa]


def test_reach_rule(maps):
    instructions, nodes = maps
    steps = reach_rule(instructions, nodes)

    assert steps == 6


# Part Two
@pytest.fixture
def maps_two():
    return read_maps(os.path.join('test', 'test_maps_two.txt'), rule = 'A')


def test_nodes_two(maps_two):
    _, nodes = maps_two

    # 11A
    a1 = Node('11A')
    a1.left = Node('11B')
    a1.right = Node('XXX')
    # 22A
    a2 = Node('22A')
    a2.left = Node('22B')
    a2.right = Node('XXX')

    assert nodes == [a1, a2]


def test_reach_rule_two(maps_two):
    instructions, nodes = maps_two
    steps = reach_rule_two(instructions, nodes, rule = 'Z')

    assert steps == 6
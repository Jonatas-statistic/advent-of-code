class Node:
    _nodes: dict = dict()

    def __new__(cls, name: str):
        node = cls._nodes.get(name)
        if node is None:
            node = super().__new__(cls)
            node.left = None
            node.right = None
            node.cycle = None # after a cycle of instructions
            node.z_point = None # Z Node in cycle of instructions
            cls._nodes[name] = node
        return cls._nodes[name]

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Node):
            if self.name == other.name:
                return True
        return False
    
    def __repr__(self) -> str:
        return f'Node("{self.name}")'
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __hash__(self) -> int:
        return hash(self.name)


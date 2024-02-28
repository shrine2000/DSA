class MapSum:
    def __init__(self):
        self.children = {}

    def insert(self, key: str, val: int) -> None:
        self.children[key] = val

    def sum(self, prefix: str) -> int:
        count = 0
        for k, v in self.children.items():
            if k.startswith(prefix):
                count += v
        return count
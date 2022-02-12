from typing import Dict


class SearchQuestion:
    def __init__(self):
        self.route = {
            "S": {"a": 4, "b": 5},
            "a": {"S": 4, "c": 5, "d": 4},
            "b": {"S": 5, "c": 6, "e": 7},
            "c": {"a": 5, "b": 6, "G": 5},
            "d": {"a": 4, "G": 8},
            "e": {"b": 7, "G": 7},
            "G": {"c": 5, "d": 8, "e": 7}
        }
        self.approximate_value_of_shortest_path = {
            "S": 11,
            "a": 8,
            "b": 6,
            "c": 3.5,
            "d": 7,
            "e": 1,
            "G": 0,
        }
        self.path_cost = 0
        self.passed_path = []

    @staticmethod
    def start_node() -> str:
        return "S"

    @staticmethod
    def end_node() -> str:
        return "G"

    def is_end_node(self, node: str) -> bool:
        return node == self.end_node()

    def next_nodes(self, point: str) -> Dict[str, int]:
        return self.route[point]

    def h(self, node: str) -> int:
        try:
            return self.approximate_value_of_shortest_path[node]
        except Exception:
            raise KeyError("unknown key error")

    def greed_search(self):
        current_node = self.start_node()
        while not self.is_end_node(current_node):
            if current_node in self.passed_path:
                raise Exception("Loop path error")
            self.passed_path.append(current_node)
            next_nodes = {node: self.h(node) for node in self.next_nodes(current_node)}
            previous_node = current_node
            current_node = min(next_nodes, key=next_nodes.get)  # h(n)が最小のノードに移動
            self.path_cost += self.next_nodes(previous_node)[current_node]
        self.passed_path.append(self.end_node())

    def print_result(self):
        print("path: ", self.passed_path)
        print("cost: ", self.path_cost)


if __name__ == '__main__':
    question = SearchQuestion()
    question.greed_search()
    question.print_result()

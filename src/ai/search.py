from typing import Dict


class SearchQuestion:
    def __init__(self):
        self.__route = {
            "S": {"a": 4, "b": 5},
            "a": {"S": 4, "c": 5, "d": 4},
            "b": {"S": 5, "c": 6, "e": 7},
            "c": {"a": 5, "b": 6, "G": 5},
            "d": {"a": 4, "G": 8},
            "e": {"b": 7, "G": 7},
            "G": {"c": 5, "d": 8, "e": 7}
        }
        self.__approximate_value_of_shortest_path = {
            "S": 11,
            "a": 8,
            "b": 6,
            "c": 3.5,
            "d": 7,
            "e": 1,
            "G": 0,
        }
        self.__path_cost = 0
        self.__passed_path = []

    @staticmethod
    def start_node() -> str:
        return "S"

    @staticmethod
    def end_node() -> str:
        return "G"

    def is_end_node(self, node: str) -> bool:
        return node == self.end_node()

    def next_nodes(self, point: str) -> Dict[str, int]:
        return self.__route[point]

    def h(self, node: str) -> int:
        """ ゴールへの近さ """
        try:
            return self.__approximate_value_of_shortest_path[node]
        except Exception:
            raise KeyError("unknown key error")

    def g(self, node: str = None):
        """ 出発点からnodeまでの経路長 """
        path_length = 0
        for i in range(len(self.__passed_path) - 1):
            path_length += self.__route[self.__passed_path[i]][self.__passed_path[i+1]]
        if node is not None:
            return path_length + self.__route[self.__passed_path[-1]][node]
        return path_length

    def greed_search(self):
        current_node = self.start_node()
        while not self.is_end_node(current_node):
            if current_node in self.__passed_path:
                raise Exception("Loop path error")
            self.__passed_path.append(current_node)
            next_nodes = {node: self.h(node) for node in self.next_nodes(current_node)}
            current_node = min(next_nodes, key=next_nodes.get)  # h(n)が最小のノードに移動
        self.__passed_path.append(self.end_node())
        self.__path_cost = self.g()

    def a_star_algorithm_search(self):
        current_node = self.start_node()
        while not self.is_end_node(current_node):
            if current_node in self.__passed_path:
                raise Exception("Loop path error")
            self.__passed_path.append(current_node)
            next_nodes = {node: self.h(node) + self.g(node) for node in self.next_nodes(current_node)}
            print(current_node, next_nodes)
            current_node = min(next_nodes, key=next_nodes.get)  # h(n)が最小のノードに移動
        self.__passed_path.append(self.end_node())
        self.__path_cost = self.g()

    def print_result(self):
        print("path: ", self.__passed_path)
        print("cost: ", self.__path_cost)

    def reset_result(self):
        self.__passed_path = []
        self.__path_cost = 0


if __name__ == '__main__':
    q = SearchQuestion()

    q.greed_search()
    q.print_result()

    q.reset_result()

    q.a_star_algorithm_search()
    q.print_result()

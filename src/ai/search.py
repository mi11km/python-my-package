from typing import Dict, List


class SearchQuestion:

    def __init__(self):
        self.__route = {
            "S": {
                "a": 4,
                "b": 5
            },
            "a": {
                "S": 4,
                "c": 5,
                "d": 4
            },
            "b": {
                "S": 5,
                "c": 6,
                "e": 7
            },
            "c": {
                "a": 5,
                "b": 6,
                "G": 5
            },
            "d": {
                "a": 4,
                "G": 8
            },
            "e": {
                "b": 7,
                "G": 7
            },
            "G": {
                "c": 5,
                "d": 8,
                "e": 7
            },
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
        self.__passed_paths_of_frontier: Dict[str, List[str]] = {
            "a": ["S", "a"],
            "b": ["S", "b"],
        }

    @staticmethod
    def start_node() -> str:
        return "S"

    @staticmethod
    def end_node() -> str:
        return "G"

    def next_nodes(self, node: str) -> Dict[str, int]:
        return self.__route[node]

    def h(self, node: str) -> float:
        """nodeからゴールまでの最短経路の近似値"""
        try:
            return self.__approximate_value_of_shortest_path[node]
        except Exception:
            raise KeyError("unknown node")

    def g(self, node: str = None) -> int:
        """出発点からnodeまでの(判明した)経路長"""
        try:
            passed_path = self.__passed_paths_of_frontier[node]
        except KeyError:
            raise KeyError("invalid node, not in frontiers.")
        path_length = 0
        for i in range(len(passed_path) - 1):
            path_length += self.__route[passed_path[i]][passed_path[i + 1]]
        return path_length

    def result_path(self):
        return self.__passed_paths_of_frontier[self.end_node()]

    def print_result(self):
        print("path: ", self.__passed_paths_of_frontier[self.end_node()])
        print("cost: ", self.g(self.end_node()))

    def reset_result(self):
        self.__passed_paths_of_frontier: Dict[str, List[str]] = {
            "a": ["S", "a"],
            "b": ["S", "b"],
        }

    def greed_search(self):
        frontiers: Dict[str, int] = {
            frontier: self.h(frontier)
            for frontier in self.next_nodes(self.start_node())
        }
        while not self.end_node() in frontiers:
            selected_node = min(frontiers, key=frontiers.get)
            self.__passed_paths_of_frontier.update({
                node:
                self.__passed_paths_of_frontier[selected_node].copy() + [node]
                for node in self.__route[selected_node]
                if not (node in self.__passed_paths_of_frontier[selected_node])
            })
            frontiers.update({
                node: self.h(node)
                for node in self.next_nodes(selected_node)
                if not (node in self.__passed_paths_of_frontier[selected_node])
            })
            del frontiers[selected_node]
            del self.__passed_paths_of_frontier[selected_node]

    def a_star_algorithm_search(self):
        frontiers: Dict[str, int] = {
            frontier: self.h(frontier) + self.g(frontier)
            for frontier in self.next_nodes(self.start_node())
        }
        while not self.end_node() in frontiers:
            selected_node = min(frontiers, key=frontiers.get)
            self.__passed_paths_of_frontier.update({
                node:
                self.__passed_paths_of_frontier[selected_node].copy() + [node]
                for node in self.__route[selected_node]
                if not (node in self.__passed_paths_of_frontier[selected_node])
            })
            frontiers.update({
                node: self.h(node) + self.g(node)
                for node in self.next_nodes(selected_node)
                if not (node in self.__passed_paths_of_frontier[selected_node])
            })
            del frontiers[selected_node]
            del self.__passed_paths_of_frontier[selected_node]

    def update_approximate_value_of_shortest_path(self, value: float):
        """h(a)の値を更新する関数"""
        self.__approximate_value_of_shortest_path["a"] = value


if __name__ == "__main__":
    q = SearchQuestion()

    q.greed_search()
    q.print_result()  # (1)の答え

    q.reset_result()

    q.a_star_algorithm_search()
    q.print_result()  # (2)の答え

    collect_path = q.result_path().copy()
    found_path = q.result_path().copy()
    threshold = 8
    while collect_path == found_path:
        threshold += 0.00001
        q.update_approximate_value_of_shortest_path(threshold)
        q.reset_result()
        q.a_star_algorithm_search()
        found_path = q.result_path().copy()
    print(threshold)  # (3)の答え

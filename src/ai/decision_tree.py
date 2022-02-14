import math
from typing import List


class HumanData:
    def __init__(self, id: int, salary: str, gender: str, like_trip: str, buy_wine: str):
        self.id: int = id
        self.is_high_salary: bool = salary == "高"
        self.is_male: bool = gender == "男"
        self.is_like_trip: bool = like_trip == "好き"
        self.is_buy_wine: bool = buy_wine == "YES"


class Node(object):
    def __init__(self, attribute):
        self.__attribute = attribute
        self.__children: List[Node] = []


class DecisionTreeQuestion(object):
    def __init__(self):
        self.dataset = [
            HumanData(1, "低", "男", "嫌い", "NO"),
            HumanData(2, "高", "女", "好き", "YES"),
            HumanData(3, "高", "女", "嫌い", "NO"),
            HumanData(4, "低", "男", "好き", "YES"),
            HumanData(5, "高", "女", "好き", "YES"),
            HumanData(6, "低", "女", "嫌い", "NO"),
            HumanData(7, "高", "男", "好き", "YES"),
            HumanData(8, "高", "男", "好き", "YES"),
            HumanData(9, "低", "男", "好き", "YES"),
            HumanData(10, "高", "男", "嫌い", "YES"),
            HumanData(11, "低", "女", "嫌い", "NO"),
            HumanData(12, "低", "男", "好き", "YES"),
            HumanData(13, "低", "女", "好き", "NO"),
            HumanData(14, "高", "女", "嫌い", "NO"),
        ]
        self.current_classification = self.classify_buy_wine(self.dataset)
        self.current_information_entropy = self.calculate_information_entropy(self.current_classification)

    @staticmethod
    def calculate_information_entropy(classification_numbers: List[int]) -> float:
        """ 情報エントロピーを計算する関数 """
        total = sum(classification_numbers)
        return -sum(
            [classification / total * math.log2(classification / total) for classification in classification_numbers])

    @staticmethod
    def classify_buy_wine(dataset: List[HumanData]) -> List[int]:
        buy_wine = len([data for data in dataset if data.is_buy_wine])
        return [buy_wine, len(dataset) - buy_wine]

    def calculate_decreasing_information_entropy(self, is_ok: List[int], is_no: List[int]):
        information_entropy = \
            sum(is_ok) / sum(q.current_classification) * q.calculate_information_entropy(is_ok) \
            + sum(is_no) / sum(q.current_classification) * q.calculate_information_entropy(is_no)
        return self.current_information_entropy - information_entropy


if __name__ == '__main__':
    q = DecisionTreeQuestion()

    is_ok = q.classify_buy_wine([data for data in q.dataset if data.is_high_salary])
    is_no = q.classify_buy_wine([data for data in q.dataset if not data.is_high_salary])
    print("情報エントロピーの減少量：", q.calculate_decreasing_information_entropy(is_ok, is_no))

    is_ok = q.classify_buy_wine([data for data in q.dataset if data.is_male])
    is_no = q.classify_buy_wine([data for data in q.dataset if not data.is_male])
    print("情報エントロピーの減少量：", q.calculate_decreasing_information_entropy(is_ok, is_no))

    is_ok = q.classify_buy_wine([data for data in q.dataset if data.is_like_trip])
    is_no = q.classify_buy_wine([data for data in q.dataset if not data.is_like_trip])
    print("情報エントロピーの減少量：", q.calculate_decreasing_information_entropy(is_ok, is_no))

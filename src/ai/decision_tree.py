import math
from typing import List


class HumanData:
    def __init__(self, id: int, salary: str, gender: str, like_trip: str, buy_wine: str):
        self.id: int = id
        self.is_high_salary: bool = salary == "高"
        self.is_male: bool = gender == "男"
        self.is_like_trip: bool = like_trip == "好き"
        self.is_buy_wine: bool = buy_wine == "YES"


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
    def split_dataset(dataset: List[HumanData], attribute: str):
        split_dataset = []
        if attribute == "年収":
            split_dataset.append([data for data in dataset if data.is_high_salary])
            split_dataset.append([data for data in dataset if not data.is_high_salary])
        if attribute == "性別":
            split_dataset.append([data for data in dataset if data.is_male])
            split_dataset.append([data for data in dataset if not data.is_male])
        if attribute == "旅行":
            split_dataset.append([data for data in dataset if data.is_like_trip])
            split_dataset.append([data for data in dataset if not data.is_like_trip])
        return split_dataset

    @staticmethod
    def calculate_information_entropy(classification_numbers: List[int]) -> float:
        """ 情報エントロピーを計算する関数 """
        total = sum(classification_numbers)
        return -sum(
            [classification / total * math.log2(classification / total) for classification in classification_numbers if
             classification != 0])

    @staticmethod
    def classify_buy_wine(dataset: List[HumanData]) -> List[int]:
        buy_wine = len([data for data in dataset if data.is_buy_wine])
        return [buy_wine, len(dataset) - buy_wine]

    def calculate_decreasing_information_entropy(self, is_ok: List[int], is_no: List[int]):
        information_entropy = \
            sum(is_ok) / sum(q.current_classification) * q.calculate_information_entropy(is_ok) \
            + sum(is_no) / sum(q.current_classification) * q.calculate_information_entropy(is_no)
        return self.current_information_entropy - information_entropy

    def select_attribute(self, dataset: List[HumanData], except_attributes: List[str]):
        decreasing_information_entropy = {}

        if not ("年収" in except_attributes):
            is_ok_dataset = q.classify_buy_wine([data for data in dataset if data.is_high_salary])
            is_no_dataset = self.classify_buy_wine([data for data in dataset if not data.is_high_salary])
            decreasing_information_entropy["年収"] = self.calculate_decreasing_information_entropy(is_ok_dataset,
                                                                                                 is_no_dataset)

        if not ("性別" in except_attributes):
            is_ok_dataset = self.classify_buy_wine([data for data in dataset if data.is_male])
            is_no_dataset = self.classify_buy_wine([data for data in dataset if not data.is_male])
            decreasing_information_entropy["性別"] = self.calculate_decreasing_information_entropy(is_ok_dataset,
                                                                                                 is_no_dataset)

        if not ("旅行" in except_attributes):
            is_ok_dataset = self.classify_buy_wine([data for data in dataset if data.is_like_trip])
            is_no_dataset = self.classify_buy_wine([data for data in dataset if not data.is_like_trip])
            decreasing_information_entropy["旅行"] = self.calculate_decreasing_information_entropy(is_ok_dataset,
                                                                                                 is_no_dataset)

        biggest_attribute = max(decreasing_information_entropy, key=decreasing_information_entropy.get)
        return biggest_attribute, decreasing_information_entropy[biggest_attribute]


if __name__ == '__main__':
    q = DecisionTreeQuestion()

    selected_attribute = q.select_attribute(q.dataset, [])
    print(selected_attribute)  # (1)の答え

    # (2)を求めるのに参考にしたプログラム
    datasets = q.split_dataset(q.dataset, selected_attribute[0])
    print([[data.id for data in dataset] for dataset in datasets])
    next_datasets = []
    for dataset in datasets:
        attribute = q.select_attribute(dataset, [selected_attribute[0]])
        next_dataset = q.split_dataset(dataset, attribute[0])
        next_datasets += next_dataset
        print(attribute)
        print([[data.id for data in dataset] for dataset in next_dataset])
    print([[data.id for data in dataset] for dataset in next_datasets])

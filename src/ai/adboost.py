import math


class HumanData:
    def __init__(
        self, id: int, age: str, salary: str, gender: str, like_trip: str, buy_wine: str
    ):
        self.id: int = id
        self.age: bool = age == "高"
        self.is_high_salary: bool = salary == "高"
        self.is_male: bool = gender == "男"
        self.is_like_trip: bool = like_trip == "好き"
        self.is_buy_wine: bool = buy_wine == "YES"


dataset = [
    HumanData(1, "高", "高", "女", "嫌い", "NO"),
    HumanData(2, "低", "低", "男", "好き", "NO"),
    HumanData(3, "高", "高", "女", "嫌い", "YES"),
    HumanData(4, "高", "高", "男", "好き", "YES"),
    HumanData(5, "低", "低", "女", "好き", "YES"),
    HumanData(6, "高", "低", "男", "好き", "NO"),
    HumanData(7, "低", "高", "女", "嫌い", "YES"),
    HumanData(8, "低", "低", "女", "嫌い", "NO"),
    HumanData(9, "高", "高", "男", "好き", "YES"),
    HumanData(10, "高", "低", "女", "好き", "YES"),
]

print(
    "A: ",
    len(
        [
            data
            for data in dataset
            if (data.age and data.is_buy_wine)
            or (not data.age and not data.is_buy_wine)
        ]
    )
    / 10,
)
print(
    "B: ",
    len(
        [
            data
            for data in dataset
            if (not data.age and data.is_buy_wine)
            or (data.age and not data.is_buy_wine)
        ]
    )
    / 10,
)
print(
    "C: ",
    len(
        [
            data
            for data in dataset
            if (data.is_high_salary and data.is_buy_wine)
            or (not data.is_high_salary and not data.is_buy_wine)
        ]
    )
    / 10,
)
print(
    "D: ",
    len(
        [
            data
            for data in dataset
            if (not data.is_high_salary and data.is_buy_wine)
            or (data.is_high_salary and not data.is_buy_wine)
        ]
    )
    / 10,
)
print(
    "E: ",
    len(
        [
            data
            for data in dataset
            if (data.is_like_trip and data.is_buy_wine)
            or (not data.is_like_trip and not data.is_buy_wine)
        ]
    )
    / 10,
)
print(
    "F: ",
    len(
        [
            data
            for data in dataset
            if (not data.is_like_trip and data.is_buy_wine)
            or (data.is_like_trip and not data.is_buy_wine)
        ]
    )
    / 10,
)
print(
    "G: ",
    len(
        [
            data
            for data in dataset
            if (data.is_male and data.is_buy_wine)
            or (not data.is_male and not data.is_buy_wine)
        ]
    )
    / 10,
)
print(
    "H: ",
    len(
        [
            data
            for data in dataset
            if (not data.is_male and data.is_buy_wine)
            or (data.is_male and not data.is_buy_wine)
        ]
    )
    / 10,
)

print(math.sqrt(0.7 / 0.3))

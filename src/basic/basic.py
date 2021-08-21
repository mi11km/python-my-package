from collections import namedtuple
from dataclasses import dataclass
from typing import Any, Generator


def is_prime(n: int) -> bool:
    """ n が素数かどうか判定する関数 """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for odd_number in range(3, n, 2):
        if n % odd_number == 0:
            return False
    return True


def load_numbers_sorted(txt: str) -> list[int]:
    with open(txt) as f:
        numbers = sorted(map(lambda e: int(e), f))
    return numbers


def print_hello():
    print('Hello, world!')


def is_tweeted(string: str) -> str:
    """ セイウチ演算子の例 """
    limit = 280
    if (diff := limit - len(string)) >= 0:
        return "A fitting tweet"
    else:
        return f"Went over by {abs(diff)}"


def document_it(func: callable) -> callable:
    """"デコレータの例"""

    def new_func(*args, **kwargs):
        print("Running function: ", func.__name__)
        print("Positional arguments: ", args)
        print("Keyword arguments: ", kwargs)
        result = func(*args, **kwargs)
        print("Result: ", result)
        return result

    return new_func


def square_it(func: callable) -> callable:
    """"デコレータの例2"""

    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2

    return new_func


@document_it
@square_it
def add_number(a: int, b: int) -> int:
    return a + b


def flatten(lol: list[Any]) -> Generator[Any, None, None]:
    """多次元リストを1次元リストに変換するためのジェネレータ"""
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)  # ↓のコメントと同じ
            # for subitem in flatten(item):
            #     yield subitem
        else:
            yield item


class Person:
    """
    クラスの基礎
    クラス属性非公開化のためのプロパティ、マングリングなど
    """
    kind: str = "Primates"
    __count: int = 0

    def __init__(self, input_name: str) -> None:
        self.__name: str = input_name
        Person.__count += 1

    @property
    def name(self) -> str:
        print("inside the getter")
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        print("inside the setter")
        self.__name = name

    # インスタンスメソッド: インスタンスごとに固有のメソッド
    def greeting(self) -> None:
        print(f"Hi! My name is {self.__name}")

    # クラスメソッド: クラスごとに固有のメソッド
    @classmethod
    def kids(cls) -> None:
        print(f"Person has {cls.__count} little objects")

    # 静的メソッド: 独立してフラフラするよりも都合がいいので、そのクラスの定義の中にあるだけな関数
    @staticmethod
    def explain() -> None:
        print("Person is a primates")

    # 特殊メソッド: 下記は print(), str()などに使われる。他にも色んな種類の特殊メソッドがある
    def __str__(self):
        return self.__name


@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0


# 名前付きタプル：上記とほぼ一緒の意味
AnimalClassTuple = namedtuple('AnimalClassTuple', 'name habitat teeth')


class OopsException(Exception):
    """ 独自例外 """
    pass


#  例外処理
try:
    raise OopsException('uuuuu')
except OopsException as err:
    print(err)

if __name__ == "__main__":
    import sys

    # 参照モジュールのパスが sys.path に入っている。追加は sys.path.insert(0, "path")
    for p in sys.path:
        print(p)

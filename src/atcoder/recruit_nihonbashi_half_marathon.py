class Farm:
    def __init__(self, size: int, last_day: int):
        self.__last_day = last_day
        self.__farm = []
        for _ in range(size):
            self.__farm.append([None] * size)

        self.__now = 0  # 何日目か
        self.__funds = 1
        self.__harvester = 0

    def __actions(self, fn: callable) -> callable:
        def __inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            if self.__last_day == self.__now:
                print(self.__funds)
            else:
                # 　次の日に行く処理
                self.__now += 1
                # 畑の状態更新
            return result

        return __inner

    @__actions
    def buy_harvester(self):
        price = (self.__harvester + 1) ** 3
        if price > self.__funds:
            return
        self.__funds -= price
        self.__harvester += 1
        # 配置する

    @__actions
    def move_harvester(self):
        if self.__harvester == 0:
            return
        # 移動する

    @__actions
    def no_action(self):
        pass

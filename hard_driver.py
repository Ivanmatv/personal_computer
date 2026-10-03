class HardDriver:
    def __init__(self, name: str, memory_size: int):
        self.__name = name
        self.__memory_size = memory_size

    def __repr__(self):
        return f"{self.__name}, {self.__memory_size} GB"

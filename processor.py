class Processor:
    def __init__(self, name: str, frequency: float):
        self.__name = name
        self.__frequency = frequency

    def __repr__(self):
        return f"{self.__name}, {self.__frequency} GHz"

class Processor:
    def __init__(self, name: str, frequency: float):
        self.__name = name
        self.__frequency = frequency

    def __repr__(self):
        return f"{self.__name}, {self.__frequency} GHz"


class VideoCard:
    def __init__(self, name: str, video_memory: int):
        self.__name = name
        self.__video_memory = video_memory

    def __repr__(self):
        return f"{self.__name}, {self.__video_memory} GB"


class HardDriver:
    def __init__(self, name: str, memory_size: int):
        self.__name = name
        self.__memory_size = memory_size

    def __repr__(self):
        return f"{self.__name}, {self.__memory_size} GB"
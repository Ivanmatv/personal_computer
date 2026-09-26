from hardware import Processor, VideoCard, HardDriver


class PersonalComputer:
    def __init__(self, name: str):
        self.__name = name
        self.__processor = ''
        self.__video_card = ''
        self.__hard_driver = ''

    def add_processor(self, processor: str, frequency: float) -> None:
        if isinstance(processor, str) and isinstance(frequency, float):
            self.__processor = Processor(processor, frequency)

    def add_video_card(self, video_card: str, memory_size: int) -> None:
        if isinstance(video_card, str) and isinstance(memory_size, int):
            self.__video_card = VideoCard(video_card, memory_size)

    def add_hard_driver(self, hard_driver: str, memory_size: int) -> None:
        if isinstance(hard_driver, str) and isinstance(memory_size, int):
            self.__hard_driver = HardDriver(hard_driver, memory_size)

    def get_configuration_computer(self) -> str:
        return (
            f'"Model": {self.__name}, '
            f'"Processor": {self.__processor}, '
            f'"Video Card": {self.__video_card}, '
            f'"Hard Driver": {self.__hard_driver}'
        )

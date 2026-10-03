from hard_driver import HardDriver
from processor import Processor
from video_card import VideoCard


class PersonalComputer:
    def __init__(self, name: str):
        self.__name: str = name
        self.__processor = None
        self.__video_card = None
        self.__hard_driver = None

    def add_processor(self, processor_name: str, frequency: float) -> None:
        if isinstance(processor_name, str) and isinstance(frequency, float):
            self.__processor = Processor(processor_name, frequency)

    def add_video_card(self, video_card_name: str, memory_size: int) -> None:
        if isinstance(video_card_name, str) and isinstance(memory_size, int):
            self.__video_card = VideoCard(video_card_name, memory_size)

    def add_hard_driver(self, hard_driver_name: str, memory_size: int) -> None:
        if isinstance(hard_driver_name, str) and isinstance(memory_size, int):
            self.__hard_driver = HardDriver(hard_driver_name, memory_size)

    def get_configuration_computer(self) -> str:
        return (
            f'"Model": {self.__name}, '
            f'"Processor": {self.__processor}, '
            f'"Video Card": {self.__video_card}, '
            f'"Hard Driver": {self.__hard_driver}'
        )

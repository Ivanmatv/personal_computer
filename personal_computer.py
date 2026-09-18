from hardware import Cell, VideoCard, HardDriver


class PersonalComputer:
    def __init__(self, name: str):
        self.__name = name
        self.__cell = []
        self.__video_card = []
        self.__hard_driver = []

    def add_cell(self, name_cell: str, frequency: float) -> None:
        if isinstance(name_cell, str) and isinstance(frequency, float):
            cell = Cell(name_cell, frequency)
            self.__cell.append(cell)

    def add_video_card(self, name_video_card: str, memory_size: int) -> None:
        if isinstance(name_video_card, str) and isinstance(memory_size, int):
            video_card = VideoCard(name_video_card, memory_size)
            self.__video_card.append(video_card)

    def add_hard_driver(self, name_hard_driver: str, memory_size: int) -> None:
        if isinstance(name_hard_driver, str) and isinstance(memory_size, int):
            hard_driver = HardDriver(name_hard_driver, memory_size)
            self.__hard_driver.append(hard_driver)

    def get_configuration_computer(self) -> dict:
        return {
            "Model": self.__name,
            "Cell": self.__cell,
            "Video Card": self.__video_card,
            "Hard Driver": self.__hard_driver
        }

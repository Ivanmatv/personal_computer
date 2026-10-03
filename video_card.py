class VideoCard:
    def __init__(self, name: str, video_memory: int):
        self.__name = name
        self.__video_memory = video_memory

    def __repr__(self):
        return f"{self.__name}, {self.__video_memory} GB"

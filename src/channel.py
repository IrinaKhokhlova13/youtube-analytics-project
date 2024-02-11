import json
from googleapiclient.discovery import build
import isodate
import os

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.info_channel = json.dumps(self.channel, indent=2, ensure_ascii=False)
        self.id = self.channel["items"][0]["id"]
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]


    def __str__(self) -> str:
        return self.url


    def __add__(self, other):
        _add = int(self.subscriber_count) + int(other.subscriber_count)
        return _add


    def __sub__(self, other):
         _sub_1 = int(self.subscriber_count) - int(other.subscriber_count)
         return _sub_1

    def __sub__(self, other):
        _sub_2 = int(other.subscriber_count) - int(self.subscriber_count)
        return _sub_2

    def __gt__(self, other):
        _gt = int(self.subscriber_count) > int(other.subscriber_count)
        return _gt

    def __ge__(self, other):
        _ge = int(self.subscriber_count) >= int(other.subscriber_count)
        return _ge

    def __lt__(self, other):
        _lt = int(self.subscriber_count) < int(other.subscriber_count)
        return _lt

    def __le__(self, other):
        _le = int(self.subscriber_count) <= int(other.subscriber_count)
        return _le

    def __eq__(self, other):
        _eq = int(self.subscriber_count) == int(other.subscriber_count)
        return _eq




    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))
        return youtube

    @property
    def channel_id(self):
        return self.__channel_id

    def to_json(self, file_name):
        moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
        chanel_info = json.loads(self.info_channel)
        with open(file_name, 'w', encoding="utf-8") as file:
            json.dump(f'{chanel_info}\n', file, ensure_ascii=False, indent=2)
            json.dump(f'Название канала: {moscowpython.title}\n', file, ensure_ascii=False, indent=2)
            json.dump(f'Количество просмотров: {moscowpython.video_count}\n', file, ensure_ascii=False)
            json.dump(f'URL адрес канала: {moscowpython.url}\n', file, ensure_ascii=False)

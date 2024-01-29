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
        #в json файле информации о канале нет поля url адреса канала, поэтому я составила структуру url сама
        #Если я сделала это неправильно, то пожалуйста объясните по какому методу YOUTUBE API можно найти url адрес самого канала
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]


    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))
        return youtube

    @property
    def channel_id(self):
        return self.__channel_id


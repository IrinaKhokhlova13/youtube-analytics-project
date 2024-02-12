import json
from googleapiclient.discovery import build
import isodate
import os

class Video:
    """Класс для видео канала"""

    def __init__(self, id_video: str) -> None:
        self.id_video = id_video
        self.youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=id_video).execute()
        self.info_video = json.dumps(self.video_response, indent=2, ensure_ascii=False)
        self._id = self.video_response['items'][0]['id']
        self.title = self.video_response['items'][0]['snippet']['title']
        self.url_video = f"https://www.youtube.com/watch/{self.id_video}"
        self.view_Count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_Count = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title




class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist

    def __str__(self):
        return self.title


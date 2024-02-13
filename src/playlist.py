import json
from googleapiclient.discovery import build
import isodate
import os
import datetime


class PlayList:
    def __init__(self, playlist_id):
        self._playlist_id = playlist_id
        self.youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))
        self.playlist_info = self.youtube.playlists().list(id=playlist_id, part='contentDetails, snippet').execute()
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails, snippet', maxResults=50).execute()
        self.videos_id: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics', id=','.join(self.videos_id)).execute()
        self.print_info = json.dumps(self.video_response, indent=2, ensure_ascii=False)
        self.title = self.playlist_info['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self._playlist_id}"

    @property
    def total_duration(self):
        total_duration = datetime.timedelta()
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += datetime.timedelta(seconds=duration.total_seconds())
        return total_duration

    def show_best_video(self):
        like_count_max = 0
        best_video = ''
        for video in self.video_response['items']:
            like_count: int = video['statistics']['likeCount']
            id_video = video['id']
            if int(like_count) > int(like_count_max):
                like_count_max = like_count
                best_video = id_video
        return f"https://youtu.be/{best_video}"
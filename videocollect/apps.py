from django.apps import AppConfig
from mega import Mega

from video_collect.local_settings import MEGA_ACCOUNT, MEGA_PASS


class VideocollectConfig(AppConfig):
    name = 'videocollect'

    mconnect = None

    def ready(self):
        self.connect_to_mega()

    @classmethod
    def connect_to_mega(cls):
        mega = Mega()
        print(MEGA_ACCOUNT)
        print(MEGA_PASS)
        cls.mconnect = mega.login(MEGA_ACCOUNT, MEGA_PASS)

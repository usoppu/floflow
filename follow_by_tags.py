import sys
from typing import List
from utils import key_exists, key_not_exists
from constants import TAGS, AMOUNT, SKIP_TOP_POSTS, RANDOMIZE, INTERACT, \
    MEDIA, USE_SMART_HASHTAGS, USE_SMART_LOCATION_HASHTAGS


class FollowByTags:
    __tags: List[str] = []
    __amount: int = 0
    __skip_top_posts: bool = True
    __randomize: bool = True
    __interact: bool = False
    __media: str = None
    __use_smart_hashtags: bool = False
    __use_smart_location_hashtags: bool = False
    __session = None

    def __init__(self, config: object, session):
        if config:
            if key_exists(TAGS, config):
                self.__tags = config[TAGS]
            if key_exists(AMOUNT, config):
                self.__amount = config[AMOUNT]
            if key_exists(SKIP_TOP_POSTS, config):
                self.__skip_top_posts = config[SKIP_TOP_POSTS]
            if key_exists(RANDOMIZE, config):
                self.__randomize = config[RANDOMIZE]
            if key_exists(INTERACT, config):
                self.__interact = config[INTERACT]
            if key_exists(MEDIA, config):
                self.__media = config[MEDIA]
            if key_exists(USE_SMART_HASHTAGS, config):
                self.__use_smart_hashtags = config[USE_SMART_HASHTAGS]
            if key_exists(USE_SMART_LOCATION_HASHTAGS, config):
                self.__use_smart_location_hashtags = config[USE_SMART_LOCATION_HASHTAGS]

        if key_not_exists(TAGS, config):
            sys.exit('[ERROR]: tags not found.')
        self.__session = session
        self.__follow_by_tags()

    def __follow_by_tags(self):
        print('[INFO]: Follow by hashtags -> ' + str(self.__tags))
        self.__session.follow_by_tags(
            tags=self.__tags,
            amount=self.__amount,
            skip_top_posts=self.__skip_top_posts,
            use_smart_hashtags=self.__use_smart_hashtags,
            use_smart_location_hashtags=self.__use_smart_location_hashtags,
            randomize=self.__randomize,
            media=self.__media,
            interact=self.__interact
        )

import re

from praw import Reddit

from Common.LoggerCommon.Logger import log_info
from Configurations.RedditConfiguration.RedditConfiguration import RedditConfiguration

THREAD_ID = 'thread_id'


def create_reddit_praw(config: RedditConfiguration):
    return Reddit(
        client_id=config.client_id,
        user_agent=config.user_agent,
        client_secret=config.client_secret
    )


def get_thread_id(reddit_obj: dict):
    """
    This function takes a reddit object and returns the post id
    """
    thread_id = re.sub(r"[^\w\s-]", "", reddit_obj[THREAD_ID])
    log_info(f"Thread ID is {thread_id}")

    return thread_id


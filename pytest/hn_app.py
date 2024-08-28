"""This module provides our simple hacker news app"""

import requests
import random

def get_top_stories(url=None):
    """Fetch top stories from the URL"""
    if url is None:
        url = "https://hacker-news.firebaseio.com/v0/" + \
              "topstories.json?print=pretty"
    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        resp = {'error':str(e)}
    return resp

def get_item(item_id):
    """Fetch item details using items api"""
    url = "https://hacker-news.firebaseio.com/v0/item/" \
          +str(item_id)+".json?print=pretty"
    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        resp = {'error':str(e)}
    return resp

def get_story_top_comment_id(story_id):
    """Fetch story top comment"""
    comment = ""
    resp = get_item(story_id)
    if resp.status_code == 200:
        data = resp.json()
    if data.get('kids', None) is not None:
        comment = data['kids'][0] 
    return comment_id

def get_top_comment_detail(story_id):
    """Fetch story comment detail"""
    comment_id = get_story_top_comment(story_id)
    data = get_item(comment_id)
    if data.status_code == 200:
        return data.json()

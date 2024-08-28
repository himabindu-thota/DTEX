import pytest
import requests
import random
from hn_app import get_top_stories, get_item

@pytest.fixture(scope="module")
def get_data():
    #url = "https://hacker-news.firebaseio.com/v0/" + \
    #          "topstories.json?print=pretty"
    resp = get_top_stories()
    print("Executing")
    story_id = random.choice(resp.json())
    resp = get_item(story_id)
    comment_id = None
    if resp.status_code == 200:
        data = resp.json()
        if data.get('kids', None) is not None:
            comment_id = random.choice(data.get('kids'))    
    if comment_id is not None:
        resp = get_item(comment_id)
        if resp.status_code == 200:
            data = resp.json()
            return data

    return {}

def test_comment_parent(get_data):
    if len(get_data.keys()) > 0:
        assert get_data['parent'] is not None

def test_comment_by(get_data):
    if len(get_data.keys()) > 0:
        assert get_data['by'] is not None

def test_comment_id(get_data):
    if len(get_data.keys()) > 0:
        assert get_data['id'] is not None

def test_comment_type(get_data):
    if len(get_data.keys()) > 0:
        assert get_data['type'] is not None

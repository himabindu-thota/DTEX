"""This module provides API acceptance tests for our hacker news app"""

import requests
import pytest
from hn_app import get_top_stories, get_item
import random

### API reachable ###

def test_api_reachable():
    resp = get_top_stories("https://abcdef_nonexisting")
    assert 'error' in resp.keys() 

### Top Stories Tests ###

def test_top_stories_api_success():
    resp = get_top_stories()
    assert resp.status_code == 200

def test_top_stories_api_returns_500_stories():
    resp = get_top_stories()
    assert len(resp.json()) == 500

def test_top_story_id_integer():
    resp = get_top_stories()
    story_id = random.choice(resp.json())
    assert isinstance(story_id, int) == True

### Comments Tests ###

def test_top_comment():
    resp = get_top_stories()
    story_id = random.choice(resp.json())
    resp = get_item(story_id)
    assert resp.status_code == 200 and isinstance(resp.json()['kids'], list) == True
    
def test_comment_detail():
    resp = get_top_stories()
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
            assert data.get('parent') is not None 
            assert data.get('by') is not None 
            assert data.get('id') is not None 
            assert data.get('type') == 'comment'

### Negative Tests ###

@pytest.mark.xfail(returns=200)
def test_invalid_item_id_1():
    resp = get_top_stories()
    story_id = str(random.choice(resp.json()))
    story_id = story_id[:3]+"!"+story_id[3:]
    resp = get_item(story_id)
    assert resp.status_code == 400

#@pytest.mark.xfail(returns=200)
def test_invalid_item_id_2():
    resp = get_top_stories()
    story_id = str(random.choice(resp.json()))
    story_id = story_id[:3]+"@"+story_id[3:]
    resp = get_item(story_id)
    assert resp.status_code == 400

def test_invalid_item_id_3():
    resp = get_top_stories()
    story_id = str(random.choice(resp.json()))
    story_id = story_id[:3]+"$"+story_id[3:]
    print(story_id)
    resp = get_item(story_id)
    assert resp.status_code == 400

### Unreachable API raises exception ###

def unreachable_api():
    url = "https://hacker-news.firebaseio1.com/v0/" + \
              "topstories.json?print=pretty"
    resp = requests.get(url)

def test_unreachable_api():
    with pytest.raises(requests.exceptions.ConnectionError):
        unreachable_api()

### Get all 500 stories in top stories one at a time ###
@pytest.mark.burst
def test_get_all_top_stories_and_iterate():
    print('\n\n *** NOTE: This test takes about 2 mins to complete. ' + \
           'To skip next time use -m "not burst" flag')
    resp_top = get_top_stories()
    assert resp_top.status_code == 200
    for story_id in resp_top.json():
        resp_story = get_item(story_id)
        assert resp_story.status_code == 200

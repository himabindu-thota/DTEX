"""This module provides API acceptance tests for our hacker news app"""

import requests
import pytest
from hn_app import get_top_stories, get_item
import random

class Test_Top_Stories:

    ### Top Stories Tests ###

    def test_top_stories_api_success(self):
        resp = get_top_stories()
        assert resp.status_code == 200

    def test_top_stories_api_returns_500_stories(self):
        resp = get_top_stories()
        assert len(resp.json()) == 500

    def test_top_story_id_integer(self):
        resp = get_top_stories()
        story_id = random.choice(resp.json())
        assert isinstance(story_id, int) == True

class Test_Story_Comments:

    ### Story Comments Tests ###

    def test_top_comment(self):
        resp = get_top_stories()
        story_id = random.choice(resp.json())
        resp = get_item(story_id)
        assert resp.status_code == 200 and isinstance(resp.json()['kids'], list) == True
    
    def test_comment_detail(self):
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

class Test_Item_Id_Negative_Tests:

    ### Negative Tests ###

    @pytest.mark.xfail(returns=200)
    def test_invalid_item_id_1(self):
        resp = get_top_stories()
        story_id = str(random.choice(resp.json()))
        story_id = story_id[:3]+"!"+story_id[3:]
        resp = get_item(story_id)
        assert resp.status_code == 400

    @pytest.mark.xfail(returns=200)
    def test_invalid_item_id_2(self):
        resp = get_top_stories()
        story_id = str(random.choice(resp.json()))
        story_id = story_id[:3]+"@"+story_id[3:]
        resp = get_item(story_id)
        assert resp.status_code == 400

    @pytest.mark.xfail(returns=200)
    def test_invalid_item_id_3(self):
        resp = get_top_stories()
        story_id = str(random.choice(resp.json()))
        story_id = story_id[:3]+"$"+story_id[3:]
        resp = get_item(story_id)
        assert resp.status_code == 400

    @pytest.mark.xfail(raises=requests.exceptions.JSONDecodeError)
    def test_get_story_with_non_integer_item_id_2(self):
        resp = get_top_stories()
        data = resp.json()
        story_id = str(data[5])
        story_id += "#"
        resp = get_item(story_id)
        assert isinstance(resp.json(), dict)

    @pytest.mark.xfail(returns=200)
    def test_invalid_item_id_4(self):
        resp = get_top_stories()
        data = resp.json()
        story_id = str(data[5])
        story_id += "#"
        resp = get_item(story_id)
        assert resp.status_code == 400

class Test_Unreachable_APIs:

    ### API reachable ###

    def test_api_reachable(self):
        resp = get_top_stories("https://abcdef_nonexisting")
        assert 'error' in resp.keys() 

    ### Unreachable API raises exception ###

    def unreachable_api(self):
        url = "https://hacker-news.firebaseio1.com/v0/" + \
              "topstories.json?print=pretty"
        resp = requests.get(url)

    def test_unreachable_api(self):
        with pytest.raises(requests.exceptions.ConnectionError):
            self.unreachable_api()

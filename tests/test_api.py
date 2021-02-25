from models import Song, Podcast, Audiobook
from flask import jsonify, json
# import requests
# url = 'http://127.0.0.1:5000'
def test_get_song(test_client):
  
    # Song('test song', 1200)
    response = test_client.get('/song')
    assert response.status_code == 200
    # assert b"Haha" in response.data
    # assert b"Existing user?" in response.data

def test_post_song(test_client):
    
    data=json.dumps({'name': "test song", 'duration': 2000})
    response = test_client.post('/song', data=data, content_type='application/json')
    assert response.status_code == 201
    assert b"Song added" in response.data
    assert b"Test" not in response.data

def test_update_song(test_client):
    
    datar=json.dumps({
        'name': "test song 1", 
        'duration': 2000
        })
    response = test_client.put('/song/11', data=datar, content_type='application/json')
    assert response.status_code == 201
    assert b"Song updated" in response.data
    assert b"Test" not in response.data

def test_delete_song(test_client):
    response = test_client.delete('/song/12', content_type='application/json')
    assert response.status_code == 200
    assert b"Song Deleted" in response.data
    assert b"Test" not in response.data


def test_get_podcast(test_client):
  
    # Song('test song', 1200)
    response = test_client.get('/podcast')
    assert response.status_code == 200
    # assert b"Haha" in response.data
    # assert b"Existing user?" in response.data

def test_post_podcast(test_client):
    
    data=json.dumps({
        'title': "My show", 'author': "akoh",
        'narrator': "john fache", 'duration': 2000,
        'host': "Audiomack"
        })
    response = test_client.post('/podcast', data=data, content_type='application/json')
    assert response.status_code == 201
    assert b"Podcast added" in response.data
    assert b"Test" not in response.data

def test_update_podcast(test_client):
    
    data=json.dumps({
        'title': "My show new", 'author': "akoh",
        'narrator': "john fache", 'duration': 2000,
        'host': "Audiomack"
        })
    response = test_client.put('/podcast/4', 
                              data=data, content_type='application/json')
    assert response.status_code == 201
    assert b"Podcast Updated" in response.data
    assert b"Test" not in response.data

def test_delete_podcast(test_client):

    response = test_client.delete('/podcast/4', content_type='application/json')
    assert response.status_code == 200
    assert b"Podcast Deleted" in response.data
    assert b"Test" not in response.data


def test_get_audiobook(test_client):
  
    # Song('test song', 1200)
    response = test_client.get('/audiobook')
    assert response.status_code == 200
    # assert b"Haha" in response.data
    # assert b"Existing user?" in response.data

def test_post_audiobook(test_client):
    
    data=json.dumps({
        'title': "My book", 'author': "akoh",
        'narrator': "steven", 'duration': 2000,
        
        })
    response = test_client.post('/audiobook', data=data, content_type='application/json')
    assert response.status_code == 201
    assert b"AudioBook added" in response.data
    assert b"Test" not in response.data

def test_update_audiobook(test_client):
    
    data=json.dumps({
        'title': "My book new", 'author': "akoh",
        'narrator': "steven durag", 'duration': 3000,
        })
    response = test_client.put('/audiobook/4', data=data, content_type='application/json')
    assert response.status_code == 201
    assert b"AudioBook Updated" in response.data
    assert b"Test" not in response.data

def test_delete_audiobook(test_client):
    response = test_client.delete('/audiobook/4', content_type='application/json')
    assert response.status_code == 200
    assert b"AudioBook Deleted" in response.data
    assert b"Test" not in response.data
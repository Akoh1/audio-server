from models import Song, Podcast, Audiobook

def test_new_song():
    """
    GIVEN a Song model
    WHEN a new Song is created
    THEN check the name, and duration are defined correctly
    """
    new_song = Song('test song', 1200)
    assert new_song.name == 'test song'
    assert new_song.duration == 1200

def test_new_podcast():
    """
    GIVEN a Podcast model
    WHEN a new Podcast is created
    THEN check the attributes are defined correctly
    """
    podcast = Podcast("A test podcast", "john", "myself", 12000, "youtube")
    assert podcast.title == 'A test podcast'
    assert podcast.author == 'john'
    assert podcast.narrator == 'myself'
    assert podcast.duration == 12000
    assert podcast.host == 'youtube'

def test_new_audiobook():
   
    audio = Audiobook("48 laws of power", "samuel", "prince", 12000)
    assert audio.title == '48 laws of power'
    assert audio.author == 'samuel'
    assert audio.narrator == 'prince'
    assert audio.duration == 12000
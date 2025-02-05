from game import Game
from exceptions import RatingError

def test_title():
    game = Game()
    assert game.title == None
    game.title = "Test Title"
    assert game.title == "Test Title"

def test_developer():
    game = Game()
    assert game.developer == None
    game.developer = "Test Developer"
    assert game.developer == "Test Developer"
    
def test_genre():
    game = Game()
    assert game.genre == None
    game.genre = "Test Genre"
    assert game.genre == "Test Genre"

    
def test_platform():
    game = Game()
    assert game.platform == None
    game.platform = "Test Platform"
    assert game.platform == "Test Platform"

def test_release():
    game = Game()
    assert game.release == None
    game.release = "Test Release"
    assert game.release == "Test Release"

def test_complete():
    game = Game()
    assert game.complete == None
    game.complete = "Test Complete"
    assert game.complete == "Test Complete"

def test_rating():
    game = Game()
    assert game.rating == None
    try:
        game.rating = 6
    except RatingError:
        pass
    assert game.rating == None
    try:
        game.rating = 0
    except RatingError:
        assert game.rating == None
    try:
        game.rating = 1
    except RatingError:
        pass
    assert game.rating == 1
from game import Game

def test_title():
    game = Game()
    assert game.title == ""
    game.title = "Test Title"
    assert game.title == "Test Title"

def test_developer():
    game = Game()
    assert game.developer == ""
    game.developer = "Test Developer"
    assert game.developer == "Test Developer"
    
def test_genre():
    game = Game()
    assert game.genre == ""
    game.genre = "Test Genre"
    assert game.genre == "Test Genre"

    
def test_platform():
    game = Game()
    assert game.platform == ""
    game.platform = "Test Platform"
    assert game.platform == "Test Platform"

def test_release():
    game = Game()
    assert game.release == ""
    game.release = "Test Release"
    assert game.release == "Test Release"

def test_complete():
    game = Game()
    assert game.complete == ""
    game.complete = "Test Complete"
    assert game.complete == "Test Complete"

def test_rating():
    game = Game()
    assert game.rating == 0
    try:
        game.rating = "6"
    except ValueError:
        pass
    assert game.rating == 0
    try:
        game.rating = "-1"
    except ValueError:
        assert game.rating == 0
    try:
        game.rating = "1"
    except ValueError:
        pass
    assert game.rating == 1

def test_str():
    game = Game()
    game.title = "Test Title"
    game.developer = "Test Developer"
    game.genre = "Test Genre"
    game.platform = "Test Platform"
    game.release = "Test Release"
    game.complete = "Test Complete"
    game.rating = "4"
    print(game)

if __name__ == "__main__":
    test_str()
from lib.exceptions import RatingError

class Game:

    def __init__(self):
        self._title = None
        self._developer = None
        self._genre = None
        self._platform = None
        self._release = None
        self._complete = None
        self._rating = None


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, text):
        self._title = text
    
    @property
    def developer(self):
        return self._developer
    
    @developer.setter
    def developer(self, text):
        self._developer = text
    
    @property
    def release(self):
        
        return self._release
    
    @release.setter
    def release(self, text):   
        self._release = text
    
    @property
    def complete(self):
        return self._complete
    
    @complete.setter
    def complete(self, text):
        self._complete = text
    
    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, text):
        self._genre = text
    
    @property
    def platform(self):
        return self._platform
    
    @platform.setter
    def platform(self, text):
        self._platform = text

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, number):
        if number < 1 or number > 5:
            raise RatingError(number,"Rating outside accepted range")
        else:
            self._rating = number

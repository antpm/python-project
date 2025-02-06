class Game:

    def __init__(self):
        self._title:str = None
        self._developer:str = None
        self._genre:str = None
        self._platform:str = None
        self._release:str = None
        self._complete:str = None
        self._rating:int = None


    @property
    def title(self)->str:
        return self._title
    
    @title.setter
    def title(self, text:str):
        self._title = text
    
    @property
    def developer(self)->str:
        return self._developer
    
    @developer.setter
    def developer(self, text:str):
        self._developer = text
    
    @property
    def release(self)->str:
        return self._release
    
    @release.setter
    def release(self, text:str):   
        self._release = text
    
    @property
    def complete(self)->str:
        return self._complete
    
    @complete.setter
    def complete(self, text:str):
        self._complete = text
    
    @property
    def genre(self)->str:
        return self._genre
    
    @genre.setter
    def genre(self, text:str):
        self._genre = text
    
    @property
    def platform(self)->str:
        return self._platform
    
    @platform.setter
    def platform(self, text:str):
        self._platform = text

    @property
    def rating(self)->int:
        return self._rating
    
    @rating.setter
    def rating(self, number:int):
        if number < 1 or number > 5:
            raise ValueError("Rating outside accepted range")
        else:
            self._rating = number

    def __str__(self)->str:
        return f"Title: {self._title}\nDeveloper: {self._developer}\nGenre: {self._genre}\nPlatform: {self._platform}\nRelease Date: {self._release}\nCompletion Date: {self._complete}\nRating: {self._rating}/5"

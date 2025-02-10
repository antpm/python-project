from validator_collection import validators,errors
from tabulate import tabulate

class Game:

    def __init__(self,title="", developer="",genre="",platform="",release="",complete="",rating=0):
        self._title:str = title
        self._developer:str = developer
        self._genre:str = genre
        self._platform:str = platform
        self._release:str = release
        self._complete:str = complete
        self._rating:int = rating


    @property
    def title(self)->str:
        return self._title
    
    @title.setter
    def title(self, text:str):
        if text == "":
            raise ValueError("Title cannot be blank")
        else:
            self._title = text
    
    @property
    def developer(self)->str:
        return self._developer
    
    @developer.setter
    def developer(self, text:str):
        if text == "":
            raise ValueError("Developer cannot be blank")
        else:
            self._developer = text
    
    @property
    def release(self)->str:
        return self._release
    
    @release.setter
    def release(self, text:str):   
        if text == "":
            raise ValueError("Release Date cannot be blank")
        else:
            try:
                validators.date(text)
            except errors.CannotCoerceError:
                raise ValueError("Invalid date")
            else:
                self._release = text
    
    @property
    def complete(self)->str:
        return self._complete
    
    @complete.setter
    def complete(self, text:str):
        if text == "":
            raise ValueError("Completion Date cannot be blank")
        else:
            try:
                validators.date(text)
            except errors.CannotCoerceError:
                raise ValueError("Invalid date")
            else:
                self._complete = text
    
    @property
    def genre(self)->str:
        return self._genre
    
    @genre.setter
    def genre(self, text:str):
        if text == "":
            raise ValueError("Genre cannot be blank")
        else:
            self._genre = text
    
    @property
    def platform(self)->str:
        return self._platform
    
    @platform.setter
    def platform(self, text:str):
        if text == "":
            raise ValueError("Platform cannot be blank")
        else:
            self._platform = text

    @property
    def rating(self)->int:
        return self._rating
    
    @rating.setter
    def rating(self, text:str):
        if text == "":
            raise ValueError("Rating cannot be blank")
        else:
            try:
                num = int(text)
            except ValueError:
                raise ValueError("Rating must be a number")
            else:
                if num < 1 or num > 5:
                    raise ValueError("Rating outside accepted range")
                else:
                    self._rating = num

    def __str__(self)->str:
        return f"Title: {self._title}\nDeveloper: {self._developer}\nGenre: {self._genre}\nPlatform: {self._platform}\nRelease Date: {self._release}\nCompletion Date: {self._complete}\nRating: {self._rating}/5"

    def full_list_data(self, num:int)->list:
        return [num, self._title,self._developer,self._genre,self._platform,self._release,self._complete,f"{self._rating}/5"]
        
    
    def short_list_data(self, num:int)->list:
        return [num, self._title]
    
    def dict_convert(self)->dict:
        return {"title":self._title, "developer":self._developer, "genre":self._genre,"platform":self._platform,"release date":self._release, "complete date":self._complete,"rating":self._rating}
class RatingError(Exception):
    def __init__(self, rating, msg):
        self.msg = msg
        self.rating = rating
    def __str__(self):
        return f"{self.rating}->{self.msg}"
from Project import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(2000), nullable=False)
    short_code = db.Column(db.String(8), nullable=False, unique=True)

    def __init__(self, long_url, short_code):
        self.long_url = long_url
        self.short_code = short_code

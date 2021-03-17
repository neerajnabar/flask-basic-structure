from api import db

class Product(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(280), unique=False, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.title

from app import app
from app import db
from sqlalchemy.sql import func

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release = db.Column(db.String(55))
    director = db.Column(db.String(200))
    genre = db.Column(db.String(100))
    
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<Movie id={self.id} title={self.title} released={self.released}>"
    
    def __init__(self, title, release, director, genre):
        self.title = title
        self.release = release
        self.director = director
        self.genre = genre
    
    def save(self):
        db.session.add(self)
        db.session.commit()
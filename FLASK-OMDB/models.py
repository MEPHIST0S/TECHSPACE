from app import app
from app import db
from sqlalchemy.sql import func

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    year = db.Column(db.String(10))
    plot = db.Column(db.String(10))
    status = db.Column(db.Boolean, default = "True")
    poster = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<Movie id={self.id} title={self.title} year={self.year}>"
    
    def __init__(self, title, year, plot, status, poster):
        self.title = title
        self.year = year
        self.plot = plot
        self.poster = poster
        self.status = status
    
    def save(self):
        db.session.add(self)
        db.session.commit()
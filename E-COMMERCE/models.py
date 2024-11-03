from app import db
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import CheckConstraint

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    parent = db.relationship('Category', remote_side=[id], backref=db.backref('children', uselist=True))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __str__(self):
        return self.name
    

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)
    additional_images = db.Column(db.Text)
    discounted_price = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    parent_category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    category = db.relationship('Category', foreign_keys=[category_id], backref=db.backref('products', uselist=True))
    parent_category = db.relationship('Category', foreign_keys=[parent_category_id], backref=db.backref('parent_products', uselist=True))
    reviews = db.relationship('Review', backref='product_reviews', lazy=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    @property
    def additional_images_list(self):
        if self.additional_images:
            return self.additional_images.split(', ')
        return []
    
    @property
    def reviews_count(self):
        return len(self.reviews)

    def __str__(self):
        return self.name
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    otp = db.Column(db.String(6), nullable=True)
    otp_verified = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

    # RELATION WITH ADDITIONAL FAVORITES TABLE
    favorite_products = db.relationship('Product', secondary='user_favorites', backref='users_favorites')

    # ADDITIONAL FAVORITES TABLE
    user_favorites = db.Table('user_favorites',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
        db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
    )

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __str__(self):
        return self.username
    
class ContactMessage(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f'<ContactMessage {self.name} - {self.email}>'

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    product = db.relationship('Product')

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='rating_range'),
    )

    def __str__(self):
        return f"Review by {self.user.name} for {self.product.name}"
    
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f'<Subscriber {self.name}>'

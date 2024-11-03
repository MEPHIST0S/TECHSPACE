from flask_admin.contrib.sqla import ModelView
from app import admin, db
from models import Category, Product, Review, User, ContactMessage
from extensions import *

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

admin.add_view(MyModelView(Category, db.session, name="Categories"))
admin.add_view(MyModelView(Product, db.session, name="Products"))
admin.add_view(MyModelView(Review, db.session, name="Reviews"))
admin.add_view(MyModelView(User, db.session, name="Users"))
admin.add_view(MyModelView(ContactMessage, db.session, name="Contacts"))
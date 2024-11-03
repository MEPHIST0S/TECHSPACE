from extensions import *

#CREATION OF FLASK INSTANCE WITH THE NAME ASSIGNMENT TO "app"
app = Flask(__name__)

#CONFIGURATION OF SQLALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4444@localhost:3308/CINEMA'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from tools import *  
from models import *

#CONDITION FOR EXECUTION SCRIPTS OF THIS FILE AS MAIN FILE
if __name__ == '__main__':
    app.run(debug=True) #FOR OBSERVING ERRORS